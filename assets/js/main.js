(function () {
  "use strict";

  /* ------------------------------------------------------------------
   * Sticky header shadow state
   * ---------------------------------------------------------------- */
  var header = document.getElementById("site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ------------------------------------------------------------------
   * Mobile navigation
   * ---------------------------------------------------------------- */
  var toggle = document.getElementById("menu-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    var closeNav = function () {
      toggle.setAttribute("aria-expanded", "false");
      nav.classList.remove("is-open");
      document.body.style.overflow = "";
    };
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
      document.body.style.overflow = open ? "" : "hidden";
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeNav);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 760) closeNav();
    });
  }

  /* ------------------------------------------------------------------
   * Placeholder contact details
   * Fill these in once real details are available, and every link and
   * label across the site updates from one place.
   * ---------------------------------------------------------------- */
  var CONTACT = {
    whatsapp: null, // e.g. "+256700000000"
    phone: null, // e.g. "+256700000000"
    email: null, // e.g. "hello@example.com"
  };

  function digitsOnly(v) {
    return v.replace(/[^\d+]/g, "");
  }

  if (CONTACT.whatsapp) {
    var waDigits = digitsOnly(CONTACT.whatsapp).replace(/^\+/, "");
    document.querySelectorAll('[data-contact="whatsapp"]').forEach(function (el) {
      var msg = el.getAttribute("data-wa-message") || "";
      el.href = "https://wa.me/" + waDigits + (msg ? "?text=" + encodeURIComponent(msg) : "");
    });
    document.querySelectorAll('[data-contact-text="whatsapp"]').forEach(function (el) {
      el.textContent = CONTACT.whatsapp;
    });
  }
  if (CONTACT.phone) {
    document.querySelectorAll('[data-contact="phone"]').forEach(function (el) {
      el.href = "tel:" + digitsOnly(CONTACT.phone);
    });
    document.querySelectorAll('[data-contact-text="phone"]').forEach(function (el) {
      el.textContent = CONTACT.phone;
    });
  }
  if (CONTACT.email) {
    document.querySelectorAll('[data-contact="email"]').forEach(function (el) {
      el.href = "mailto:" + CONTACT.email;
    });
    document.querySelectorAll('[data-contact-text="email"]').forEach(function (el) {
      el.textContent = CONTACT.email;
    });
  }

  /* ------------------------------------------------------------------
   * Dismissible WhatsApp float
   * Appears after scrolling, stays dismissed for the session once closed.
   * ---------------------------------------------------------------- */
  var waFloat = document.getElementById("wa-float");
  var waClose = document.getElementById("wa-float-close");
  if (waFloat && waClose) {
    var dismissed = false;
    try {
      dismissed = sessionStorage.getItem("wa-float-dismissed") === "1";
    } catch (e) {
      /* storage unavailable, fall through with dismissed = false */
    }
    if (!dismissed) {
      var revealFloat = function () {
        if (window.scrollY > window.innerHeight * 0.6) {
          waFloat.hidden = false;
          window.removeEventListener("scroll", revealFloat);
        }
      };
      window.addEventListener("scroll", revealFloat, { passive: true });
    }
    waClose.addEventListener("click", function () {
      waFloat.hidden = true;
      try {
        sessionStorage.setItem("wa-float-dismissed", "1");
      } catch (e) {
        /* ignore */
      }
    });
  }

  /* ------------------------------------------------------------------
   * Footer year
   * ---------------------------------------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ------------------------------------------------------------------
   * FAQ accordions
   * ---------------------------------------------------------------- */
  document.querySelectorAll(".faq__item").forEach(function (item) {
    var btn = item.querySelector(".faq__q");
    var panel = item.querySelector(".faq__a");
    if (!btn || !panel) return;
    btn.addEventListener("click", function () {
      var open = item.getAttribute("data-open") === "true";
      item.setAttribute("data-open", String(!open));
      btn.setAttribute("aria-expanded", String(!open));
      panel.style.maxHeight = open ? "" : panel.scrollHeight + "px";
    });
  });

  /* ------------------------------------------------------------------
   * Work page category filter
   * ---------------------------------------------------------------- */
  var filterBar = document.querySelector("[data-work-filter]");
  if (filterBar) {
    var buttons = filterBar.querySelectorAll("button");
    var cases = document.querySelectorAll("[data-case-category]");
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        buttons.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true");
        var cat = b.getAttribute("data-filter");
        cases.forEach(function (c) {
          var match = cat === "all" || c.getAttribute("data-case-category") === cat;
          c.hidden = !match;
        });
      });
    });
  }

  /* ------------------------------------------------------------------
   * Pre-select a service on the contact form from a query string,
   * e.g. contact.html?service=mobile
   * ---------------------------------------------------------------- */
  var serviceMap = {
    website: "Business Website",
    system: "Business Management System",
    mobile: "Mobile Application",
    webapp: "Web Application",
    booking: "Booking System",
    custom: "Custom Software",
  };
  var params = new URLSearchParams(window.location.search);
  var svc = params.get("service");
  if (svc && serviceMap[svc]) {
    var select = document.getElementById("f-service");
    if (select) select.value = serviceMap[svc];
  }
})();
