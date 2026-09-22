# Ian Balijawa — Software Engineer Website

A static client-acquisition website: plain HTML, CSS and vanilla JavaScript,
no build step and no framework. Built to be uploaded to any static host as-is.

## Running locally

No build step is required. From this folder, run any static file server, for example:

```
python3 -m http.server 8080
```

Then open `http://localhost:8080/index.html`. Opening `index.html` directly by
double-clicking also works for a quick look, but a local server is more accurate
(the contact form's `fetch` call and a couple of relative-path checks behave
better served over HTTP than over `file://`).

## Deploying

Upload the contents of this folder as-is to any static host: Netlify, Vercel,
Cloudflare Pages, GitHub Pages, or a plain web server. There is nothing to build.

- Netlify / Vercel: drag-and-drop the folder, or connect the repository and set
  the publish directory to this folder with no build command.
- Traditional hosting (cPanel, etc.): upload everything to the web root
  (usually `public_html`).

## Before you launch: placeholders to replace

Search the project for square-bracket placeholders and replace every one.
Nothing was invented — these are intentionally left for you to fill in.

| Placeholder | Where it appears | Replace with |
|---|---|---|
| `[WHATSAPP_NUMBER]` | Every page (header, footer, hero, contact, service CTAs) and `assets/js/main.js` (`CONTACT.whatsapp`) | Your WhatsApp number, digits only with country code, e.g. `256700000000` |
| `[PHONE_NUMBER]` | Footer, contact page, `assets/js/main.js` (`CONTACT.phone`), JSON-LD in `common.py`-generated pages | Your phone number |
| `[EMAIL_ADDRESS]` | Footer, contact page, privacy policy, `assets/js/main.js` (`CONTACT.email`) | Your email address |
| `[DOMAIN]` | `robots.txt`, `sitemap.xml`, every page's canonical/Open Graph tags | Your live domain, e.g. `ianbalijawa.com` |
| `[LINKEDIN_URL]` | Footer, JSON-LD `sameAs` | Your LinkedIn profile URL |
| `[INSTAGRAM_URL]`, `[FACEBOOK_URL]` | Footer | Your social profile URLs, or delete the links if you don't use them |
| `[FORM_ENDPOINT]` | `assets/js/form.js` (top of file) | Your form provider's endpoint — see below |
| `[SCREENSHOT_1]` … `[SCREENSHOT_3]` and `[SCREENSHOT_*_MOBILE]` | `work.html`, and the work preview on `index.html` | Real, approved screenshots of finished projects — see "Adding real project screenshots" |
| `[CLIENT_NAME]`, `[BUSINESS_NAME]`, `[POSITION]`, `[AUTHENTIC_TESTIMONIAL]`, `[CLIENT_PHOTO]` | Testimonials section on `index.html` | Real testimonials, once you have them to publish. No testimonials were invented — delete the section entirely if you don't have any yet |
| `[PORTRAIT_PHOTO]` | About teaser on `index.html` | A real photo of you |

None of these were faked with placeholder-sounding real data. Until you fill
them in, the site is honest about being unfinished rather than showing invented
numbers or names.

## Where the contact form sends messages

The form at `#contact-form` posts to whatever URL you put in `FORM_ENDPOINT`
at the top of `assets/js/form.js`. Any of the following work without a
custom backend:

- **Formspree** (https://formspree.io) — create a form, get an endpoint like
  `https://formspree.io/f/xxxxxxxx`, paste it in.
- **Web3Forms** (https://web3forms.com) — free, no signup email verification loop.
- **Netlify Forms** — if hosting on Netlify, add a `data-netlify="true"` attribute
  to the `<form>` in each page and follow Netlify's static-form docs instead of
  using `FORM_ENDPOINT`.
- **A serverless function you control** — point `FORM_ENDPOINT` at it; it should
  accept a `POST` with form-encoded or multipart data and respond `200 OK`.

Until `FORM_ENDPOINT` is set, the form still validates input correctly but
shows a "the form is not connected yet" message with a WhatsApp fallback
instead of silently failing — so it's safe to launch before the form is wired up.

The form also has a honeypot field (`name="website"`, visually hidden) for
basic spam protection. No CAPTCHA is included; add one at your form
provider if spam becomes a problem.

## Adding real project screenshots

1. Export a screenshot (browser mockup shots work well — crop to just the
   interface, no visible client data).
2. Save it under `assets/images/` as a `.webp` (smaller) or `.jpg`, e.g.
   `assets/images/project-1.webp`.
3. In `work.html` (and the matching preview block in `index.html`), replace the
   placeholder `.frame__screen` markup for that project with an `<img>` tag:
   ```html
   <img src="assets/images/project-1.webp" alt="Describe what the screenshot shows" loading="lazy" width="960" height="600">
   ```
   Keep the outer `.frame` / `.frame--browser` wrapper for the consistent
   browser-chrome styling.
4. For confidential government/institutional work, only use screenshots you
   have explicit permission to publish, with no real names, IDs, or private
   data visible. Blur or crop anything sensitive first.

## Adding real testimonials

Edit the `<figure class="quote">` blocks in the testimonials section of
`index.html` (search for "What clients say"). Replace the placeholder text
with a real quote, name, role and business. If you don't have any yet,
delete the whole `<section class="section testimonials">` block rather than
leave the placeholders live.

## Updating SEO metadata

Titles, meta descriptions, Open Graph tags and JSON-LD structured data are
generated per page from `/build/common.py` and `/build/build.py` if you're
regenerating the site, or can be hand-edited directly in each `.html` file's
`<head>`. If you edit HTML directly rather than regenerating, keep the
`<title>`, `meta[name="description"]`, and the matching Open Graph/Twitter
tags in sync.

## Regenerating the site from source (optional)

The `/build` folder (not part of the deployed site — you can delete it, or
keep it privately for future edits) contains the Python scripts used to
generate every HTML page consistently:

- `common.py` — shared header, footer, contact form, SEO/JSON-LD helpers
- `pages_home.py` — homepage content and service/case-study data
- `pages_more.py` — about, services, work, contact, privacy, terms, 404
- `build.py` — runs the above and writes the final HTML into this folder

To regenerate after editing the Python source:

```
cd build
python3 build.py
```

This is optional. You can also just hand-edit the generated `.html` files
directly — they are plain, readable HTML with no templating markers left in.

## Project structure

```
index.html            Home
about.html
services.html
work.html
contact.html
privacy.html
terms.html
404.html

assets/
  css/styles.css       Design system and component styles
  css/responsive.css   Mobile/tablet breakpoints
  js/main.js           Header, mobile nav, contact-detail fill-in, WhatsApp float
  js/animations.js     Scroll-reveal via IntersectionObserver, respects reduced motion
  js/form.js           Contact form validation and submission
  fonts/               Self-hosted variable fonts (Bricolage Grotesque, Instrument Sans)
  images/              og-image.jpg and, once added, project screenshots
  icons/               favicon.svg, apple-touch-icon.png, icon-192.png, icon-512.png

robots.txt
sitemap.xml
site.webmanifest
favicon.ico
```

## Security notes for your hosting provider

This is a static site, so most server-side attack surface doesn't apply. Still
worth doing at the hosting level:

- Serve over HTTPS only (redirect HTTP to HTTPS).
- Set standard security headers if your host supports it:
  `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
  `Referrer-Policy: strict-origin-when-cross-origin`.
- A Content-Security-Policy is optional but the site is compatible with a
  strict one: no inline event handlers, and the only inline `<script>` is a
  single one-line class toggle in `<head>` on every page.

## Accessibility and performance

Built to a quality floor, not just to a Lighthouse number: semantic HTML5
landmarks, a skip-to-content link, visible keyboard focus states, labelled
form fields with inline error messages, `prefers-reduced-motion` support, and
alt text on every meaningful image. Fonts are self-hosted and preloaded, CSS
and JS are hand-written with no dependencies, and there are no render-blocking
third-party scripts.
