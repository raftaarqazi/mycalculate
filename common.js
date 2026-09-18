// ===== common.js — Global logic for all pages =====
(function () {
  'use strict';

  const GA_ID = 'G-T1C2SXJPZK';
  const CONSENT_KEY = 'calqin_cookie_consent';

  function initGA() {
    if (window.__calqinGAReady) return;
    window.__calqinGAReady = true;

    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { anonymize_ip: true });

    const load = () => {
      const s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
      document.head.appendChild(s);
    };
    if ('requestIdleCallback' in window) {
      requestIdleCallback(load, { timeout: 3000 });
    } else {
      window.addEventListener('load', load, { once: true });
    }
  }

  function buildBanner() {
    const div = document.createElement('div');
    div.id = 'cookie-banner';
    div.className = 'cookie-banner';
    div.setAttribute('role', 'dialog');
    div.setAttribute('aria-label', 'Cookie consent');
    div.innerHTML =
      '<div class="cookie-inner">' +
        '<p>We use cookies for analytics and ads to improve your experience. ' +
        'See our <a href="/privacy">Privacy Policy</a>.</p>' +
        '<div class="cookie-btns">' +
          '<button type="button" class="cookie-btn cookie-reject" data-action="reject">Reject</button>' +
          '<button type="button" class="cookie-btn cookie-accept" data-action="accept">Accept</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(div);

    div.addEventListener('click', (e) => {
      const action = e.target.getAttribute('data-action');
      if (!action) return;
      try { localStorage.setItem(CONSENT_KEY, action); } catch (_) {}
      div.classList.remove('show');
      if (action === 'accept') initGA();
    });
  }

  function setupMenu() {
    document.querySelectorAll('.nav-links a').forEach((a) => {
      a.addEventListener('click', () => {
        const nav = document.querySelector('.nav-links');
        if (nav) nav.classList.remove('open');
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    setupMenu();

    let consent = null;
    try { consent = localStorage.getItem(CONSENT_KEY); } catch (_) {}

    if (consent === 'accept') {
      initGA();
    } else if (consent !== 'reject') {
      buildBanner();
      requestAnimationFrame(() => {
        const b = document.getElementById('cookie-banner');
        if (b) b.classList.add('show');
      });
    }
  });
})();