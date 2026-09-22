/* =========================================================================
   Ian Balijawa — site interactions & scroll animations
   Handles: fade/mask reveals, number counters, header scroll state,
   mobile nav, hero entrance sequence, and the WhatsApp float.
   Everything respects prefers-reduced-motion.
   ========================================================================= */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------------
   * Fade / mask reveals on scroll into view
   * ---------------------------------------------------------------- */
  var revealTargets = document.querySelectorAll("[data-reveal], [data-stagger]");
  if (revealTargets.length && !reduceMotion && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var el = entry.target;
            if (el.hasAttribute("data-stagger")) {
              Array.prototype.slice.call(el.children).forEach(function (child, i) {
                child.style.transitionDelay = (i * 70) + "ms";
              });
            }
            el.classList.add("is-visible");
            obs.unobserve(el);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -8% 0px" }
    );
    revealTargets.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealTargets.forEach(function (el) {
      el.classList.add("is-visible");
    });
  }

  /* ------------------------------------------------------------------
   * Number counters, e.g. <span data-count="5" data-suffix="+">
   * ---------------------------------------------------------------- */
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length) {
    var animateCount = function (el) {
      if (el.dataset.counted === "true") return;
      el.dataset.counted = "true";

      var target = parseFloat(el.getAttribute("data-count"), 10);
      var suffix = el.getAttribute("data-suffix") || "";
      if (reduceMotion || isNaN(target)) {
        el.textContent = target + suffix;
        return;
      }
      var duration = 900;
      var start = null;
      var step = function (ts) {
        if (start === null) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        var value = Math.round(target * eased * 10) / 10;
        el.textContent = (value % 1 === 0 ? value.toFixed(0) : value.toFixed(1)) + suffix;
        if (progress < 1) window.requestAnimationFrame(step);
      };
      window.requestAnimationFrame(step);
    };

    if ("IntersectionObserver" in window) {
      var countIo = new IntersectionObserver(
        function (entries, obs) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              animateCount(entry.target);
              obs.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.6 }
      );
      counters.forEach(function (el) {
        countIo.observe(el);
      });
    } else {
      counters.forEach(animateCount);
    }
  }

  /* ------------------------------------------------------------------
   * Header: shadow + border once the page has scrolled past the top.
   * ---------------------------------------------------------------- */
  var header = document.getElementById("site-header");
  if (header) {
    var setHeaderState = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    setHeaderState();
    window.addEventListener("scroll", setHeaderState, { passive: true });
  }

  /* ------------------------------------------------------------------
   * Mobile nav toggle.
   * ---------------------------------------------------------------- */
  var menuToggle = document.getElementById("menu-toggle");
  var siteNav = document.getElementById("site-nav");
  if (menuToggle && siteNav) {
    menuToggle.addEventListener("click", function () {
      var isOpen = siteNav.classList.toggle("is-open");
      menuToggle.setAttribute("aria-expanded", String(isOpen));
    });
    siteNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        siteNav.classList.remove("is-open");
        menuToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ------------------------------------------------------------------
   * Year stamp in the footer.
   * ---------------------------------------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ------------------------------------------------------------------
   * Hero entrance sequence. Each [data-hero-el] carries a
   * data-hero-delay (ms) written into --el-delay so the CSS
   * transition-delay picks it up — timing lives in the markup,
   * the actual motion lives in CSS.
   * ---------------------------------------------------------------- */
  var heroEls = document.querySelectorAll("[data-hero-el]");
  if (heroEls.length) {
    heroEls.forEach(function (el) {
      var delay = el.getAttribute("data-hero-delay") || "0";
      el.style.setProperty("--el-delay", delay);
    });

    if (reduceMotion) {
      heroEls.forEach(function (el) { el.classList.add("is-in"); });
    } else {
      // Let the initial (hidden) state paint first, then flip the
      // class so the CSS transitions actually run.
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          heroEls.forEach(function (el) { el.classList.add("is-in"); });
        });
      });
    }
  }

  /* ------------------------------------------------------------------
   * Scroll to the "problem" section from the hero's scroll cue.
   * ---------------------------------------------------------------- */
  var heroScroll = document.getElementById("hero-scroll");
  if (heroScroll) {
    heroScroll.addEventListener("click", function () {
      var target = document.getElementById("problem");
      if (target) {
        target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
      }
    });
  }

  /* ------------------------------------------------------------------
   * WhatsApp float: appears once the hero has scrolled out of view,
   * and can be dismissed for the rest of the session.
   * ---------------------------------------------------------------- */
  var waFloat = document.getElementById("wa-float");
  var waFloatClose = document.getElementById("wa-float-close");
  var hero = document.querySelector(".hero");

  if (waFloat) {
    var dismissed = false;
    try {
      dismissed = sessionStorage.getItem("wa-float-dismissed") === "true";
    } catch (e) { /* storage unavailable — treat as not dismissed */ }

    if (!dismissed) {
      if (hero && "IntersectionObserver" in window) {
        var heroObserver = new IntersectionObserver(
          function (entries) {
            entries.forEach(function (entry) {
              waFloat.hidden = false;
              waFloat.classList.toggle("is-visible", !entry.isIntersecting);
            });
          },
          { threshold: 0 }
        );
        heroObserver.observe(hero);
      } else {
        waFloat.hidden = false;
        waFloat.classList.add("is-visible");
      }
    }

    if (waFloatClose) {
      waFloatClose.addEventListener("click", function () {
        waFloat.classList.remove("is-visible");
        window.setTimeout(function () { waFloat.hidden = true; }, 200);
        try {
          sessionStorage.setItem("wa-float-dismissed", "true");
        } catch (e) { /* ignore */ }
      });
    }
  }
})();
