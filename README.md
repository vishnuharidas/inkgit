# Inkgit🫟 - quick HTML content for your site

Turn markdown files into embeddable HTML pages, served from GitHub Pages. No build tools on your site, no frameworks, no dependencies at runtime.

**Example use case:** you want to publish a TIL or reading list on your personal site, but you don't want to do that daily from your CMS, or don't want to rebuild your static site for every small update. With Inkgit🫟, you can make updates in a markdown file — directly on GitHub, or local repo and push. A tiny embedded script will load this content on your site seamlessly.

## How it works

1. You update the markdown files in the `data/` folder (eg. `data/til.md`)
2. A GitHub Action converts them to minified HTML and outputs to `dist/`
3. GitHub Pages serves the `dist/` directory
4. Your site fetches and displays them with a one-line embed

## Quick start

### 1. Fork this repo

Click **Fork** on GitHub. Rename it if you like.

### 2. Enable GitHub Pages

Go to **Settings → Pages** and set the source to **GitHub Actions**.

Your files will be available at `https://<username>.github.io/<repo-name>/<filename>.html`.

### 3. Add your content

Edit or add markdown files in the `data/` folder:

```
data/
  sample.til.md                  ← sample TIL entries (delete or rename)
  sample.books.md                ← sample reading list
  sample.hydroponics_updates.md  ← sample project updates
  til.md                         ← add your own files
```

Push to `main`. The GitHub Action will automatically build the `.html` files and an `index.html` for standalone viewing.

### 4. Embed in your site

Add the embed script and a div for each page you want to display:

```html
<!-- The container — one per page -->
<div data-inkgit="https://<username>.github.io/<repo>/til.html"></div>

<!-- The embed script — once, anywhere on the page -->
<script async src="https://<username>.github.io/<repo>/inkgit.min.js"></script>
```

That's it. The script finds all `[data-inkgit]` divs and fetches their content.

### Multiple pages on one site

```html
<h2>TIL</h2>
<div data-inkgit="https://user.github.io/repo/til.html"></div>

<h2>Books</h2>
<div data-inkgit="https://user.github.io/repo/books.html"></div>

<script async src="https://user.github.io/repo/inkgit.min.js"></script>
```

## Standalone viewer

The build also generates `index.html` — a minimal styled page that shows all your markdown files in one place. Visit it directly at:

```
https://<username>.github.io/<repo>/index.html
```

## Styling

The embedded HTML is unstyled — it inherits your site's CSS. The HTML uses standard tags (`<h1>`, `<ul>`, `<li>`, `<code>`, `<pre>`, `<strong>`, etc.), so your existing styles will apply.

You can also add a class to the container:

```html
<div data-inkgit="https://..." data-inkgit-class="til-section"></div>
```

## Markdown format

Use any standard markdown. A simple list format works well for TIL-style entries:

```markdown
- **2026-03-06** — Honey never spoils. Archaeologists have found 3,000-year-old honey
  in Egyptian tombs that was still perfectly edible.

- **2026-03-05** — Sharks are older than trees. Sharks have been around for about
  400 million years; trees appeared roughly 350 million years ago.
```

## Local build

To build locally without waiting for the Action:

```bash
pip install markdown-it-py minify-html rjsmin
python build.py
```

This outputs everything to `dist/`. Open `dist/index.html` in a browser to preview.

## Project structure

```
├── build.py                    # Markdown → HTML converter
├── assets/
│   ├── inkgit.js               # Lightweight embed script for your site
│   └── index.html              # Template for the standalone viewer
├── data/
│   ├── sample.til.md           # Sample files (delete or rename)
│   ├── sample.books.md
│   └── sample.hydroponics_updates.md
├── dist/                       # Build output (auto-generated, not committed)
│   ├── sample.til.html
│   ├── sample.books.html
│   ├── index.html              # Standalone viewer
│   ├── inkgit.js               # Full version (for debugging)
│   └── inkgit.min.js           # Minified (use this)
├── .github/
│   └── workflows/
│       └── build.yml           # GitHub Action
└── README.md
```

### Why I built this

I keep running into interesting things every day — a handy CLI flag, a language quirk, a debugging trick — and I wanted a place to share them quickly. But rebuilding my entire website for a one-line TIL entry felt like overkill. I didn't want to open my blog content, trigger a deploy, and wait for a build pipeline just to jot down something I learned.

So I built Inkgit🫟. Now I just edit a markdown file — right on GitHub or from my local repo — push, and it shows up on my blog. The website itself doesn't change at all; a tiny script fetches the latest content at load time. The TIL stays separate, lives in its own repo, and updates independently.

### The name "Inkgit🫟"

> **/ˈɪŋk.ɡɪt/** — *ink* as in writing, *git* as in Git.

**Ink** is the oldest form of publishing — putting thoughts on a surface. **Git** is how developers share and version their work. Inkgit🫟 is where the two meet: you write in markdown, Git delivers it to the world. Simple writing, simple delivery.

## License

Copyright (c) 2026 Vishnu Haridas

This software is published under MIT License. See [LICENSE.txt](LICENSE.txt) for more details
