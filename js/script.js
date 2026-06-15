(function () {
  "use strict";

  // ===== Mobile nav toggle =====
  var toggle = document.querySelector(".nav-toggle");
  var mobileNav = document.getElementById("mobileNav");

  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      mobileNav.hidden = open;
    });

    // Close menu after tapping a link
    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.hidden = true;
      });
    });
  }

  // ===== Scroll reveal =====
  var revealTargets = document.querySelectorAll(
    ".section-head, .card, .room-card, .why-card, .g-item, .price-note, .location-info, .location-map, .faq-item, .closing-inner, .hero-badges li"
  );

  if ("IntersectionObserver" in window) {
    revealTargets.forEach(function (el) {
      el.classList.add("reveal");
    });

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );

    revealTargets.forEach(function (el) {
      observer.observe(el);
    });
  }

  // ===== Header shadow on scroll =====
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 12) {
        header.style.boxShadow = "0 10px 30px rgba(0,0,0,.4)";
      } else {
        header.style.boxShadow = "none";
      }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();
