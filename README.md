# Inkgit🫟 - quick HTML content for your site

Inkgit🫟 is a simple tool to serve frequently changing content from a Git repo and show it on your website without requiring to go through CMS updates or build pipelines.

## Example use cases

 * **Showing frequently updated section on your website**: For example, a TIL, reading list, project updates, or a changelog — that you want to maintain separately from your main content because you don't want to rebuild your entire site for every small update.

 * **Showing updates from AI agents:** For example, an AI agent collecting daily market data and showing it on your site without giving it access to your website CMS.


## How it works

1. You update the markdown files in the `data/` folder (eg. `data/til.md`)
2. A GitHub Action converts them to minified HTML and outputs to `dist/`
3. GitHub Pages serves the `dist/` directory
4. Your site fetches and displays them with a one-line embed.

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

Take a look at the index page for this repo: https://vishnuharidas.github.io/inkgit/index.html

## Styling

View the raw HTML generated from the markdown files in `/data` directory:
 - [sample.til.html](https://vishnuharidas.github.io/inkgit/sample.til.html)
 - [sample.books.html](https://vishnuharidas.github.io/inkgit/sample.books.html)
 - [sample.hydroponics_updates.html](https://vishnuharidas.github.io/inkgit/sample.hydroponics_updates.html)

The generated HTML is unstyled — it inherits your site's CSS when the content is displayed on your website. The generated HTML uses standard tags (`<h1>`, `<ul>`, `<li>`, `<code>`, `<pre>`, `<strong>`, etc.), so your existing styles will apply.

You can also add a class to the container:

```html
<div data-inkgit="..." data-inkgit-class="til-section"></div>
```

## Markdown format

Use any standard markdown. A simple list format works well for TIL-style entries:

```markdown
- **2026-03-06** — Honey never spoils. Archaeologists have found 3,000-year-old honey in Egyptian tombs that was still perfectly edible.

- **2026-03-05** — Sharks are older than trees. Sharks have been around for about 400 million years; trees appeared roughly 350 million years ago.
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

## Why I built this

I keep running into interesting things every day — a handy CLI flag, a language quirk, a debugging trick — and I wanted to share a TIL list on my [personal blog](https://iamvishnu.com). But rebuilding my entire website for a one-line TIL entry felt like overkill. I didn't want to open my blog content, edit it, trigger a deploy, and wait for a build pipeline every time just to jot down a line of text.

So I built Inkgit🫟. Now I just edit a markdown file — right on GitHub or from my local repo and push, and it shows up on my blog. The website itself doesn't change at all; a tiny script fetches the latest content at load time. The TIL stays separate, lives in its own repo, and updates independently.

### The name "Inkgit🫟"

> **/ˈɪŋk.ɡɪt/** — *ink* as in writing, *git* as in Git.

**Ink** is the oldest form of publishing — putting thoughts on a surface. **Git** is how developers share and version their work. Inkgit🫟 is where the two meet: you write in markdown, Git delivers it to the world. Simple writing, simple delivery.

## License

Copyright (c) 2026 [Vishnu Haridas](https://iamvishnu.com)

This software is published under MIT License. See [LICENSE.txt](LICENSE.txt) for more details
