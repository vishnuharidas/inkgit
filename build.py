#!/usr/bin/env python3
"""
build.py - Convert all markdown files in /data to minified HTML.

Outputs everything to a flat dist/ directory (HTML files, index.html, inkgit.js)
for clean serving via GitHub Pages.

Usage:
    python build.py [--data-dir data] [--output-dir dist]
"""

import argparse
import shutil
import sys
from pathlib import Path

import minify_html
from markdown_it import MarkdownIt
from rjsmin import jsmin

ASSETS_DIR = Path(__file__).parent / "assets"


def convert_md(src: Path, md: MarkdownIt) -> str:
    """Convert a markdown file to minified HTML."""
    content = src.read_text(encoding="utf-8")
    html = md.render(content)
    return minify_html.minify(html, keep_closing_tags=True)


def build_index(files: list[dict]) -> str:
    """Generate index.html from the template in assets/."""
    template = (ASSETS_DIR / "index.html").read_text(encoding="utf-8")

    content = ""
    for f in files:
        content += f'\n\n<h2 class="file-title">{f["name"]}.md</h2>\n<div data-inkgit="{f["html_file"]}"></div>'

    base = "https://&lt;username&gt;.github.io/&lt;repo&gt;"
    snippet_lines = "\n".join(
        f'&lt;div data-inkgit="{base}/{f["html_file"]}"&gt;&lt;/div&gt;'
        for f in files
    )
    snippet_lines += f'\n\n&lt;script async src="{base}/inkgit.min.js"&gt;&lt;/script&gt;'
    snippet_lines += '\n\n&lt;!-- Optional credit --&gt;'
    snippet_lines += '\n&lt;p&gt;Powered by &lt;a href="https://github.com/vishnuharidas/inkgit"&gt;Inkgit🫟&lt;/a&gt;'
    snippet_lines += ' · &lt;a href="https://&lt;username&gt;.github.io/&lt;repo&gt;/"&gt;View source&lt;/a&gt;&lt;/p&gt;'

    html = template.replace("{{CONTENT}}", content).replace("{{SNIPPET}}", snippet_lines)
    return html


def main():
    parser = argparse.ArgumentParser(description="Build HTML from markdown files")
    parser.add_argument("--data-dir", default="data", help="Directory containing .md files (default: data)")
    parser.add_argument("--output-dir", default="dist", help="Output directory for built files (default: dist)")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output_dir)

    if not data_dir.is_dir():
        print(f"Error: {data_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(data_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {data_dir}")
        sys.exit(0)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Clean stale HTML files from previous builds
    for old in output_dir.glob("*.html"):
        old.unlink()

    md = MarkdownIt("commonmark", {"html": True}).enable(["table"])

    files = []

    for src in md_files:
        html = convert_md(src, md)
        dst = output_dir / f"{src.stem}.html"
        dst.write_text(html, encoding="utf-8")
        files.append({"name": src.stem, "html_file": dst.name})
        print(f"  {src.name} -> {dst.name}")

    # Build index.html from template
    index_html = build_index(files)
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")
    print("  index.html")

    # Copy inkgit.js and create minified version
    js_src = ASSETS_DIR / "inkgit.js"
    if js_src.is_file():
        shutil.copy2(js_src, output_dir / "inkgit.js")
        js_minified = jsmin(js_src.read_text(encoding="utf-8"))
        (output_dir / "inkgit.min.js").write_text(js_minified, encoding="utf-8")
        print(f"  inkgit.js + inkgit.min.js")

    print(f"\nBuilt {len(files)} file(s) into {output_dir}/.")


if __name__ == "__main__":
    main()
