/**
 * Inkgit🫟 — embed script
 *
 * Drop this into your site to fetch and display your Inkgit🫟 pages.
 *
 * Usage:
 *   <div data-inkgit="https://yourname.github.io/your-repo/til.html"></div>
 *   <script async src="https://yourname.github.io/your-repo/inkgit.min.js"></script>
 *
 * Options (via data attributes):
 *   data-inkgit       — URL of the built HTML file (required)
 *   data-inkgit-class — CSS class to add to the container (optional)
 */
(function () {
  function init() {
    document.querySelectorAll("[data-inkgit]").forEach(function (el) {
      var url = el.getAttribute("data-inkgit");
      var cls = el.getAttribute("data-inkgit-class");
      if (!url) return;

      if (cls) el.classList.add(cls);
      el.textContent = "Loading…";

      fetch(url)
        .then(function (r) {
          if (!r.ok) throw new Error(r.status);
          return r.text();
        })
        .then(function (html) {
          el.innerHTML = html;
        })
        .catch(function () {
          el.textContent = "Failed to load content.";
        });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
