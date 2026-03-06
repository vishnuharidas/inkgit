# CLAUDE.md

## Project Overview

**Inkgit🫟** (pronounced /ˈɪŋk.ɡɪt/) — Ink + Git. A lightweight, fork-and-go project that turns markdown files into embeddable HTML pages served via GitHub Pages. No build tools on the user's site, no frameworks, no runtime dependencies.

**Core idea:** Users maintain markdown files (TIL entries, updates, notes, etc.) in a GitHub repo. A GitHub Action auto-converts them to minified HTML. Their blog/site fetches and displays the HTML with a tiny embed script.

## Architecture

```
├── build.py                    # Python script: MD → minified HTML converter
├── assets/
│   ├── inkgit.js               # Browser script: fetches and injects HTML into divs
│   └── index.html              # Template for the standalone viewer page
├── data/
│   └── *.md                    # User's markdown files (source of truth)
├── dist/                       # Build output (auto-generated, not committed)
│   ├── *.html                  # Minified HTML from each .md file
│   ├── index.html              # Generated standalone viewer
│   ├── inkgit.js               # Full version (copied from assets/)
│   └── inkgit.min.js           # Minified version (for embedding)
├── .github/
│   └── workflows/
│       └── build.yml           # GitHub Action: build + deploy to Pages
├── README.md                   # User-facing setup instructions
├── LICENSE                     # MIT
└── CLAUDE.md                   # This file
```

## How It Works

1. User writes/edits markdown files in `data/` folder
2. On push to `main`, GitHub Action runs `build.py`
3. `build.py` cleans stale HTML files from `dist/` and converts each `data/*.md` to minified HTML
4. `build.py` copies `assets/inkgit.js` into `dist/` and generates `dist/inkgit.min.js` (minified via `rjsmin`)
5. `build.py` generates `dist/index.html` from the `assets/index.html` template
6. GitHub Action deploys `dist/` to GitHub Pages (via `actions/deploy-pages`)
7. User's site uses `inkgit.min.js` to fetch HTML and inject into `<div data-inkgit="URL">` elements

## Technical Details

### build.py
- Uses `markdown-it-py` (CommonMark compliant, handles fenced code blocks inside list items correctly — Python's `markdown` library does NOT handle this well)
- HTML minification via `minify-html` (Rust-based, preserves `<pre>` whitespace automatically)
- Generates `index.html` from `assets/index.html` template (replaces `{{CONTENT}}` and `{{SNIPPET}}` placeholders)
- Copies `assets/inkgit.js` into the output directory and generates a minified `inkgit.min.js` via `rjsmin`
- CLI: `python build.py [--data-dir data] [--output-dir dist]`
- Dependencies: `pip install markdown-it-py minify-html rjsmin`

### assets/inkgit.js
- Zero dependencies, vanilla JS, IIFE pattern
- Finds all elements with `data-inkgit` attribute, fetches the URL, injects innerHTML
- Optional `data-inkgit-class` attribute to add a CSS class to the container
- Shows "Loading…" while fetching, "Failed to load content." on error
- Uses `DOMContentLoaded` guard — safe to load with `async` attribute, works regardless of script placement
- Uses `fetch` API — works in all modern browsers

### assets/index.html
- Template for the standalone viewer / preview page
- Uses `{{CONTENT}}` placeholder for the data-inkgit divs (each file gets a styled `h2.file-title` header + a `data-inkgit` div)
- Uses `{{SNIPPET}}` placeholder for the embed code example (includes optional credit linking to Inkgit and source repo)
- Intro callout box (blue left border) explains this is a preview and points to the embed snippet
- File titles are prominent: gray background, dark left border, bold, with 📄 prefix via CSS
- Loads `inkgit.min.js` itself — acts as a real showcase of the embed script

### GitHub Action
- Triggers on changes to `data/*.md`, `assets/**`, or `build.py` on `main` branch
- Uses `actions/upload-pages-artifact` + `actions/deploy-pages` to deploy `dist/`
- No generated files committed to the repo — clean separation of source and output

### Why GitHub Pages instead of raw.githubusercontent.com
- GitHub tightened rate limits on `raw.githubusercontent.com` for unauthenticated requests (as of mid-2025)
- Unauthenticated API limit is ~60 requests/hour/IP — too low for a public site
- GitHub Pages is designed for serving static content to the public with generous limits
- No third-party CDN dependency (considered and rejected jsDelivr as overkill)

## Design Decisions

- **Single markdown file per topic** (not one file per entry) — keeps things simple, user just appends to a list
- **List format with bold dates** works well: `- **2026-03-06** — Content here`
- **Minified HTML output** — since the user's site already has CSS, we output unstyled HTML fragments (standard tags: h1, ul, li, code, pre, strong, etc.)
- **The `data-inkgit` attribute pattern** was chosen over custom element names or magic class names because it's standard HTML, self-documenting (the URL is right there), and supports multiple embeds on one page naturally
- **`dist/` output directory** — flat structure, all build artifacts go here, not committed to the repo, deployed directly to Pages
- **`assets/` directory** — holds the embed script and index.html template, keeps the root clean
- **index.html** serves dual purpose: standalone viewer AND proof that the build works (uses inkgit.js itself)
- **`inkgit.js`** not `embed.js` — branded, so users can identify it in their codebase

## Development Commands

```bash
# Install dependencies
pip install markdown-it-py minify-html rjsmin

# Build all markdown files
python build.py

# Build from a custom directory / custom output
python build.py --data-dir my-folder --output-dir my-output

# Test locally — just open dist/index.html in a browser
```

## What to Improve / TODO

- [ ] Add a `.gitignore`
- [ ] Consider adding `--watch` mode for local development
- [ ] Consider CORS headers documentation (GitHub Pages handles this, but worth noting)
- [ ] Could add optional frontmatter support (title, tags, date) for richer index.html
- [ ] Could add RSS feed generation from the markdown files
- [ ] The inkgit.js could support a `data-inkgit-loading` attribute for custom loading states
- [ ] Consider adding cache-busting (query param with commit SHA or timestamp)
- [ ] Add a demo/preview GH Pages site in the README
- [ ] Update LICENSE copyright holder name before publishing

## Code Style

- Python: standard library + markdown-it-py + minify-html + rjsmin only, no unnecessary dependencies
- JavaScript: vanilla ES5-compatible, no dependencies, no build step (IIFE pattern, `fetch` API)
- Keep everything minimal — this is a micro-project, not a framework
