"""Shared building blocks for the static site generator.

The generator only exists to keep the eight HTML pages consistent. The output
is plain HTML, CSS and JavaScript and does not depend on this script.
"""
import base64
import hashlib
import json
import re
from urllib.parse import quote

SITE_NAME = "Ian Balijawa"
DOMAIN = "[DOMAIN]"
BASE_URL = f"https://{DOMAIN}"
OG_IMAGE = f"{BASE_URL}/assets/images/og-image.jpg"
BUILD_DATE = "2026-09-21"

INLINE_JS = "document.documentElement.classList.add('js');"
INLINE_JS_HASH = "sha256-" + base64.b64encode(hashlib.sha256(INLINE_JS.encode()).digest()).decode()

DEFAULT_WA = "Hello, I found your website and would like to discuss software for my business."
WA_WEBSITE = "Hello, I found your website and would like to discuss a website for my business."
WA_SYSTEM = "Hello, I found your website and would like to discuss a system to manage my business."
WA_MOBILE = "Hello, I found your website and would like to discuss a mobile app for my business."

ICONS = {
    "whatsapp": '<path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3z"/><path d="M9.2 8.6c0 3.4 2.8 6.2 6.2 6.2l.9-1.5-2-.9-.9.9c-.9-.4-1.8-1.3-2.2-2.2l.9-.9-.9-2-1.5.9z"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "alert": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5v5.5M12 16.5v.01"/>',
}


def icon(name, cls="icon"):
    return (
        f'<svg class="{cls}" viewBox="0 0 24 24" width="24" height="24" fill="none" '
        'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'
    )


def wa_link(label="Chat on WhatsApp", message=DEFAULT_WA, cls="btn btn--outline", show_icon=True):
    href = f"https://wa.me/256787444814?text={quote(message)}"
    ic = icon("whatsapp") if show_icon else ""
    return (
        f'<a class="{cls}" href="{href}" data-contact="whatsapp" data-wa-message="{message}" '
        f'target="_blank" rel="noopener noreferrer">{ic}<span>{label}</span>'
        '<span class="visually-hidden"> (opens WhatsApp in a new tab)</span></a>'
    )


def btn(label, href, cls="btn btn--primary"):
    return f'<a class="{cls}" href="{href}">{label}</a>'


NAV = [
    ("Services", "services.html", "services"),
    ("Solutions", "index.html#solutions", ""),
    ("Work", "work.html", "work"),
    ("About", "about.html", "about"),
    ("Process", "index.html#process", ""),
    ("Contact", "contact.html", "contact"),
]


def breadcrumb(name, path):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": f"{BASE_URL}/{path}"},
        ],
    }


PERSON = {
    "@type": "Person",
    "@id": f"{BASE_URL}/#person",
    "name": SITE_NAME,
    "jobTitle": "Software Engineer",
    "url": f"{BASE_URL}/",
    "email": "ianbalijawa16@gmail.com",
    "telephone": "256787444814",
    "address": {"@type": "PostalAddress", "addressLocality": "Kampala", "addressCountry": "UG"},
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Makerere University"},
    "knowsAbout": [
        "Web application development", "Mobile application development", "React Native",
        "TypeScript", "APIs", "Databases", "Business systems",
    ],
    "sameAs": ["https://www.linkedin.com/in/ian-balijawa-10369a181/"],
}

BUSINESS = {
    "@type": "ProfessionalService",
    "@id": f"{BASE_URL}/#business",
    "name": "Ian Balijawa, Software Engineering",
    "url": f"{BASE_URL}/",
    "image": OG_IMAGE,
    "description": (
        "Websites, mobile applications and custom business systems for businesses "
        "in Kampala and across Uganda."
    ),
    "telephone": "256787444814",
    "email": "ianbalijawa16@gmail.com",
    "address": {"@type": "PostalAddress", "addressLocality": "Kampala", "addressCountry": "UG"},
    "areaServed": [{"@type": "City", "name": "Kampala"}, {"@type": "Country", "name": "Uganda"}],
    "founder": {"@id": f"{BASE_URL}/#person"},
    "knowsAbout": ["Custom software development", "Website development", "Mobile app development"],
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Software services",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}}
            for n in [
                "Business websites", "Business management systems", "Mobile applications",
                "Custom web applications", "Booking and appointment systems",
                "Automation and integrations",
            ]
        ],
    },
}


def head(title, desc, path, schema=None, noindex=False):
    canonical = f"{BASE_URL}/{path}" if path else f"{BASE_URL}/"
    graph = json.dumps({"@context": "https://schema.org", "@graph": schema or []}, indent=2, ensure_ascii=False)
    robots = '<meta name="robots" content="noindex, follow">\n' if noindex else ""
    ld = f'<script type="application/ld+json">\n{graph}\n</script>\n' if schema else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#1A1E21">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:locale" content="en_UG">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Ian Balijawa, software engineer in Kampala, Uganda. Websites, mobile apps and business systems.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG_IMAGE}">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/bricolage-grotesque.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/instrument-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">
<link rel="stylesheet" href="assets/css/responsive.css">
<script>{INLINE_JS}</script>
{ld}</head>
"""


def header(current="", home=False):
    items = []
    for label, href, key in NAV:
        if home and href.startswith("index.html#"):
            href = href.replace("index.html", "")
        cur = ' aria-current="page"' if key and key == current else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    nav_items = "\n          ".join(items)
    brand_href = "#main" if False else "index.html"
    return f"""<body>
<a class="skip-link" href="#main">Skip to main content</a>
<div class="top-sentinel" aria-hidden="true"></div>
<header class="site-header" id="site-header">
  <div class="container header__inner">
    <a class="brand" href="{brand_href}" aria-label="Ian Balijawa, software engineer. Home">
      <span class="brand__mark" aria-hidden="true">IB</span>
      <span class="brand__text">
        <span class="brand__name">Ian Balijawa</span>
        <span class="brand__role">Software Engineer</span>
      </span>
    </a>
    <nav class="site-nav" id="site-nav" aria-label="Primary">
      <ul class="site-nav__list">
          {nav_items}
      </ul>
      <a class="btn btn--primary btn--sm site-nav__cta" href="contact.html">Start a Project</a>
    </nav>
    <div class="header__actions">
      <a class="icon-btn" href="https://wa.me/256787444814?text={quote(DEFAULT_WA)}" data-contact="whatsapp" data-wa-message="{DEFAULT_WA}" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp (opens in a new tab)">{icon("whatsapp")}</a>
      <button class="menu-toggle" type="button" id="menu-toggle" aria-expanded="false" aria-controls="site-nav">
        <span class="menu-toggle__label">Menu</span>
        <span class="menu-toggle__bars" aria-hidden="true"></span>
      </button>
    </div>
  </div>
</header>
"""


def footer():
    return f"""<aside class="wa-float" id="wa-float" hidden>
  {wa_link("Chat on WhatsApp", DEFAULT_WA, "btn btn--primary btn--sm")}
  <button class="wa-float__close" type="button" id="wa-float-close" aria-label="Dismiss WhatsApp prompt">{icon("close")}</button>
</aside>
<footer class="site-footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__about">
        <p class="footer__name">Ian Balijawa</p>
        <p class="footer__desc">Software engineer in Kampala, Uganda. I build websites, mobile apps and custom business systems for businesses across Uganda.</p>
      </div>
      <nav class="footer__col" aria-label="Footer navigation">
        <h2 class="footer__title">Site</h2>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="work.html">Work</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </nav>
      <nav class="footer__col" aria-label="Services">
        <h2 class="footer__title">Services</h2>
        <ul>
          <li><a href="services.html#business-websites">Business websites</a></li>
          <li><a href="services.html#business-systems">Business management systems</a></li>
          <li><a href="services.html#mobile-apps">Mobile applications</a></li>
          <li><a href="services.html#web-apps">Custom web applications</a></li>
          <li><a href="services.html#booking-systems">Booking systems</a></li>
          <li><a href="services.html#automation">Automation and integrations</a></li>
        </ul>
      </nav>
      <div class="footer__col">
        <h2 class="footer__title">Contact</h2>
        <ul>
          <li><a href="https://wa.me/256787444814?text={quote(DEFAULT_WA)}" data-contact="whatsapp" data-wa-message="{DEFAULT_WA}" target="_blank" rel="noopener noreferrer">WhatsApp<span class="visually-hidden"> (opens in a new tab)</span></a></li>
          <li><a href="tel:256787444814" data-contact="phone"><span data-contact-text="phone">256787444814</span></a></li>
          <li><a href="mailto:ianbalijawa16@gmail.com" data-contact="email"><span data-contact-text="email">ianbalijawa16@gmail.com</span></a></li>
          <li><a href="https://www.linkedin.com/in/ian-balijawa-10369a181/" data-social="linkedin" target="_blank" rel="noopener noreferrer">LinkedIn<span class="visually-hidden"> (opens in a new tab)</span></a></li>
          <li><a href="https://www.instagram.com/ianbalijawa/" data-social="instagram" target="_blank" rel="noopener noreferrer">Instagram<span class="visually-hidden"> (opens in a new tab)</span></a></li>
          <li><a href="https://www.facebook.com/ian.balijawa" data-social="facebook" target="_blank" rel="noopener noreferrer">Facebook<span class="visually-hidden"> (opens in a new tab)</span></a></li>
        </ul>
      </div>
    </div>
    <div class="footer__base">
      <p>&copy; <span data-year>2026</span> Ian Balijawa. Kampala, Uganda.</p>
      <ul class="footer__legal">
        <li><a href="privacy.html">Privacy Policy</a></li>
        <li><a href="terms.html">Terms</a></li>
      </ul>
    </div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
<script src="assets/js/animations.js" defer></script>
<script src="assets/js/form.js" defer></script>
</body>
</html>
"""


def field(fid, label, control_html, error_hint=""):
    return (
        f'<div class="field">\n  <label for="{fid}">{label}</label>\n  {control_html}\n'
        f'  <p class="field__error" id="{fid}-error" hidden></p>\n</div>'
    )


def contact_form(prefix="f"):
    business_types = [
        "Restaurant or café", "Salon or barbershop", "Clinic or health service", "School or training centre",
        "Shop or retailer", "Real estate", "Logistics or transport", "Professional services",
        "Construction", "Hotel or hospitality", "Travel and tours", "Other",
    ]
    services = [
        "Business Website", "Business Management System", "Mobile Application", "Web Application",
        "Booking System", "Inventory System", "Custom Software", "Not Sure",
    ]
    budgets = [
        "Under UGX 2,000,000", "UGX 2,000,000 to 5,000,000", "UGX 5,000,000 to 15,000,000",
        "UGX 15,000,000 to 40,000,000", "Above UGX 40,000,000", "Not sure yet",
    ]

    def opts(items):
        return "".join(f'<option value="{i}">{i}</option>' for i in items)

    p = prefix
    parts = [
        field(f"{p}-name", "Full name",
              f'<input id="{p}-name" name="name" type="text" autocomplete="name" required aria-describedby="{p}-name-error">'),
        field(f"{p}-business", 'Business name <span class="optional">(optional)</span>',
              f'<input id="{p}-business" name="business" type="text" autocomplete="organization" aria-describedby="{p}-business-error">'),
        field(f"{p}-phone", "Phone or WhatsApp number",
              f'<input id="{p}-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required aria-describedby="{p}-phone-error">'),
        field(f"{p}-email", 'Email <span class="optional">(optional)</span>',
              f'<input id="{p}-email" name="email" type="email" autocomplete="email" aria-describedby="{p}-email-error">'),
        field(f"{p}-type", "Type of business",
              f'<select id="{p}-type" name="business_type" required aria-describedby="{p}-type-error"><option value="">Choose one</option>{opts(business_types)}</select>'),
        field(f"{p}-service", "Service needed",
              f'<select id="{p}-service" name="service" required aria-describedby="{p}-service-error"><option value="">Choose one</option>{opts(services)}</select>'),
        field(f"{p}-budget", 'Budget range <span class="optional">(optional)</span>',
              f'<select id="{p}-budget" name="budget" aria-describedby="{p}-budget-error"><option value="">Choose one</option>{opts(budgets)}</select>'),
    ]
    grid = "\n".join(f'<div class="form__cell">{x}</div>' for x in parts)
    desc = field(
        f"{p}-message",
        "Tell me about the problem",
        f'<textarea id="{p}-message" name="message" rows="6" minlength="20" required aria-describedby="{p}-message-hint {p}-message-error"></textarea>'
        f'<p class="field__hint" id="{p}-message-hint">What is slowing your business down? Rough notes are fine. A few sentences will do.</p>',
    )
    return f"""<form class="form" id="inquiry-form" novalidate>
  <div class="form__summary" id="{p}-summary" role="alert" tabindex="-1" hidden></div>
  <p class="form__note">All fields are required unless marked optional.</p>
  <div class="form__grid">
{grid}
    <div class="form__cell form__cell--full">{desc}</div>
  </div>
  <div class="form__trap" aria-hidden="true">
    <label for="{p}-website">Leave this field empty</label>
    <input id="{p}-website" name="website" type="text" tabindex="-1" autocomplete="off">
  </div>
  <div class="form__actions">
    <button class="btn btn--primary" type="submit" id="{p}-submit"><span class="btn__label">Send Inquiry</span></button>
    <p class="form__consent">By sending this form you agree that I may contact you about your project. Read the <a href="privacy.html">privacy policy</a>.</p>
  </div>
  <p class="form__status visually-hidden" id="{p}-status" role="status" aria-live="polite"></p>
  <noscript><p class="form__noscript">This form needs JavaScript. Please use WhatsApp, phone or email instead.</p></noscript>
</form>
<div class="form__success" id="{p}-success" role="status" tabindex="-1" hidden>
  <span class="form__success-icon">{icon("check")}</span>
  <h3>Thank you. Your message has been sent.</h3>
  <p>I will read it and reply with questions or a suggested next step. If it is urgent, message me on WhatsApp.</p>
  {wa_link("Chat on WhatsApp", DEFAULT_WA, "btn btn--outline")}
</div>
<div class="form__fallback" id="{p}-fallback" role="alert" tabindex="-1" hidden>
  <h3>The form is not connected yet.</h3>
  <p>Your details were not sent anywhere. You can send the same message on WhatsApp instead.</p>
  <a class="btn btn--primary" id="{p}-fallback-link" href="https://wa.me/256787444814" data-contact="whatsapp" target="_blank" rel="noopener noreferrer">{icon("whatsapp")}<span>Continue on WhatsApp</span><span class="visually-hidden"> (opens in a new tab)</span></a>
</div>"""


def direct_options():
    return f"""<ul class="direct">
  <li>
    <a class="direct__link" href="https://wa.me/256787444814?text={quote(DEFAULT_WA)}" data-contact="whatsapp" data-wa-message="{DEFAULT_WA}" target="_blank" rel="noopener noreferrer">
      {icon("whatsapp")}
      <span class="direct__text"><span class="direct__label">WhatsApp</span><span class="direct__detail" data-contact-text="whatsapp">256787444814</span></span>
      <span class="visually-hidden">(opens in a new tab)</span>
    </a>
  </li>
  <li>
    <a class="direct__link" href="tel:256787444814" data-contact="phone">
      {icon("phone")}
      <span class="direct__text"><span class="direct__label">Call</span><span class="direct__detail" data-contact-text="phone">256787444814</span></span>
    </a>
  </li>
  <li>
    <a class="direct__link" href="mailto:ianbalijawa16@gmail.com" data-contact="email">
      {icon("mail")}
      <span class="direct__text"><span class="direct__label">Email</span><span class="direct__detail" data-contact-text="email">ianbalijawa16@gmail.com</span></span>
    </a>
  </li>
</ul>"""


def cta_band(title, text, primary_label="Start a Project", wa_message=DEFAULT_WA):
    return f"""<section class="section section--dark cta-band" aria-labelledby="cta-title">
  <div class="container cta-band__inner">
    <div>
      <h2 id="cta-title" class="cta-band__title">{title}</h2>
      <p class="cta-band__text">{text}</p>
    </div>
    <div class="cta-band__actions">
      {btn(primary_label, "contact.html")}
      {wa_link("Chat on WhatsApp", wa_message)}
    </div>
  </div>
</section>
"""


def page_hero(title, lead, crumb=None):
    return f"""<section class="page-hero">
  <div class="container">
    <h1 class="page-hero__title">{title}</h1>
    <p class="page-hero__lead">{lead}</p>
  </div>
</section>
"""


def assemble(hd, body, current="", home=False, main_class=""):
    return hd + header(current, home) + f'<main id="main" class="{main_class}" tabindex="-1">\n{body}</main>\n' + footer()


def root_relative(html):
    """Prefix relative URLs with / so the 404 page works at any depth."""
    return re.sub(r'(href|src)="(?!(?:https?:|mailto:|tel:|#|/|\[))', r'\1="/', html)
