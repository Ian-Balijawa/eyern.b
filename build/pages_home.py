from common import *

# ---------------------------------------------------------------- shared data

SERVICES = [
    {
        "slug": "business-websites",
        "name": "Business Websites",
        "short": "A professional website that shows customers you are real, tells them what you do and makes it easy to contact you.",
        "for": "Businesses with no website, an outdated one, or a Facebook page doing all the work.",
        "solves": "Customers cannot find you, or cannot tell whether you are a serious business.",
        "uses": [
            "Company website with services, contact details and a map",
            "Enquiry forms that arrive on WhatsApp or email",
            "Catalogues and photo galleries that load quickly on mobile data",
            "Pages written so people searching for your service in your city can find you",
        ],
        "cta": "Need a website?",
        "cta_label": "Start a website project",
        "param": "website",
        "wa": WA_WEBSITE,
    },
    {
        "slug": "business-systems",
        "name": "Business Management Systems",
        "short": "One system for your customers, sales, stock, staff and expenses, built around the way your business actually runs.",
        "for": "Growing SMEs, shops, workshops, distributors and service companies.",
        "solves": "Your information is spread across notebooks, spreadsheets, WhatsApp chats and people's heads.",
        "uses": [
            "Customer records with full history",
            "Sales, receipts and invoices",
            "Stock levels with alerts before items run out",
            "Staff accounts with different levels of access",
            "Expense tracking and monthly reports",
        ],
        "cta": "Need to automate your business?",
        "cta_label": "Start a systems project",
        "param": "system",
        "wa": WA_SYSTEM,
    },
    {
        "slug": "mobile-apps",
        "name": "Mobile Applications",
        "short": "Android and iOS apps built around a real need, for your customers or for the people doing the work in the field.",
        "for": "Businesses with field staff, deliveries or customers who expect to do things from a phone.",
        "solves": "Work happens away from a desk, and paper or phone calls cannot keep up.",
        "uses": [
            "Customer apps for ordering, booking and tracking",
            "Staff apps for inspections, deliveries and site reports",
            "Data collection that copes with weak network coverage",
            "Push notifications, maps and GPS locations",
        ],
        "cta": "Need a mobile application?",
        "cta_label": "Start a mobile project",
        "param": "mobile",
        "wa": WA_MOBILE,
    },
    {
        "slug": "web-apps",
        "name": "Custom Web Applications",
        "short": "Purpose-built portals, dashboards and internal tools for processes that off-the-shelf software does not fit.",
        "for": "Organisations with a specific workflow, such as applications, approvals, licensing or case handling.",
        "solves": "You are forcing your process into someone else's software, or doing it by hand.",
        "uses": [
            "Customer, member or supplier portals",
            "Approval workflows with clear status at each step",
            "Dashboards that turn records into reports",
            "Document upload, review and download",
            "Role-based access so people see only what they should",
        ],
        "cta": "Need a custom web application?",
        "cta_label": "Start a web app project",
        "param": "webapp",
        "wa": WA_SYSTEM,
    },
    {
        "slug": "booking-systems",
        "name": "Booking & Appointment Systems",
        "short": "Let customers book online, and give your staff one calendar that everyone trusts.",
        "for": "Salons, clinics, consultants, trainers, garages and other service providers.",
        "solves": "Time lost to calls and messages, double bookings and customers who forget to come.",
        "uses": [
            "An online booking page with your services and opening hours",
            "Calendars for each staff member",
            "Reminders to reduce missed appointments",
            "Payment options such as mobile money, where they suit the business",
        ],
        "cta": "Need online bookings?",
        "cta_label": "Start a booking project",
        "param": "booking",
        "wa": DEFAULT_WA,
    },
    {
        "slug": "automation",
        "name": "Automation & Integrations",
        "short": "Connect the tools you already use, remove repeated typing and keep your information in one place.",
        "for": "Businesses that use several tools which do not talk to each other.",
        "solves": "The same details are typed in two or three places, and mistakes creep in.",
        "uses": [
            "Website enquiries sent straight to a spreadsheet or your system",
            "Invoices and reports produced automatically",
            "Data shared between systems through their APIs",
            "Alerts when something needs your attention",
        ],
        "cta": "Tired of repeating the same admin?",
        "cta_label": "Start an automation project",
        "param": "custom",
        "wa": DEFAULT_WA,
    },
]

SECTORS = [
    ("Restaurants", "Menus, orders, table bookings and daily sales in one place."),
    ("Salons & Barbershops", "Online booking, client history and appointment reminders."),
    ("Clinics", "Appointments, visit records and simple reports for the owner."),
    ("Schools", "Student records, fee tracking and messages to parents."),
    ("Shops & Retailers", "Stock, sales and supplier records that add up."),
    ("Real Estate", "Property listings, enquiries and a diary of viewings."),
    ("Logistics", "Job tracking, driver updates and delivery records."),
    ("Professional Services", "Client files, project tracking and invoicing."),
    ("Construction", "Site reports, materials and project costs."),
    ("Hospitality", "Reservations, guest enquiries and service requests."),
    ("Travel & Tours", "Package pages, booking enquiries and itineraries."),
    ("Growing SMEs", "One system to replace the five spreadsheets you use today."),
]

CASES = [
    {
        "slug": "enforcement-platform",
        "n": 1,
        "title": "Enforcement and Compliance Platform",
        "tags": ["Regulatory authority", "Web and mobile"],
        "role": "Frontend engineer, web and mobile",
        "problem": "Inspection and enforcement work involved many officers, many roles and a large amount of records. Field teams and office staff needed to work from the same information, and each person needed to see only what their role allowed.",
        "solution": "A web application for office staff and a mobile app for officers in the field, sharing one set of records and one permission model.",
        "functions": [
            "Searchable registers of inspections, premises and enforcement actions",
            "Multi-step forms for reporting and follow-up, with location capture",
            "Enforcement plans with findings and scoring",
            "A permission model covering 40 user roles, with menus that adapt to each role",
            "Document preview and download from the mobile app",
        ],
        "tech": ["React", "TypeScript", "React Native", "Android", "REST APIs"],
        "duo": True,
    },
    {
        "slug": "revenue-inspection-reporting",
        "n": 2,
        "title": "Revenue Inspection and Reporting System",
        "tags": ["Government", "Web application"],
        "role": "Frontend engineer",
        "problem": "Revenue officers had to review records with many layers of related information: inspections, registrations and reports. Reading them in raw form was slow and easy to get wrong.",
        "solution": "A register-based interface that turns deeply nested records into clear tables, tabbed views and detail panels, with a map for location-based work.",
        "functions": [
            "Registers that present complex records as readable tables and tabs",
            "Spot inspection records with a location-aware detail panel and map view",
            "Taxpayer registration reports with nested data shown as proper tables",
            "Consistent date and location handling across reports",
        ],
        "tech": ["React", "TypeScript", "REST APIs", "Mapping"],
        "duo": False,
    },
    {
        "slug": "agricultural-licensing",
        "n": 3,
        "title": "Agricultural Licensing and Royalty Platform",
        "tags": ["Government", "Web application"],
        "role": "Frontend engineer",
        "problem": "Licensing involves several linked steps, from expressions of interest to allocations and royalty declarations. Applicants needed forms that were quick to complete and hard to get wrong.",
        "solution": "Guided forms that look up existing records as the applicant types, fill in related fields automatically and handle repeating entries such as multiple varieties.",
        "functions": [
            "Variety orders, expressions of interest and allocations",
            "Royalty declarations with repeating entries",
            "Live lookups that fill in related details automatically",
            "Validation that catches mistakes before submission",
        ],
        "tech": ["React", "TypeScript", "REST APIs"],
        "duo": False,
    },
]


def frame(n, duo=False):
    browser = f"""<div class="frame frame--browser" data-reveal="mask">
      <div class="frame__bar" aria-hidden="true"><i></i><i></i><i></i></div>
      <div class="frame__screen">
        <p class="frame__label">[SCREENSHOT_{n}]</p>
        <p class="frame__hint">Add an approved screenshot at assets/images/project-{n}.webp</p>
      </div>
    </div>"""
    if not duo:
        return browser
    phone = f"""<div class="frame frame--phone" data-reveal="mask">
      <div class="frame__screen">
        <p class="frame__label">[SCREENSHOT_{n}_MOBILE]</p>
      </div>
    </div>"""
    return f'<div class="frame-duo">{browser}{phone}</div>'


def tags(items):
    return '<ul class="tags">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


def chips(items):
    return '<ul class="chips">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


# ---------------------------------------------------------------- home page

def home_body():
    services_rows = ""
    for s in SERVICES:
        services_rows += f"""
      <article class="service">
        <h3 class="service__title">{s['name']}</h3>
        <p class="service__desc">{s['short']}</p>
        <div class="service__side">
          <p class="service__for"><span class="service__for-label">Good for</span> {s['for']}</p>
          <a class="link" href="services.html#{s['slug']}">More about {s['name'].lower().replace('&amp;', '&')}</a>
        </div>
      </article>"""

    issues = [
        ("Paper records", "Registers, receipts and files that get lost, damaged or cannot be searched."),
        ("Spreadsheet dependency", "One file, one person who understands it, and no record of who changed what."),
        ("Customers scattered across WhatsApp", "Orders and enquiries buried in chats, with no single record of who asked for what."),
        ("Manual bookings", "Calls and messages to agree on a time, and double bookings on busy days."),
        ("Guesswork on stock", "You find out something has run out when a customer asks for it."),
        ("Reports that take days", "Month-end means hours of adding things up, and the totals still get argued about."),
        ("Repeated admin", "The same details typed into three places, every day, by someone with better things to do."),
        ("No professional online presence", "Customers search for you, find nothing or an old page, and call someone else."),
    ]
    issues_html = "".join(f'<li class="issue"><h3>{t}</h3><p>{d}</p></li>' for t, d in issues)

    sectors_html = "".join(
        f'<li class="sector"><h3>{n}</h3><p>{d}</p></li>' for n, d in SECTORS
    )

    cases_html = ""
    for i, c in enumerate(CASES):
        flip = " case--flip" if i % 2 else ""
        cases_html += f"""
      <article class="case{flip}" id="{c['slug']}-preview">
        <div class="case__media">{frame(c['n'], c['duo'])}</div>
        <div class="case__body">
          {tags(c['tags'])}
          <h3 class="case__title">{c['title']}</h3>
          <p class="case__label">The problem</p>
          <p>{c['problem']}</p>
          <p class="case__label">What I built</p>
          <p>{c['solution']}</p>
          <p class="case__role"><span>Role</span> {c['role']}</p>
          {chips(c['tech'])}
          <a class="link" href="work.html#{c['slug']}">Read the case study</a>
        </div>
      </article>"""

    why = [
        ("Engineering experience", "I have built and maintained software that organisations rely on every day. That means I know what breaks, and how to prevent it."),
        ("Business first", "I start with how your business works and what slows it down. The technology comes after, and it is chosen to fit your budget."),
        ("Web, mobile and backend", "One engineer across the whole stack means fewer hand-offs, fewer misunderstandings and one person accountable for how it all fits together."),
        ("Built to last and to grow", "A clear structure and sensible technology choices mean the system can change as your business does."),
        ("Plain communication", "You get updates in normal language. You always know what is being built, why, and what happens next."),
        ("Support after launch", "Software needs care once it is live. I stay available for fixes, changes and questions."),
    ]
    why_html = "".join(f'<li class="why__item"><h3>{t}</h3><p>{d}</p></li>' for t, d in why)

    steps = [
        ("Discovery", "We talk through your business, your customers and the problem to solve. I ask a lot of questions.", "A clear summary of the problem and the goal."),
        ("Planning", "We agree what the system needs to do, who will use it and how the work will be organised.", "A written scope, a timeline and a quote in UGX."),
        ("Design", "I design the screens and the structure behind them. You review before anything is built.", "Screens you can react to and a plan for your data."),
        ("Development", "I build in stages and test as I go, so you can see real progress along the way.", "Working software to try, not only status updates."),
        ("Launch", "The system goes live, your data is moved across and your team is shown how to use it.", "A live system, training and handover notes."),
        ("Support", "After launch I keep things healthy and make the changes you need as the business grows.", "Fixes, updates and a person to call."),
    ]
    steps_html = "".join(
        f"""<li class="step"><span class="step__num" aria-hidden="true">{i:02d}</span>
          <h3>{t}</h3><p>{d}</p><p class="step__out"><span>You get</span> {o}</p></li>"""
        for i, (t, d, o) in enumerate(steps, 1)
    )

    quote = """<figure class="quote is-placeholder">
        <blockquote><p>[AUTHENTIC_TESTIMONIAL]</p></blockquote>
        <figcaption>
          <span class="quote__photo" aria-hidden="true">[CLIENT_PHOTO]</span>
          <span class="quote__who"><strong>[CLIENT_NAME]</strong><span>[POSITION], [BUSINESS_NAME]</span></span>
        </figcaption>
      </figure>"""

    tools = ["JavaScript", "TypeScript", "React", "React Native", "Next.js", "Node.js", "Python", "Java", "C#", "REST APIs", "PostgreSQL", "Git", "Cloud deployment"]
    tools_html = "".join(f"<li>{t}</li>" for t in tools)

    return f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="container hero__grid">
    <div class="hero__copy">
      <p class="hero__who">Ian Balijawa, software engineer</p>
      <h1 id="hero-title" class="hero__title">
        <span class="h-line"><span>Software built</span></span>
        <span class="h-line"><span>around how your</span></span>
        <span class="h-line"><span>business actually works.</span></span>
      </h1>
      <p class="hero__lead">I build websites, mobile apps and custom business systems for companies in Kampala and across Uganda, so your records, bookings and reports stop living in five different places.</p>
      <div class="hero__actions">
        {btn("Start a Project", "contact.html")}
        {wa_link("Chat on WhatsApp", DEFAULT_WA)}
        <a class="link hero__work" href="work.html">View Our Work</a>
      </div>
      <ul class="hero__meta" aria-label="At a glance">
        <li>Kampala, Uganda</li>
        <li>Websites</li>
        <li>Mobile apps</li>
        <li>Business systems</li>
      </ul>
    </div>
    <div class="hero__stage">
      <div class="hero__visual" aria-hidden="true">
        <div class="ledger">
          <div class="ledger__title"></div>
          <div class="ledger__rows"><i></i><i></i><i class="is-struck"></i><i></i><i></i><i></i><i></i><i></i></div>
        </div>
        <div class="app">
          <div class="app__bar"><i></i><i></i><i></i><span>Orders</span></div>
          <div class="app__body">
            <div class="app__side"><span class="is-active">Orders</span><span>Customers</span><span>Stock</span><span>Reports</span></div>
            <div class="app__main">
              <div class="app__row app__row--head"><span>Customer</span><span>Item</span><span>Status</span></div>
              <div class="app__row"><b class="bar bar--a"></b><b class="bar bar--b"></b><em class="pill pill--done">Delivered</em></div>
              <div class="app__row"><b class="bar bar--c"></b><b class="bar bar--a"></b><em class="pill pill--paid">Paid</em></div>
              <div class="app__row"><b class="bar bar--b"></b><b class="bar bar--c"></b><em class="pill pill--wait">Pending</em></div>
              <div class="app__row"><b class="bar bar--a"></b><b class="bar bar--b"></b><em class="pill pill--paid">Paid</em></div>
              <div class="app__row"><b class="bar bar--c"></b><b class="bar bar--a"></b><em class="pill pill--done">Delivered</em></div>
            </div>
          </div>
        </div>
        <div class="phone">
          <p class="phone__title">Book a visit</p>
          <div class="phone__opt is-selected">Haircut</div>
          <div class="phone__opt">Beard trim</div>
          <div class="phone__slots"><span>09:00</span><span class="is-selected">10:30</span><span>12:00</span></div>
          <div class="phone__cta">Confirm</div>
        </div>
      </div>
      <p class="hero__caption">Illustrative interface. Not a client project.</p>
    </div>
  </div>
</section>

<section class="section section--dark trust" aria-labelledby="trust-title">
  <div class="container trust__grid">
    <div class="trust__intro">
      <h2 id="trust-title" class="h2">Proven in production.</h2>
      <p class="trust__text">The care that goes into systems for large organisations goes into every project, from a first website to a full business system.</p>
    </div>
    <dl class="facts" data-stagger>
      <div class="facts__row"><dt>Experience</dt><dd><span data-count="5" data-suffix="+">5+</span> years building production software</dd></div>
      <div class="facts__row"><dt>Platforms</dt><dd>Web, Android and iOS</dd></div>
      <div class="facts__row"><dt>Background</dt><dd>Systems for institutional and government-related organisations</dd></div>
      <div class="facts__row"><dt>Range</dt><dd>Web applications, mobile apps, APIs and business systems</dd></div>
    </dl>
  </div>
</section>

<section class="section problem" id="problem" aria-labelledby="problem-title">
  <div class="container problem__grid">
    <div class="problem__intro">
      <h2 id="problem-title" class="h2">Still running important parts of your business manually?</h2>
      <p class="lead">Most business owners I speak to do not have a technology problem. They have a records problem, a follow-up problem or a visibility problem. Software is what fixes it.</p>
    </div>
    <ul class="issues" data-stagger>{issues_html}</ul>
  </div>
  <div class="container problem__resolve">
    <p class="statement" data-reveal>Software should make the business simpler, not more complicated.</p>
    <div class="problem__resolve-side" data-reveal>
      <p>A good system disappears into the daily routine. Your staff know what to click, you can see what is happening, and customers get answers faster.</p>
      <a class="link" href="contact.html">Talk about your business</a>
    </div>
  </div>
</section>

<section class="section section--alt services" id="services" aria-labelledby="services-title">
  <div class="container">
    <div class="section__head">
      <h2 id="services-title" class="h2">Software for the parts of your business that need it.</h2>
      <p class="lead">Six kinds of work. Each one starts with a business problem, not a technology.</p>
    </div>
    <div class="service-list">{services_rows}
    </div>
    <div class="ctas" data-stagger>
      <a class="ctas__item" href="contact.html?service=website#contact-form"><span class="ctas__q">Need a website?</span><span class="ctas__a">Start here</span></a>
      <a class="ctas__item" href="contact.html?service=system#contact-form"><span class="ctas__q">Need to automate your business?</span><span class="ctas__a">Start here</span></a>
      <a class="ctas__item" href="contact.html?service=mobile#contact-form"><span class="ctas__q">Need a mobile application?</span><span class="ctas__a">Start here</span></a>
    </div>
  </div>
</section>

<section class="section section--dark sectors" id="solutions" aria-labelledby="solutions-title">
  <div class="container">
    <div class="section__head">
      <h2 id="solutions-title" class="h2">Built for businesses like yours.</h2>
      <p class="lead">Find your kind of business below. The details differ, but the goal is the same: less admin, better records and happier customers.</p>
    </div>
    <ul class="sector-grid" data-stagger>{sectors_html}</ul>
    <div class="sectors__cta">
      <div>
        <h3 class="h3">Not sure what software your business needs?</h3>
        <p>Tell me how your business works today. We will work out together what can be improved or automated.</p>
      </div>
      {btn("Discuss My Business", "contact.html")}
    </div>
  </div>
</section>

<section class="section work" id="work" aria-labelledby="work-title">
  <div class="container">
    <div class="section__head">
      <h2 id="work-title" class="h2">Selected work.</h2>
      <p class="lead">Much of my most substantial work is for government and institutional organisations, so it is described in general terms. Ask me and I will explain what I can.</p>
    </div>
    <div class="case-list">{cases_html}
    </div>
    <p class="work__more"><a class="btn btn--outline" href="work.html">View Our Work</a></p>
  </div>
</section>

<section class="section section--alt why" aria-labelledby="why-title">
  <div class="container why__grid">
    <div class="why__intro">
      <h2 id="why-title" class="h2">Why businesses work with me.</h2>
      <p class="lead">You are hiring an engineer who will listen first, build carefully and still be around after launch.</p>
    </div>
    <ul class="why__list" data-stagger>{why_html}</ul>
  </div>
</section>

<section class="section section--dark process" id="process" aria-labelledby="process-title">
  <div class="container">
    <div class="section__head">
      <h2 id="process-title" class="h2">How a project runs.</h2>
      <p class="lead">Six steps, each with something you can see and approve.</p>
    </div>
    <ol class="steps" data-stagger>{steps_html}</ol>
  </div>
</section>

<section class="section testimonials" aria-labelledby="quotes-title">
  <div class="container">
    <div class="section__head">
      <h2 id="quotes-title" class="h2">What clients say.</h2>
    </div>
    <!-- Replace these placeholders with real, approved testimonials. Delete this section if none are available yet. -->
    <div class="quotes" data-stagger>
      {quote}
      {quote}
    </div>
  </div>
</section>

<section class="section section--alt about-teaser" aria-labelledby="about-title">
  <div class="container about-teaser__grid">
    <figure class="portrait" data-reveal="mask">
      <div class="portrait__frame"><p>[PORTRAIT_PHOTO]</p><p class="portrait__hint">assets/images/ian-balijawa.png</p></div>
    </figure>
    <div class="about-teaser__copy">
      <h2 id="about-title" class="h2">The engineer behind the work.</h2>
      <p>I am Ian Balijawa, a software engineer based in Kampala. For more than five years I have built web applications, mobile apps, APIs and databases for organisations in fintech, telecom and government.</p>
      <p>I enjoy the moment a business problem turns into a working system that people actually use. If you can explain how your business runs, I can help you build the software around it.</p>
      <p><a class="link" href="about.html">Read my full profile</a></p>
      <div class="tools">
        <h3 class="tools__title">Tools I work with</h3>
        <ul class="tools__list">{tools_html}</ul>
        <p class="tools__note">I choose tools to fit your budget and your team, not the other way round.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark contact" id="contact" aria-labelledby="contact-title">
  <div class="container contact__grid">
    <div class="contact__intro">
      <h2 id="contact-title" class="h2">Have a business problem that software could solve?</h2>
      <p class="lead">Describe it in your own words. Rough is fine. I will reply with questions, a suggested approach, or an honest answer if software is not what you need.</p>
      {direct_options()}
      <p class="contact__where">Based in Kampala, Uganda. Working with businesses across the country.</p>
    </div>
    <div class="form-card" id="contact-form">
      {contact_form("f")}
    </div>
  </div>
</section>
"""
