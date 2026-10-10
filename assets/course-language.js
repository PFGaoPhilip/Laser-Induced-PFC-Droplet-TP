(function () {
  'use strict';
  var root = document.documentElement, key = 'laser-pfc-tp-language', mode = 'en';
  try { mode = localStorage.getItem(key) || mode; } catch (_) {}
  mode = new URLSearchParams(location.search).get('lang') || mode;
  function apply(value) {
    mode = value === 'zh' ? 'zh' : 'en';
    root.dataset.language = mode; root.lang = mode === 'zh' ? 'zh-CN' : 'en';
    try { localStorage.setItem(key, mode); } catch (_) {}
    document.querySelectorAll('[title]').forEach(function (node) {
      var original = node.dataset.languageTitle || node.title;
      if (original.indexOf(' / ') >= 0) { node.dataset.languageTitle = original; node.title = original.split(' / ')[mode === 'en' ? 0 : 1]; }
    });
    var button = document.getElementById('language-toggle');
    if (button) { button.textContent = mode === 'en' ? '中文' : 'English'; button.setAttribute('aria-label', mode === 'en' ? 'Switch to Chinese' : '切换到英文'); }
    document.querySelectorAll('a[href]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href || /^[a-z]+:/i.test(href) || href[0] === '#' || href.indexOf('//') === 0) return;
      var u = new URL(href, location.href);
      if (!/\.html$/i.test(u.pathname)) return;
      u.searchParams.set('lang', mode);
      a.setAttribute('href', href.split('#')[0].split('?')[0] + '?' + u.searchParams.toString() + u.hash);
    });
    document.dispatchEvent(new CustomEvent('course-language-change'));
  }
  var button = document.createElement('button'); button.id = 'language-toggle'; button.type = 'button';
  button.addEventListener('click', function () { apply(mode === 'en' ? 'zh' : 'en'); });
  (document.querySelector('.theme-tools') || document.body).appendChild(button);
  apply(mode);
})();
