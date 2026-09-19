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
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav-links');

    if (toggle && nav) {
      // Remove old inline onclick if present (from un-updated pages)
      toggle.removeAttribute('onclick');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.addEventListener('click', () => {
        const isOpen = nav.classList.toggle('open');
        toggle.setAttribute('aria-expanded', isOpen.toString());
      });
    }

    document.querySelectorAll('.nav-links a').forEach((a) => {
      a.addEventListener('click', () => {
        if (nav) {
          nav.classList.remove('open');
          if (toggle) toggle.setAttribute('aria-expanded', 'false');
        }
      });
    });
  }
  function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    if (!searchInput) return;

    // Create live region for screen readers
    let liveRegion = document.getElementById('search-live');
    if (!liveRegion) {
      liveRegion = document.createElement('div');
      liveRegion.id = 'search-live';
      liveRegion.setAttribute('aria-live', 'polite');
      liveRegion.setAttribute('aria-atomic', 'true');
      liveRegion.style.cssText = 'position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden';
      document.body.appendChild(liveRegion);
    }

    searchInput.addEventListener('input', function (e) {
      const q = e.target.value.toLowerCase().trim();
      let visibleCount = 0;

      document.querySelectorAll('.calc-card').forEach(card => {
        const name = card.dataset.name || '';
        const text = card.textContent.toLowerCase();
        const match = !q || name.includes(q) || text.includes(q);
        card.style.display = match ? '' : 'none';
        if (match) visibleCount++;
      });

      document.querySelectorAll('.calc-category').forEach(cat => {
        const visible = cat.querySelectorAll('.calc-card:not([style*="display: none"])');
        if (visible.length === 0 && cat.querySelector('.calc-grid')) {
          cat.style.display = 'none';
        } else {
          cat.style.display = '';
        }
      });

      liveRegion.textContent = visibleCount === 0
        ? 'No calculators found'
        : visibleCount + ' calculator' + (visibleCount === 1 ? '' : 's') + ' found';
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    setupMenu();
    setupSearch();

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