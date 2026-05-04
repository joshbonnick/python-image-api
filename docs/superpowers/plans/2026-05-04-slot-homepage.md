# Slot Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the JSON index route with a designed HTML landing page for Slot, a placeholder image API.

**Architecture:** Django template rendered by the existing `index` view. Single HTML file with inline CSS and vanilla JS. No external dependencies, no build step.

**Tech Stack:** Django 6.0, Django Templates, vanilla HTML/CSS/JS

---

### Task 1: Make template directory discoverable

**Files:**
- Modify: `pythonimageapi/settings.py`

- [ ] **Step 1: Add template directory to DIRS**

The project-level `pythonimageapi/templates/` directory isn't found by Django's `APP_DIRS` loader because `pythonimageapi` is not an `INSTALLED_APP`. Add it to `DIRS`.

```python
# pythonimageapi/settings.py — in TEMPLATES[0], change DIRS from [] to:
'DIRS': [BASE_DIR / 'pythonimageapi/templates'],
```

- [ ] **Step 2: Verify template is found**

Run: `python manage.py check`
Expected: "System check identified no issues (0 silenced)."

- [ ] **Step 3: Commit**

```bash
git add pythonimageapi/settings.py
git commit -m "feat: add project template directory to TEMPLATES DIRS"
```

---

### Task 2: Update index view to render template

**Files:**
- Modify: `pythonimageapi/views.py`

- [ ] **Step 1: Change index view from JsonResponse to template render**

```python
# pythonimageapi/views.py
from django.shortcuts import render
from django.urls import get_resolver, URLPattern, URLResolver


def extract_patterns(patterns, prefix=""):
    routes = []

    for pattern in patterns:
        if isinstance(pattern, URLPattern):
            routes.append(prefix + str(pattern.pattern))
        elif isinstance(pattern, URLResolver):
            routes.extend(
                extract_patterns(
                    pattern.url_patterns,
                    prefix + str(pattern.pattern)
                )
            )

    return routes


def index(request):
    resolver = get_resolver()
    routes = [route for route in extract_patterns(resolver.url_patterns) if 'admin/' not in route]
    return render(request, 'home.html', {'routes': routes})
```

- [ ] **Step 2: Verify the view renders without error**

Run: `python manage.py runserver` and visit `http://localhost:8000/`
Expected: Renders `home.html` (currently empty, so blank page). No 500 error.

- [ ] **Step 3: Commit**

```bash
git add pythonimageapi/views.py
git commit -m "feat: render home.html template from index view"
```

---

### Task 3: Write the homepage template

**Files:**
- Modify: `pythonimageapi/templates/home.html`

- [ ] **Step 1: Write the complete template**

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Slot — Placeholder images via URL parameters</title>
<style>
  :root {
    --bg: oklch(0.98 0.005 200);
    --text: oklch(0.15 0.005 200);
    --text-muted: oklch(0.45 0.005 200);
    --accent: oklch(0.55 0.12 200);
    --accent-subtle: oklch(0.55 0.12 200 / 0.12);
    --code-bg: oklch(0.93 0.008 200);
    --surface: oklch(0.96 0.005 200);
    --border: oklch(0.88 0.005 200);
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; }

  body {
    font-family: system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    max-width: 72ch;
    margin: 0 auto;
    padding: 4rem 1.5rem 6rem;
    -webkit-font-smoothing: antialiased;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: 700;
    letter-spacing: -0.025em;
    line-height: 1.1;
    color: var(--accent);
  }

  .subtitle {
    font-size: 1.0625rem;
    color: var(--text-muted);
    margin-top: 0.5rem;
  }

  h2 {
    font-size: 1.1875rem;
    font-weight: 600;
    letter-spacing: -0.01em;
    margin-bottom: 1.25rem;
  }

  section { margin-top: 5rem; }

  code, .route-pattern, .url-display {
    font-family: "SF Mono", "Cascadia Code", "Fira Code", "JetBrains Mono", ui-monospace, monospace;
    font-size: 0.9375em;
  }

  /* ── Routes ── */

  .route-block { margin-top: 2.5rem; }
  .route-block + .route-block { margin-top: 3rem; }

  .route-pattern {
    display: block;
    background: var(--code-bg);
    padding: 0.875rem 1.125rem;
    border-radius: 6px;
    font-size: 1.0625rem;
    color: var(--text);
    word-break: break-all;
  }

  .route-pattern var {
    font-style: normal;
    color: var(--accent);
    font-weight: 500;
  }

  .route-desc {
    margin-top: 0.75rem;
    color: var(--text);
    max-width: 65ch;
  }

  .params {
    margin-top: 0.75rem;
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 0.375rem 1rem;
  }

  .params dt {
    font-weight: 600;
    font-size: 0.875rem;
    color: var(--text);
    font-family: ui-monospace, monospace;
  }

  .params dd {
    font-size: 0.875rem;
    color: var(--text-muted);
  }

  .params dd code {
    background: var(--code-bg);
    padding: 0.125em 0.375em;
    border-radius: 3px;
    font-size: 0.875em;
  }

  .query-params {
    margin-top: 0.5rem;
    font-size: 0.875rem;
    color: var(--text-muted);
  }

  .route-examples {
    display: flex;
    gap: 0.75rem;
    margin-top: 1rem;
  }

  .route-examples img {
    border-radius: 4px;
    display: block;
    max-width: 100%;
    height: auto;
  }

  /* ── Playground ── */

  .playground { margin-top: 1.5rem; }

  .playground-inputs {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-end;
    gap: 1rem;
  }

  .playground-inputs label {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
    font-size: 0.8125rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .playground-inputs input[type="number"],
  .playground-inputs input[type="text"] {
    font-family: ui-monospace, monospace;
    font-size: 0.9375rem;
    padding: 0.5rem 0.625rem;
    border: 1px solid var(--border);
    border-radius: 5px;
    background: var(--bg);
    color: var(--text);
    width: 7rem;
    transition: border-color 0.15s ease-out;
  }

  .playground-inputs input[type="text"] { width: 8rem; }
  .playground-inputs input#text { width: 10rem; }

  .playground-inputs input:focus {
    outline: none;
    border-color: var(--accent);
  }

  .link-toggle {
    background: none;
    border: 1px solid var(--border);
    border-radius: 5px;
    cursor: pointer;
    padding: 0.5rem 0.625rem;
    font-size: 0.8125rem;
    color: var(--text-muted);
    transition: border-color 0.15s ease-out, color 0.15s ease-out;
    align-self: flex-end;
    margin-bottom: 0;
  }

  .link-toggle:hover { border-color: var(--accent); color: var(--accent); }
  .link-toggle.linked { background: var(--accent-subtle); color: var(--accent); border-color: var(--accent); }

  .url-display {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-top: 1.5rem;
    background: var(--code-bg);
    padding: 0.75rem 1rem;
    border-radius: 6px;
    font-size: 1rem;
    word-break: break-all;
  }

  .url-display code { flex: 1; }

  .copy-btn {
    background: none;
    border: 1px solid var(--border);
    border-radius: 5px;
    cursor: pointer;
    padding: 0.375rem 0.75rem;
    font-size: 0.8125rem;
    font-family: system-ui, sans-serif;
    color: var(--text-muted);
    white-space: nowrap;
    transition: border-color 0.15s ease-out, color 0.15s ease-out;
  }

  .copy-btn:hover { border-color: var(--accent); color: var(--accent); }
  .copy-btn.copied { color: oklch(0.55 0.15 150); border-color: oklch(0.55 0.15 150); }

  .playground-preview {
    margin-top: 1.5rem;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
  }

  .playground-preview img {
    border-radius: 4px;
    max-width: 100%;
    height: auto;
  }

  .color-swatch {
    display: inline-block;
    width: 1em;
    height: 1em;
    border-radius: 3px;
    vertical-align: middle;
    margin-left: 0.25em;
    border: 1px solid var(--border);
  }

  /* ── Footer ── */

  .footer {
    margin-top: 5rem;
    padding-top: 2rem;
    font-size: 0.8125rem;
    color: var(--text-muted);
  }
</style>
</head>
<body>

<header>
  <h1>Slot</h1>
  <p class="subtitle">Placeholder images via URL parameters</p>
</header>

<main>
  <section>
    <h2>Routes</h2>

    <div class="route-block">
      <code class="route-pattern">/svg/<var>size</var>/<var>color</var></code>
      <p class="route-desc">Generate a placeholder image with custom dimensions and background color.</p>
      <dl class="params">
        <dt>size</dt>
        <dd>An integer for a square, or <code>W</code>x<code>H</code> for a rectangle. Default: <code>300</code></dd>
        <dt>color</dt>
        <dd>Hex color without the <code>#</code>. Supports 3 or 6 digit hex, and <code>rgb()</code>. Default: <code>e3e3e3</code></dd>
      </dl>
      <p class="query-params">Query params: <code>text</code> (string), <code>font_size</code> (integer px)</p>
      <div class="route-examples">
        <img src="/svg/120/4488cc" alt="" width="120" height="120" loading="lazy">
        <img src="/svg/180x90/4488cc" alt="" width="180" height="90" loading="lazy">
      </div>
    </div>

    <div class="route-block">
      <code class="route-pattern">/svg/<var>size</var></code>
      <p class="route-desc">Generate an image with custom dimensions using the default background color.</p>
      <dl class="params">
        <dt>size</dt>
        <dd>An integer for a square, or <code>W</code>x<code>H</code> for a rectangle. Default: <code>300</code></dd>
      </dl>
      <div class="route-examples">
        <img src="/svg/120" alt="" width="120" height="120" loading="lazy">
        <img src="/svg/200x80" alt="" width="200" height="80" loading="lazy">
      </div>
    </div>

    <div class="route-block">
      <code class="route-pattern">/svg/</code>
      <p class="route-desc">Generate a default 300&times;300 placeholder with no customization.</p>
      <div class="route-examples">
        <img src="/svg/" alt="" width="150" height="150" loading="lazy">
      </div>
    </div>
  </section>

  <section>
    <h2>Try it</h2>

    <div class="playground">
      <div class="playground-inputs">
        <label>Width
          <input type="number" id="width" value="300" min="1" max="4000">
        </label>
        <button class="link-toggle linked" id="link-toggle" aria-label="Toggle dimension linking">Linked</button>
        <label>Height
          <input type="number" id="height" value="300" min="1" max="4000">
        </label>
        <label>Color
          <input type="text" id="color" value="e3e3e3" maxlength="24" placeholder="e3e3e3">
          <span class="color-swatch" id="color-swatch" style="background:#e3e3e3"></span>
        </label>
        <label>Text
          <input type="text" id="text" placeholder="Optional">
        </label>
      </div>

      <div class="url-display">
        <code id="url-output">/svg/300/e3e3e3</code>
        <button class="copy-btn" id="copy-btn">Copy</button>
      </div>

      <div class="playground-preview">
        <img id="preview" src="/svg/300/e3e3e3" alt="Preview">
      </div>
    </div>
  </section>
</main>

<footer class="footer">
  <p>Slot generates images on the fly. No auth, no rate limits, no storage.</p>
</footer>

<script>
(function() {
  var widthInput = document.getElementById('width');
  var heightInput = document.getElementById('height');
  var colorInput = document.getElementById('color');
  var textInput = document.getElementById('text');
  var linkToggle = document.getElementById('link-toggle');
  var urlOutput = document.getElementById('url-output');
  var preview = document.getElementById('preview');
  var copyBtn = document.getElementById('copy-btn');
  var swatch = document.getElementById('color-swatch');

  var linked = true;

  function sanitizeColor(v) {
    return v.replace(/[^a-zA-Z0-9(),.% ]/g, '').substring(0, 24);
  }

  function buildUrl() {
    var w = parseInt(widthInput.value) || 300;
    var h = parseInt(heightInput.value) || 300;
    var color = sanitizeColor(colorInput.value) || 'e3e3e3';
    var text = textInput.value.trim();

    var size = w === h ? String(w) : w + 'x' + h;
    var path = '/svg/' + size + '/' + color;
    if (text) path += '?text=' + encodeURIComponent(text);
    return path;
  }

  function updatePreview() {
    var path = buildUrl();
    urlOutput.textContent = path;
    preview.src = path;

    var color = sanitizeColor(colorInput.value) || 'e3e3e3';
    swatch.style.background = '#' + color.replace(/^#/, '');
  }

  widthInput.addEventListener('input', function() {
    if (linked) heightInput.value = widthInput.value;
    updatePreview();
  });

  heightInput.addEventListener('input', function() {
    if (linked) widthInput.value = heightInput.value;
    updatePreview();
  });

  colorInput.addEventListener('input', updatePreview);
  textInput.addEventListener('input', updatePreview);

  linkToggle.addEventListener('click', function() {
    linked = !linked;
    if (linked) {
      heightInput.value = widthInput.value;
      linkToggle.textContent = 'Linked';
      linkToggle.classList.add('linked');
    } else {
      linkToggle.textContent = 'Unlinked';
      linkToggle.classList.remove('linked');
    }
    updatePreview();
  });

  copyBtn.addEventListener('click', function() {
    var url = urlOutput.textContent;
    navigator.clipboard.writeText(url).then(function() {
      copyBtn.textContent = 'Copied';
      copyBtn.classList.add('copied');
      setTimeout(function() {
        copyBtn.textContent = 'Copy';
        copyBtn.classList.remove('copied');
      }, 2000);
    });
  });
})();
</script>

</body>
</html>
```

- [ ] **Step 2: Verify the page renders correctly**

Run: `python manage.py runserver` and visit `http://localhost:8000/`
Expected: Full homepage renders with all three sections. Playground is interactive.

- [ ] **Step 3: Commit**

```bash
git add pythonimageapi/templates/home.html
git commit -m "feat: add Slot homepage with route reference and playground"
```
