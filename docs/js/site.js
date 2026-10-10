/* Labib Shami — site behaviour. Vanilla JS, progressive enhancement only.
   Everything on the site works without this file; it adds the mobile menu,
   copy-to-clipboard, click-to-load videos and the chip filters. */
(function () {
  'use strict';

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    var mq = window.matchMedia('(max-width: 860px)');
    var setOpen = function (open, returnFocus) {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
      if (!open && returnFocus) toggle.focus();
    };
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
      if (toggle.getAttribute('aria-expanded') === 'true') {
        var first = nav.querySelector('a');
        if (first) first.focus();
      }
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') setOpen(false, true);
    });
    document.addEventListener('click', function (ev) {
      if (toggle.getAttribute('aria-expanded') === 'true' && !nav.contains(ev.target) && !toggle.contains(ev.target)) setOpen(false);
    });
    nav.addEventListener('click', function (ev) { if (ev.target.closest('a')) setOpen(false); });
    var onChange = function () { if (!mq.matches) setOpen(false); };
    if (mq.addEventListener) mq.addEventListener('change', onChange); else if (mq.addListener) mq.addListener(onChange);
  }

  /* ---------- Polite announcer ---------- */
  var live = document.createElement('div');
  live.className = 'visually-hidden';
  live.setAttribute('role', 'status');
  live.setAttribute('aria-live', 'polite');
  document.body.appendChild(live);
  var announce = function (msg) { live.textContent = ''; window.setTimeout(function () { live.textContent = msg; }, 60); };
  window.LS_announce = announce;

  /* ---------- Copy to clipboard ---------- */
  document.addEventListener('click', function (ev) {
    var btn = ev.target.closest('[data-copy-target]');
    if (!btn) return;
    var target = document.getElementById(btn.getAttribute('data-copy-target'));
    if (!target) return;
    var text = target.textContent.trim();
    var done = function () {
      btn.setAttribute('data-copied', 'true');
      announce('Copied to clipboard');
      window.setTimeout(function () { btn.removeAttribute('data-copied'); }, 2000);
    };
    var fallback = function () {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      if (ok) { done(); } else {
        var range = document.createRange(); range.selectNodeContents(target);
        var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range);
        announce('Text selected. Press Control+C or Command+C to copy.');
      }
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, fallback);
    } else { fallback(); }
  });

  /* ---------- Click-to-load YouTube (privacy-friendly facade) ---------- */
  document.addEventListener('click', function (ev) {
    var btn = ev.target.closest('[data-youtube]');
    if (!btn) return;
    var id = btn.getAttribute('data-youtube');
    if (!/^[A-Za-z0-9_-]{6,20}$/.test(id)) return;
    var iframe = document.createElement('iframe');
    iframe.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
    iframe.title = btn.getAttribute('data-title') || 'Video';
    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
    iframe.setAttribute('allowfullscreen', '');
    iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    btn.parentNode.replaceChild(iframe, btn);
    iframe.focus();
  });

  /* ---------- Chip filters (policy, media) ---------- */
  Array.prototype.forEach.call(document.querySelectorAll('[data-filter-controls]'), function (group) {
    var scope = document.getElementById(group.getAttribute('data-filter-controls'));
    if (!scope) return;
    group.hidden = false;
    var chips = group.querySelectorAll('[data-filter]');
    var apply = function (value, silent) {
      Array.prototype.forEach.call(chips, function (c) { c.setAttribute('aria-pressed', String(c.getAttribute('data-filter') === value)); });
      var shown = 0;
      Array.prototype.forEach.call(scope.querySelectorAll('[data-filter-item]'), function (it) {
        var tags = (it.getAttribute('data-tags') || '').split(/\s+/);
        var on = value === 'all' || tags.indexOf(value) !== -1;
        it.hidden = !on;
        if (on) shown++;
      });
      Array.prototype.forEach.call(scope.querySelectorAll('[data-filter-section]'), function (sec) {
        sec.hidden = !sec.querySelector('[data-filter-item]:not([hidden])');
      });
      if (!silent) announce(shown + (shown === 1 ? ' item' : ' items') + ' shown');
    };
    Array.prototype.forEach.call(chips, function (c) {
      c.addEventListener('click', function () { apply(c.getAttribute('data-filter')); });
    });
    var initial = new URLSearchParams(window.location.search).get(group.getAttribute('data-filter-param') || 'filter');
    var valid = Array.prototype.some.call(chips, function (c) { return c.getAttribute('data-filter') === initial; });
    apply(valid ? initial : 'all', true);
  });
})();
