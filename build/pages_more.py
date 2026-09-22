from common import *
from pages_home import SERVICES, CASES, SECTORS, frame, tags, chips

# ---------------------------------------------------------------- about

def about_body():
    timeline = [
        ("BSc, Computer Science", "Makerere University", "Studied computer science, the foundation for the engineering work that followed."),
        ("Early career", "Fintech and telecom", "Worked on production systems for fintech and telecom organisations, learning how software behaves once real money and real customers depend on it."),
        ("Government and regulatory systems", "Web and mobile", "Took on frontend engineering for institutional and government-related platforms: licensing, revenue and regulatory enforcement systems used by many roles at once."),
        ("Independent practice", "Kampala, Uganda", "Now building websites, mobile apps and business systems directly for Ugandan businesses, bringing the same discipline to a shop's booking system as to a national platform."),
    ]
    timeline_html = "".join(
        f"""<li class="timeline__item"><time>{t}</time><div><h3>{s}</h3><p>{d}</p></div></li>"""
        for t, s, d in timeline
    )

    values = [
        ("Understand before building", "I ask about the business before I open an editor. Software that does not fit the business is expensive, however well it is coded."),
        ("Plain communication", "You should always know what is being built and why, in language that has nothing to do with programming."),
        ("Software that lasts", "I choose technology that a future developer, including a future me, can maintain, not the newest thing available."),
        ("Honesty over selling", "If software is not the answer, or a smaller version would serve you better, I will say so."),
    ]
    values_html = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in values)

    tools = ["JavaScript", "TypeScript", "React", "React Native", "Next.js", "Node.js", "Python", "Java", "C#", "PostgreSQL", "REST APIs", "Git", "Android", "iOS"]
    tools_html = "".join(f"<li>{t}</li>" for t in tools)

    return page_hero(
        "About",
        "I am a software engineer based in Kampala. I spend most of my time turning a business problem into software that people actually want to use.",
    ) + f"""
<section class="section" aria-labelledby="story-title">
  <div class="container">
    <div class="prose">
      <h2 id="story-title" class="h2" style="max-width:none">My background.</h2>
      <p>My name is Ian Balijawa. For more than five years I have worked as a software engineer across fintech, telecom and government-related sectors, building web applications, mobile apps, APIs and the databases behind them.</p>
      <p>Much of that work has involved systems used by many people at once: licensing platforms, revenue reporting tools and regulatory enforcement systems, each with its own set of roles, forms and rules. That kind of work teaches you to build carefully, because a mistake does not stay small.</p>
      <p>I hold a BSc in Computer Science from Makerere University, and my core stack is JavaScript, TypeScript, React, React Native, Next.js and Node.js, alongside Python, Java, C# and PostgreSQL where a project calls for them.</p>
      <p>What I enjoy most is the point where a business problem, described in someone's own words, turns into a system they and their customers actually use. That is the work I do now, for businesses in Kampala and across Uganda.</p>
    </div>
    <ol class="timeline" style="margin-top:clamp(3rem,5vw,4.5rem)">{timeline_html}</ol>
  </div>
</section>

<section class="section section--alt" aria-labelledby="values-title">
  <div class="container">
    <div class="section__head">
      <h2 id="values-title" class="h2">How I work.</h2>
    </div>
    <ul class="value-grid" data-stagger>{values_html}</ul>
  </div>
</section>

<section class="section" aria-labelledby="tools-title">
  <div class="container">
    <div class="section__head">
      <h2 id="tools-title" class="h2">Tools I work with.</h2>
      <p class="lead">Chosen to fit the project and the budget, not the other way round.</p>
    </div>
    <ul class="tools__list" data-stagger style="gap:0.6rem">{tools_html}</ul>
  </div>
</section>
""" + cta_band(
        "Have a business problem worth solving?",
        "Tell me about it. I will reply with questions, a suggested approach, or an honest answer if software is not the right fix.",
    )


# ---------------------------------------------------------------- services

def services_body():
    sections = ""
    for s in SERVICES:
        uses_html = "".join(f"<li>{u}</li>" for u in s["uses"])
        sections += f"""
  <article class="case-full" id="{s['slug']}">
    <div class="container case-full__grid">
      <div>
        {tags([s['name']])}
        <h2 class="h2" style="margin-top:0.8rem">{s['name']}</h2>
        <p class="lead" style="margin-top:0.9rem">{s['short']}</p>
        <div class="case-full__cols">
          <div>
            <h3>Who it is for</h3>
            <p>{s['for']}</p>
          </div>
          <div>
            <h3>The problem it solves</h3>
            <p>{s['solves']}</p>
          </div>
        </div>
        <div style="margin-top:1.8rem">
          <h3 style="color:var(--signal-ink);font-size:0.95rem;font-weight:600;margin-bottom:0.6rem">What this can include</h3>
          <ul class="prose" style="max-width:none">{uses_html}</ul>
        </div>
        <div style="margin-top:1.8rem;display:flex;flex-wrap:wrap;gap:1rem;align-items:center">
          {btn(s['cta_label'], f"contact.html?service={s['param']}#contact-form")}
          {wa_link("Ask on WhatsApp", s['wa'], "btn btn--outline")}
        </div>
      </div>
      <div>{frame(0, False)}</div>
    </div>
  </article>"""

    faqs = [
        ("How much will my project cost?", "It depends on scope. A simple business website costs less than a full management system with several user roles. After discovery I send a written quote in UGX, so you know the number before any work starts."),
        ("How long does a project take?", "A business website can often launch in a few weeks. A management system or mobile app takes longer, usually a small number of months, depending on how much the software needs to do."),
        ("Do I need to know anything technical?", "No. Part of the job is translating between what your business needs and what gets built. You explain the problem in your own words."),
        ("What happens after launch?", "I stay available for fixes, small changes and questions. Larger changes are scoped and quoted the same way the original project was."),
        ("Can you work with my existing website or system?", "Often, yes. Tell me what you already have and I will tell you honestly whether it makes sense to extend it or build something new."),
    ]
    faq_html = "".join(
        f"""<div class="faq__item"><h3><button class="faq__q" aria-expanded="false">{q}{icon('close', 'icon')}</button></h3><div class="faq__a"><p>{a}</p></div></div>"""
        for q, a in faqs
    )

    return page_hero(
        "Services",
        "Six kinds of work, each one aimed at a specific business problem. If your need does not fit neatly into one, tell me about it and we will work out what is needed.",
    ) + f"""
<div class="services-detail">{sections}
</div>
<section class="section section--alt" aria-labelledby="faq-title">
  <div class="container">
    <div class="section__head">
      <h2 id="faq-title" class="h2">Common questions.</h2>
    </div>
    <div class="faq">{faq_html}</div>
  </div>
</section>
""" + cta_band("Not sure which service fits?", "Describe your business and what is slowing it down. I will suggest where to start.")


# ---------------------------------------------------------------- work

def work_body():
    cats = ["all", "government", "web", "mobile"]
    cat_labels = {"all": "All work", "government": "Government & regulatory", "web": "Web applications", "mobile": "Mobile"}
    filter_btns = "".join(
        f'<button type="button" data-filter="{c}" aria-pressed="{"true" if c == "all" else "false"}">{cat_labels[c]}</button>'
        for c in cats
    )

    full_cases = ""
    for c in CASES:
        functions_html = "".join(f"<li>{f}</li>" for f in c["functions"])
        cat = "mobile" if c["duo"] else "government"
        full_cases += f"""
  <article class="case-full" id="{c['slug']}" data-case-category="{cat}">
    <div class="container case-full__grid">
      <div>
        {tags(c['tags'])}
        <h2 class="h2" style="margin-top:0.9rem">{c['title']}</h2>
        <div class="case-full__cols">
          <div><h3>Challenge</h3><p>{c['problem']}</p></div>
          <div><h3>Solution</h3><p>{c['solution']}</p></div>
        </div>
        <div style="margin-top:1.6rem">
          <h3 style="color:var(--signal-ink);font-size:0.95rem;font-weight:600;margin-bottom:0.6rem">Functionality</h3>
          <ul class="prose" style="max-width:none">{functions_html}</ul>
        </div>
        <dl class="case-full__facts">
          <div><dt>Role</dt><dd>{c['role']}</dd></div>
          <div><dt>Technology</dt><dd>{', '.join(c['tech'])}</dd></div>
          <div><dt>Outcome</dt><dd>Confidential client work: measurable outcomes are not published here. Ask directly and I can share what is appropriate.</dd></div>
        </dl>
      </div>
      <div>{frame(c['n'], c['duo'])}</div>
    </div>
  </article>"""

    return page_hero(
        "Our Work",
        "A selection of production systems I have built or contributed to as a frontend engineer. Client and institutional details are described in general terms where confidentiality requires it.",
    ) + f"""
<section class="section" aria-labelledby="work-list-title">
  <div class="container">
    <h2 id="work-list-title" class="visually-hidden">Case studies</h2>
    <div class="work-filter" data-work-filter role="group" aria-label="Filter work by category">{filter_btns}</div>
  </div>
  <div class="case-list-full">{full_cases}
  </div>
</section>
<section class="section section--alt" aria-labelledby="more-work-title">
  <div class="container">
    <div class="section__head">
      <h2 id="more-work-title" class="h2">Have a public project of your own?</h2>
      <p class="lead">Real, approved case studies with screenshots and links go here as projects are completed and clients agree to be featured.</p>
    </div>
    {btn("Start a Project", "contact.html")}
  </div>
</section>
"""


# ---------------------------------------------------------------- contact

def contact_body():
    return page_hero(
        "Contact",
        "Tell me about the problem you are trying to solve. I read every message myself and reply with questions, a suggested approach, or an honest answer if software is not what you need.",
    ) + f"""
<section class="section" aria-labelledby="contact-page-title">
  <div class="container" style="display:grid;grid-template-columns:minmax(0,0.85fr) minmax(0,1.15fr);gap:clamp(2.5rem,5vw,4rem);align-items:start">
    <div>
      <h2 id="contact-page-title" class="visually-hidden">Contact details</h2>
      {direct_options()}
      <div style="margin-top:2rem;padding-top:1.6rem;border-top:1px solid var(--border)">
        <h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin-bottom:0.6rem">Where I work</h3>
        <p style="color:var(--text-soft)">Based in Kampala, Uganda. Working with businesses across the country, in person and remotely.</p>
      </div>
      <div style="margin-top:1.6rem">
        <h3 style="font-family:var(--font-display);font-weight:600;font-size:1rem;margin-bottom:0.6rem">Response time</h3>
        <p style="color:var(--text-soft)">I usually reply within one business day.</p>
      </div>
    </div>
    <div class="form-card" id="contact-form" style="border:1px solid var(--border)">
      {contact_form("f")}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- legal pages

def privacy_body():
    return page_hero("Privacy Policy", "How information submitted through this website is collected, used and kept.") + f"""
<section class="section">
  <div class="container">
    <p class="legal-updated">Last updated {BUILD_DATE}. This is a template policy. Have it reviewed against Uganda's Data Protection and Privacy Act, 2019 before publishing.</p>
    <div class="prose">
      <h2>What this policy covers</h2>
      <p>This policy explains how information is handled when you use this website, including the contact form, and when you contact me by WhatsApp, phone or email.</p>

      <h2>Information collected</h2>
      <p>When you submit the contact form, the following may be collected:</p>
      <ul>
        <li>Full name</li>
        <li>Business name</li>
        <li>Phone or WhatsApp number</li>
        <li>Email address</li>
        <li>Business type and service needed</li>
        <li>Budget range</li>
        <li>The project description you provide</li>
      </ul>
      <p>Basic technical information, such as browser type and pages visited, may also be collected through standard hosting and analytics tools, where enabled.</p>

      <h2>How information is used</h2>
      <p>Information you submit is used only to respond to your enquiry, discuss a potential project and, where you agree to proceed, to deliver that project. It is not sold, and it is not shared with third parties except a form-processing provider used to deliver messages to me, and any tool you separately agree to.</p>

      <h2>How information is stored</h2>
      <p>This is a static website. Submitted messages are delivered through a third-party form provider, configured at [FORM_ENDPOINT]. Once received, messages are kept only as long as needed to respond to your enquiry or deliver an agreed project.</p>

      <h2>Cookies</h2>
      <p>This website does not set marketing or tracking cookies by default. If analytics are added later, this section will be updated to name the tool and what it collects.</p>

      <h2>Your rights</h2>
      <p>You can ask what information is held about you, ask for it to be corrected, or ask for it to be deleted, by contacting [EMAIL_ADDRESS].</p>

      <h2>Contact</h2>
      <p>Questions about this policy can be sent to [EMAIL_ADDRESS] or [PHONE_NUMBER].</p>
    </div>
  </div>
</section>
"""


def terms_body():
    return page_hero("Terms and Conditions", "The terms that apply to enquiries submitted through this website and to project engagements.") + f"""
<section class="section">
  <div class="container">
    <p class="legal-updated">Last updated {BUILD_DATE}. This is a template. Have it reviewed by a qualified professional before publishing, and replace it with a signed contract for any actual project.</p>
    <div class="prose">
      <h2>Use of this website</h2>
      <p>This website is provided to describe services offered by Ian Balijawa and to let visitors make contact. Content is provided in good faith, but no guarantee is made that it is complete, current or free of error.</p>

      <h2>Enquiries and quotes</h2>
      <p>Submitting the contact form does not create a contract. A project begins only once scope, timeline and price have been agreed in writing, separately from this website.</p>

      <h2>Intellectual property</h2>
      <p>The content, design and code of this website belong to Ian Balijawa unless otherwise stated. Project deliverables, including ownership of code and assets, are covered by the individual agreement for that project.</p>

      <h2>Confidentiality</h2>
      <p>Where a case study on this website describes work for a government or institutional client, details are presented in general terms so that no confidential or proprietary information is disclosed.</p>

      <h2>Liability</h2>
      <p>This website is provided as is. To the extent permitted by law, no liability is accepted for losses arising from its use, beyond what is set out in a signed project agreement.</p>

      <h2>Governing law</h2>
      <p>These terms are governed by the laws of the Republic of Uganda.</p>

      <h2>Contact</h2>
      <p>Questions about these terms can be sent to [EMAIL_ADDRESS].</p>
    </div>
  </div>
</section>
"""


def not_found_body():
    return f"""
<section class="section error-page">
  <div class="container">
    <p class="error-page__code" aria-hidden="true">404</p>
    <h1 class="h2" style="margin-top:0.5rem">This page has moved, or never existed.</h1>
    <p class="lead" style="margin-top:1rem">Check the address, or head back to the homepage. If you followed a link to get here, it may be outdated.</p>
    <div class="error-page__actions">
      {btn("Back to homepage", "/index.html")}
      {btn("Contact", "/contact.html", "btn btn--outline")}
    </div>
  </div>
</section>
"""
