(function () {
  'use strict';

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function $all(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function uniq(arr) {
    return Array.from(new Set(arr.filter(Boolean)));
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }

    // Fallback for older browsers.
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) {}
    document.body.removeChild(ta);
    return Promise.resolve();
  }

  function init() {
    $all('[data-quote-helper="1"]').forEach(function (root) {
      var textarea = $('[data-quote-template]', root);
      if (!textarea) return;

      var selected = [];

      function buildText() {
        var base = textarea.getAttribute('data-quote-template') || textarea.value || '';
        var lines = [];
        if (selected.length) {
          lines.push('Selections: ' + selected.join(' / '));
          lines.push('');
        }
        lines.push(base);
        return lines.join('\n');
      }

      function setStatus(msg) {
        var el = $('[data-quote-status]', root);
        if (!el) return;
        el.textContent = msg;
        window.clearTimeout(el.__t);
        el.__t = window.setTimeout(function () {
          el.textContent = '';
        }, 1600);
      }

      $all('[data-quote-chip]', root).forEach(function (chip) {
        chip.addEventListener('click', function () {
          var val = chip.getAttribute('data-quote-chip') || '';
          if (!val) return;

          var on = chip.getAttribute('aria-pressed') === 'true';
          if (on) {
            chip.setAttribute('aria-pressed', 'false');
            chip.classList.remove('chip--on');
            selected = selected.filter(function (x) { return x !== val; });
          } else {
            chip.setAttribute('aria-pressed', 'true');
            chip.classList.add('chip--on');
            selected = uniq(selected.concat([val]));
          }
        });
      });

      var copyBtn = $('[data-quote-copy]', root);
      if (copyBtn) {
        copyBtn.addEventListener('click', function () {
          copyBtn.disabled = true;
          copyText(buildText())
            .then(function () { setStatus('Copied'); })
            .catch(function () { setStatus('Copy failed'); })
            .finally(function () { copyBtn.disabled = false; });
        });
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
