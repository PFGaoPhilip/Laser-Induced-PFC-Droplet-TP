(function () {
  'use strict';
  var root = document.documentElement;
  var key = 'laser-pfc-tp-theme';
  var stored = null;
  try { stored = localStorage.getItem(key); } catch (e) { /* File origins may deny storage. */ }
  var query = new URLSearchParams(location.search).get('theme');
  var mode = query === 'light' || query === 'dark' ? query : stored;
  if (mode !== 'light' && mode !== 'dark') mode = 'dark';
  function apply(value) {
    mode = value;
    root.setAttribute('data-theme', mode);
    try { localStorage.setItem(key, mode); } catch (e) { /* Query links carry the choice too. */ }
    var button = document.getElementById('theme-toggle');
    if (button) {
      var zh = root.dataset.language === 'zh';
      button.textContent = zh ? (mode === 'dark' ? '日间模式' : '夜间模式') : (mode === 'dark' ? 'Day mode' : 'Night mode');
      button.setAttribute('aria-pressed', mode === 'light' ? 'true' : 'false');
      button.setAttribute('aria-label', zh ? '切换日间与夜间模式' : 'Switch between day and night modes');
    }
    document.querySelectorAll('a[href]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href || /^[a-z]+:/i.test(href) || href.indexOf('//') === 0 || href[0] === '#') return;
      var u = new URL(href, location.href);
      if (!/\.html$/i.test(u.pathname)) return;
      var hash = href.indexOf('#') < 0 ? '' : href.slice(href.indexOf('#'));
      var path = href.split('#')[0].split('?')[0];
      u.searchParams.set('theme', mode);
      a.setAttribute('href', path + '?' + u.searchParams.toString() + hash);
    });
  }
  apply(mode);
  document.addEventListener('course-language-change', function () { apply(mode); });
  function ready() {
    var bar = document.createElement('div');
    bar.className = 'theme-tools';
    var button = document.createElement('button');
    button.id = 'theme-toggle';
    button.type = 'button';
    button.addEventListener('click', function () { apply(mode === 'dark' ? 'light' : 'dark'); });
    bar.appendChild(button);
    document.body.insertBefore(bar, document.body.firstChild);
    apply(mode);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready);
  else ready();
})();
