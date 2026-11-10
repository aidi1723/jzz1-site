(function () {
  'use strict';

  function getUmami() {
    return (window.umami && typeof window.umami.track === 'function') ? window.umami : null;
  }

  function trackEvent(name, data) {
    var u = getUmami();
    if (u) {
      try {
        u.track(name, data);
      } catch (err) {
        // fail-safe, do not disrupt user interaction
      }
    }
  }

  document.addEventListener('click', function (e) {
    var target = e.target;
    if (!target) return;

    var link = target.closest ? target.closest('a') : null;
    var button = target.closest ? target.closest('button') : null;

    if (link) {
      var href = (link.getAttribute('href') || '').trim();
      var text = (link.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 60);

      // 1. WhatsApp Clicks
      if (href.indexOf('wa.me') !== -1 || href.indexOf('whatsapp.com') !== -1) {
        trackEvent('WhatsApp Inquiry', {
          page: window.location.pathname,
          label: text || 'WhatsApp Link'
        });
        return;
      }

      // 2. CAD Simulator Launch (20GP container simulation)
      if (href.indexOf('cargo.agentcoreos.com') !== -1) {
        trackEvent('Launch CAD Simulator', {
          page: window.location.pathname,
          target_url: href
        });
        return;
      }

      // 3. PDF Catalog / Technical Spec Downloads
      if (/\.pdf($|\?)/i.test(href) || href.indexOf('/catalogs/') !== -1 || href.indexOf('/specifications/') !== -1) {
        var filename = href.split('/').pop().split('?')[0];
        trackEvent('Download PDF Catalog', {
          page: window.location.pathname,
          filename: filename
        });
        return;
      }

      // 4. Email Inquiries
      if (href.indexOf('mailto:') === 0) {
        trackEvent('Email Click', {
          page: window.location.pathname,
          email: href.replace(/^mailto:/, '').split('?')[0]
        });
        return;
      }

      // 5. Phone Call Clicks
      if (href.indexOf('tel:') === 0) {
        trackEvent('Phone Call Click', {
          page: window.location.pathname,
          phone: href.replace(/^tel:/, '')
        });
        return;
      }

      // 6. Dock RFQ or Primary Contact CTA Buttons
      if (link.classList.contains('dock-btn-rfq') || (href === '/contact.html' && link.classList.contains('btn'))) {
        trackEvent('Click RFQ CTA', {
          page: window.location.pathname,
          label: text || 'RFQ Button'
        });
        return;
      }
    }

    if (button) {
      var btnId = button.id || '';
      var btnText = (button.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 60);

      // Copy RFQ Summary Button
      if (btnId === 'btn-copy-rfq' || btnText.indexOf('Copy') !== -1) {
        trackEvent('Copy RFQ Summary', {
          page: window.location.pathname,
          button_id: btnId
        });
      }
    }
  }, { passive: true });
})();
