#!/usr/bin/env python3
"""
socarframe_scrape.py — Render socarframe.socar.kr (a client-rendered Docusaurus SPA)
with headless Chrome and convert each doc page's <article> into clean Markdown.

Why headless Chrome: every route returns an identical SPA shell over plain HTTP;
the real content is hydrated client-side, so curl/WebFetch see nothing useful.

Usage:
  python3 tools/socarframe_scrape.py --list            # print known doc paths
  python3 tools/socarframe_scrape.py PATH [PATH ...]    # render specific paths
  python3 tools/socarframe_scrape.py --all              # render every known path

Output: one Markdown file per page under /tmp/sf_raw/<slug>.md
"""
import sys, os, re, html, subprocess, argparse, time, signal
from html.parser import HTMLParser

BASE = "https://socarframe.socar.kr"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTDIR = "/tmp/sf_raw"

PATHS = [
    "/development/principle",
    "/development/foundation",
    "/development/foundation/Colors",
    "/development/foundation/Typography",
    "/development/foundation/Spacing",
    "/development/foundation/Icons",
    "/development/components",
    "/development/components/Accordion",
    "/development/components/Alert",
    "/development/components/Badge",
    "/development/components/BottomSheet",
    "/development/components/Buttons",
    "/development/components/Buttons/ActionButton",
    "/development/components/Buttons/IconButton",
    "/development/components/Buttons/TextButton",
    "/development/components/Checkbox",
    "/development/components/Chip",
    "/development/components/DatePicker",
    "/development/components/Haptic",
    "/development/components/Input",
    "/development/components/Pattern",
    "/development/components/Pattern/Carousel",
    "/development/components/Radio",
    "/development/components/SegmentedControl",
    "/development/components/SelectionBox",
    "/development/components/Skeleton",
    "/development/components/Snackbar",
    "/development/components/Tab",
    "/development/components/Tag",
    "/development/components/TextArea",
    "/development/components/TimePicker",
    "/development/components/Tips",
    "/development/components/Tips/AccentTip",
    "/development/components/Tips/InfoTip",
    "/development/components/TopAppBar",
    "/docs/foundation",
    "/docs/guidelines",
    "/docs/migration",
    "/docs/principle",
    "/docs/resources",
    "/ux-principles/overview",
    "/ux-principles/release-checklist",
    "/ux-principles/trade-off-rules",
    "/ux-principles/wow-moment",
]


def slug(path):
    return path.strip("/").replace("/", "__")


def render(path, profile_id, wall=25):
    """Chrome --dump-dom reliably writes the hydrated DOM but then hangs on exit.
    So: stream stdout to a temp file, poll until the DOM is complete (</html>),
    then force-kill the process tree. Returns the captured DOM string."""
    url = BASE + path
    tmpf = f"/tmp/sf_dump_{profile_id}_{slug(path)}.html"
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", "--disable-software-rasterizer",
        "--no-first-run", "--no-default-browser-check", "--mute-audio",
        f"--user-data-dir=/tmp/sf_chrome_{profile_id}",
        "--virtual-time-budget=8000",
        "--dump-dom", url,
    ]
    with open(tmpf, "w") as fh:
        proc = subprocess.Popen(cmd, stdout=fh, stderr=subprocess.DEVNULL,
                                start_new_session=True)
        deadline = time.monotonic() + wall
        done = False
        while time.monotonic() < deadline:
            time.sleep(0.5)
            if proc.poll() is not None:
                done = True
                break
            try:
                with open(tmpf) as r:
                    head = r.read()
                # dump is complete once the closing tag and real article text exist
                if "</html>" in head and "<article" in head:
                    done = True
                    break
            except OSError:
                pass
        # force-kill the (possibly hung) Chrome process group
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
    with open(tmpf) as r:
        return r.read()


class MD(HTMLParser):
    """Minimal but structure-preserving HTML->Markdown for Docusaurus articles."""
    SKIP = {"script", "style", "nav", "svg", "button", "footer", "head"}

    def __init__(self):
        super().__init__()
        self.out = []
        self.skip_depth = 0
        self.in_article = False
        self.article_depth = 0
        self.tag_stack = []
        # table state
        self.in_table = False
        self.row = None
        self.rows = []
        self.in_cell = False
        self.cell = ""
        self.header_done = False
        self.list_stack = []
        self.pre = False

    def emit(self, s):
        if not self.in_article:
            return
        self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "article":
            self.in_article = True
            self.article_depth = 1
            return
        if self.in_article and tag == "article":
            self.article_depth += 1
        if tag in self.SKIP:
            self.skip_depth += 1
            return
        if self.skip_depth or not self.in_article:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.emit("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self.emit("\n\n")
        elif tag == "br":
            self.emit("  \n")
        elif tag in ("strong", "b"):
            self.emit("**")
        elif tag in ("em", "i"):
            self.emit("_")
        elif tag == "code" and not self.pre:
            self.emit("`")
        elif tag == "pre":
            self.pre = True
            self.emit("\n\n```\n")
        elif tag == "ul":
            self.list_stack.append("ul")
        elif tag == "ol":
            self.list_stack.append("ol")
        elif tag == "li":
            indent = "  " * (len(self.list_stack) - 1)
            self.emit("\n" + indent + "- ")
        elif tag == "img":
            alt = a.get("alt", "").strip()
            src = a.get("src", "")
            if alt or src:
                self.emit(f"![{alt}]({src})")
        elif tag == "table":
            self.in_table = True
            self.rows = []
            self.header_done = False
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.in_cell = True
            self.cell = ""

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if tag == "article" and self.in_article:
            self.article_depth -= 1
            if self.article_depth <= 0:
                self.in_article = False
            return
        if tag in self.SKIP:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth or not self.in_article:
            return
        if tag in ("strong", "b"):
            self.emit("**")
        elif tag in ("em", "i"):
            self.emit("_")
        elif tag == "code" and not self.pre:
            self.emit("`")
        elif tag == "pre":
            self.pre = False
            self.emit("\n```\n")
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
        elif tag in ("td", "th"):
            self.in_cell = False
            if self.row is not None:
                self.row.append(re.sub(r"\s+", " ", self.cell).strip())
        elif tag == "tr":
            if self.row is not None:
                self.rows.append(self.row)
            self.row = None
        elif tag == "table":
            self.in_table = False
            self.flush_table()

    def flush_table(self):
        if not self.rows:
            return
        ncol = max(len(r) for r in self.rows)
        self.emit("\n\n")
        for i, r in enumerate(self.rows):
            cells = r + [""] * (ncol - len(r))
            self.emit("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |\n")
            if i == 0:
                self.emit("| " + " | ".join(["---"] * ncol) + " |\n")
        self.emit("\n")

    def handle_data(self, data):
        if self.skip_depth or not self.in_article:
            return
        if self.in_cell:
            self.cell += data
            return
        if self.pre:
            self.emit(data)
            return
        text = data
        if text.strip() == "":
            # preserve a single space for inline flow
            if self.out and not self.out[-1].endswith((" ", "\n")):
                self.emit(" ")
            return
        self.emit(text)


def to_markdown(dom_html, title_path):
    p = MD()
    try:
        p.feed(dom_html)
    except Exception as e:
        return f"<!-- parse error: {e} -->\n"
    md = "".join(p.out)
    md = html.unescape(md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    return md.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--profile", default="0")
    args = ap.parse_args()
    if args.list:
        print("\n".join(PATHS))
        return
    paths = PATHS if args.all else args.paths
    if not paths:
        print("no paths; use --all or pass paths or --list", file=sys.stderr)
        sys.exit(1)
    os.makedirs(OUTDIR, exist_ok=True)
    for path in paths:
        try:
            dom = render(path, args.profile)
            md = to_markdown(dom, path)
            outp = os.path.join(OUTDIR, slug(path) + ".md")
            header = f"# SOURCE: {BASE}{path}\n\n"
            with open(outp, "w") as f:
                f.write(header + md + "\n")
            print(f"OK  {path}  ({len(md)} chars) -> {outp}")
        except Exception as e:
            print(f"ERR {path}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
