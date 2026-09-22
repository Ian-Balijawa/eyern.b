import os
from common import *
from pages_home import home_body
from pages_more import (
    about_body, services_body, work_body, contact_body,
    privacy_body, terms_body, not_found_body,
)

OUT = "/home/claude/site"


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------- index.html

home_schema = [
    PERSON,
    BUSINESS,
    {
        "@type": "WebSite",
        "@id": f"{BASE_URL}/#website",
        "url": f"{BASE_URL}/",
        "name": SITE_NAME,
        "publisher": {"@id": f"{BASE_URL}/#business"},
    },
]
hd = head(
    "Ian Balijawa — Software Engineer in Kampala, Uganda",
    "Websites, mobile apps and custom business systems for businesses in Kampala and across Uganda. Automate operations, serve customers and grow.",
    "",
    home_schema,
)
write("index.html", assemble(hd, home_body(), current="", home=True, main_class="home"))

# ---------------------------------------------------------------- about.html

about_schema = [PERSON, BUSINESS, {"@type": "WebPage", "@id": f"{BASE_URL}/about.html", "name": "About Ian Balijawa", "isPartOf": {"@id": f"{BASE_URL}/#website"}}, breadcrumb("About", "about.html")]
hd = head(
    "About — Ian Balijawa, Software Engineer in Kampala",
    "Ian Balijawa is a software engineer based in Kampala with over five years of experience across fintech, telecom and government sectors.",
    "about.html",
    about_schema,
)
write("about.html", assemble(hd, about_body(), current="about"))

# ---------------------------------------------------------------- services.html

services_schema = [BUSINESS, {"@type": "WebPage", "@id": f"{BASE_URL}/services.html", "name": "Services", "isPartOf": {"@id": f"{BASE_URL}/#website"}}, breadcrumb("Services", "services.html")]
hd = head(
    "Services — Websites, Business Systems & Mobile Apps | Ian Balijawa",
    "Business websites, management systems, mobile apps, custom web applications, booking systems and automation for Ugandan businesses.",
    "services.html",
    services_schema,
)
write("services.html", assemble(hd, services_body(), current="services"))

# ---------------------------------------------------------------- work.html

work_schema = [BUSINESS, {"@type": "WebPage", "@id": f"{BASE_URL}/work.html", "name": "Our Work", "isPartOf": {"@id": f"{BASE_URL}/#website"}}, breadcrumb("Work", "work.html")]
hd = head(
    "Our Work — Case Studies | Ian Balijawa",
    "Case studies from web and mobile engineering work, including government and regulatory platforms, built by Ian Balijawa.",
    "work.html",
    work_schema,
)
write("work.html", assemble(hd, work_body(), current="work"))

# ---------------------------------------------------------------- contact.html

contact_schema = [BUSINESS, {"@type": "ContactPage", "@id": f"{BASE_URL}/contact.html", "name": "Contact", "isPartOf": {"@id": f"{BASE_URL}/#website"}}, breadcrumb("Contact", "contact.html")]
hd = head(
    "Contact — Start a Software Project | Ian Balijawa",
    "Get in touch to discuss a website, mobile app or business system for your company in Kampala or across Uganda. WhatsApp, call, email or use the form.",
    "contact.html",
    contact_schema,
)
write("contact.html", assemble(hd, contact_body(), current="contact"))

# ---------------------------------------------------------------- privacy / terms

hd = head("Privacy Policy | Ian Balijawa", "Privacy policy for ianbalijawa.com covering the contact form and general website use.", "privacy.html", [breadcrumb("Privacy Policy", "privacy.html")], noindex=False)
write("privacy.html", assemble(hd, privacy_body(), current=""))

hd = head("Terms and Conditions | Ian Balijawa", "Terms and conditions for use of this website and its contact form.", "terms.html", [breadcrumb("Terms", "terms.html")], noindex=False)
write("terms.html", assemble(hd, terms_body(), current=""))

# ---------------------------------------------------------------- 404.html

hd = head("Page not found | Ian Balijawa", "This page could not be found. Return to the homepage or get in touch.", "404.html", None, noindex=True)
write("404.html", root_relative(assemble(hd, not_found_body(), current="")))

# ---------------------------------------------------------------- robots.txt / sitemap.xml

write("robots.txt", f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
""")

pages = ["", "about.html", "services.html", "work.html", "contact.html", "privacy.html", "terms.html"]
urls = "\n".join(
    f"""  <url>
    <loc>{BASE_URL}/{p}</loc>
    <lastmod>{BUILD_DATE}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{"1.0" if p == "" else "0.7"}</priority>
  </url>"""
    for p in pages
)
write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
""")

# ---------------------------------------------------------------- site.webmanifest

write("site.webmanifest", """{
  "name": "Ian Balijawa \u2014 Software Engineer",
  "short_name": "Ian Balijawa",
  "start_url": "/index.html",
  "display": "browser",
  "background_color": "#F7F4EE",
  "theme_color": "#1A1E21",
  "icons": [
    { "src": "assets/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "assets/icons/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}
""")

print("Build complete.")
