/* Publication explorer for research.html.
   The complete bibliography is plain HTML in the page; this script only filters,
   searches and re-orders the existing entries. No network requests. */
(function () {
  'use strict';
  var root = document.getElementById('bibliography');
  var form = document.getElementById('bib-controls');
  if (!root || !form) return;

  var q = form.querySelector('#bib-q');
  var type = form.querySelector('#bib-type');
  var topic = form.querySelector('#bib-topic');
  var sort = form.querySelector('#bib-sort');
  var reset = form.querySelector('#bib-reset');
  var count = document.getElementById('bib-count');
  var empty = document.getElementById('bib-empty');
  var groups = Array.prototype.slice.call(root.querySelectorAll('[data-year-group]'));
  var entries = Array.prototype.slice.call(root.querySelectorAll('.bib-entry'));
  var total = entries.length;

  form.hidden = false;
  document.getElementById('bib-status').hidden = false;

  var normalise = function (s) {
    s = (s || '').toLowerCase();
    if (s.normalize) s = s.normalize('NFD').replace(/[̀-ͯ]/g, '');
    return s.replace(/[^\w\s-]/g, ' ').replace(/\s+/g, ' ').trim();
  };

  var params = new URLSearchParams(window.location.search);
  if (params.get('q')) q.value = params.get('q');
  ['type', 'topic', 'sort'].forEach(function (k) {
    var el = form.querySelector('#bib-' + k);
    var v = params.get(k);
    if (v && el.querySelector('option[value="' + v.replace(/"/g, '') + '"]')) el.value = v;
  });

  var syncUrl = function () {
    var p = new URLSearchParams();
    if (q.value.trim()) p.set('q', q.value.trim());
    if (type.value !== 'all') p.set('type', type.value);
    if (topic.value !== 'all') p.set('topic', topic.value);
    if (sort.value !== 'newest') p.set('sort', sort.value);
    var s = p.toString();
    try { history.replaceState(null, '', window.location.pathname + (s ? '?' + s : '') + window.location.hash); } catch (e) { /* file:// */ }
  };

  var timer;
  var apply = function (announce) {
    var terms = normalise(q.value).split(' ').filter(Boolean);
    var shown = 0;
    entries.forEach(function (li) {
      var hay = li.getAttribute('data-search') || '';
      var ok = (type.value === 'all' || li.getAttribute('data-type') === type.value) &&
               (topic.value === 'all' || (' ' + li.getAttribute('data-themes') + ' ').indexOf(' ' + topic.value + ' ') !== -1) &&
               terms.every(function (t) { return hay.indexOf(t) !== -1; });
      li.hidden = !ok;
      if (ok) shown++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector('.bib-entry:not([hidden])'); });

    // Order: newest or oldest first (groups and entries inside groups).
    var asc = sort.value === 'oldest';
    var ordered = groups.slice().sort(function (a, b) {
      return asc ? a.getAttribute('data-year-group') - b.getAttribute('data-year-group') : b.getAttribute('data-year-group') - a.getAttribute('data-year-group');
    });
    ordered.forEach(function (g) {
      root.appendChild(g);
      var list = g.querySelector('.bib-list');
      var items = Array.prototype.slice.call(list.children).sort(function (a, b) {
        var da = a.getAttribute('data-date'), db = b.getAttribute('data-date');
        return asc ? (da > db ? 1 : da < db ? -1 : 0) : (da < db ? 1 : da > db ? -1 : 0);
      });
      items.forEach(function (it) { list.appendChild(it); });
      if (asc) list.removeAttribute('reversed'); else list.setAttribute('reversed', '');
    });

    var msg = shown === total ? 'Showing all ' + total + ' works' : 'Showing ' + shown + ' of ' + total + ' works';
    count.textContent = msg;
    empty.hidden = shown !== 0;
    reset.disabled = !q.value && type.value === 'all' && topic.value === 'all' && sort.value === 'newest';
    syncUrl();
    if (announce && window.LS_announce) window.LS_announce(msg);
  };

  q.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(function () { apply(true); }, 180); });
  [type, topic, sort].forEach(function (el) { el.addEventListener('change', function () { apply(true); }); });
  form.addEventListener('submit', function (ev) { ev.preventDefault(); apply(true); });
  reset.addEventListener('click', function () {
    q.value = ''; type.value = 'all'; topic.value = 'all'; sort.value = 'newest';
    apply(true); q.focus();
  });
  var emptyReset = document.getElementById('bib-empty-reset');
  if (emptyReset) emptyReset.addEventListener('click', function () { reset.click(); });

  apply(false);
})();
