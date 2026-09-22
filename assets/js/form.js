(function () {
  "use strict";

  var FORM_ENDPOINT = "[FORM_ENDPOINT]"; // e.g. https://formspree.io/f/xxxxxxx — see README

  var forms = document.querySelectorAll("#inquiry-form");
  if (!forms.length) return;

  forms.forEach(function (form) {
    var prefix = form.querySelector("[name='name']").id.split("-")[0];
    var summary = document.getElementById(prefix + "-summary");
    var status = document.getElementById(prefix + "-status");
    var submitBtn = document.getElementById(prefix + "-submit");
    var successEl = document.getElementById(prefix + "-success");
    var fallbackEl = document.getElementById(prefix + "-fallback");
    var fallbackLink = document.getElementById(prefix + "-fallback-link");
    var honeypot = form.querySelector("input[name='website']");

    var fieldErrors = {
      name: "Enter your name.",
      phone: "Enter a phone or WhatsApp number.",
      business_type: "Choose the type of business.",
      service: "Choose the service you need.",
      message: "Tell us a little about the problem, at least a sentence or two.",
    };

    function setError(field, message) {
      var wrapper = field.closest(".field");
      var errorEl = document.getElementById(field.id + "-error");
      if (!wrapper || !errorEl) return;
      if (message) {
        wrapper.classList.add("has-error");
        errorEl.textContent = message;
        errorEl.hidden = false;
        field.setAttribute("aria-invalid", "true");
      } else {
        wrapper.classList.remove("has-error");
        errorEl.hidden = true;
        field.removeAttribute("aria-invalid");
      }
    }

    function validate() {
      var firstInvalid = null;
      var valid = true;
      Object.keys(fieldErrors).forEach(function (name) {
        var field = form.querySelector("[name='" + name + "']");
        if (!field) return;
        var value = field.value.trim();
        var bad = name === "message" ? value.length < 20 : value === "";
        setError(field, bad ? fieldErrors[name] : "");
        if (bad) {
          valid = false;
          if (!firstInvalid) firstInvalid = field;
        }
      });
      var email = form.querySelector("[name='email']");
      if (email && email.value.trim() && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
        setError(email, "Enter a valid email address, or leave it blank.");
        valid = false;
        if (!firstInvalid) firstInvalid = email;
      } else if (email) {
        setError(email, "");
      }
      return { valid: valid, firstInvalid: firstInvalid };
    }

    form.querySelectorAll("input, select, textarea").forEach(function (field) {
      field.addEventListener("blur", function () {
        if (field.name in fieldErrors || field.name === "email") validate();
      });
    });

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (summary) summary.hidden = true;

      if (honeypot && honeypot.value) {
        // Likely a bot. Pretend success without sending anything further.
        showSuccess();
        return;
      }

      var result = validate();
      if (!result.valid) {
        if (summary) {
          summary.textContent = "Please check the highlighted fields and try again.";
          summary.hidden = false;
        }
        if (result.firstInvalid) result.firstInvalid.focus();
        return;
      }

      if (!FORM_ENDPOINT || FORM_ENDPOINT.indexOf("[") === 0) {
        showFallback();
        return;
      }

      var formData = new FormData(form);
      submitBtn.disabled = true;
      var originalLabel = submitBtn.querySelector(".btn__label").textContent;
      submitBtn.querySelector(".btn__label").textContent = "Sending\u2026";
      if (status) status.textContent = "Sending your message.";

      fetch(FORM_ENDPOINT, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: formData,
      })
        .then(function (response) {
          if (response.ok) {
            showSuccess();
          } else {
            throw new Error("submission failed");
          }
        })
        .catch(function () {
          submitBtn.disabled = false;
          submitBtn.querySelector(".btn__label").textContent = originalLabel;
          if (summary) {
            summary.textContent = "The message could not be sent. Please try again, or use WhatsApp, phone or email below.";
            summary.hidden = false;
          }
          if (status) status.textContent = "The message could not be sent.";
        });
    });

    function showSuccess() {
      form.hidden = true;
      if (successEl) {
        successEl.hidden = false;
        successEl.focus();
      }
      if (status) status.textContent = "Your message has been sent.";
    }

    function showFallback() {
      form.hidden = true;
      if (fallbackEl) {
        fallbackEl.hidden = false;
        fallbackEl.focus();
      }
      if (fallbackLink) {
        var name = (form.querySelector("[name='name']").value || "").trim();
        var service = (form.querySelector("[name='service']").value || "").trim();
        var message = (form.querySelector("[name='message']").value || "").trim();
        var text = "Hello, my name is " + name + ". I am interested in " + (service || "software") + " for my business. " + message;
        fallbackLink.href = "https://wa.me/[WHATSAPP_NUMBER]?text=" + encodeURIComponent(text.trim());
      }
    }
  });
})();
