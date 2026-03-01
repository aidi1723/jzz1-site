(function () {
  'use strict';

  function normalize(path) {
    if (!path) return '/';
    path = path.split('#')[0].split('?')[0];
    if (!path.startsWith('/')) path = '/' + path;
    if (path.length > 1 && path.endsWith('/')) path = path.slice(0, -1);
    return path;
  }

  function init() {
    var current = normalize(window.location.pathname);
    var links = document.querySelectorAll('nav a[href]');
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      var href = normalize(a.getAttribute('href'));
      if (href === current) {
        a.classList.add('nav-active');
        a.setAttribute('aria-current', 'page');
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
