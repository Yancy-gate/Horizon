(function () {
  'use strict';

  var FEEDBACK_KEY = 'horizon-feedback-v1';

  /** Replace ⭐️ N/10 with a colored badge in h2, h3, and li elements */
  function processScoreBadges() {
    var scoreRe = /⭐️\s*(\d+(?:\.\d+)?)\/10/;
    var targets = document.querySelectorAll('.main-content h2, .main-content h3, .main-content li');
    targets.forEach(function (el) {
      var m = el.innerHTML.match(scoreRe);
      if (!m) return;
      var score = parseFloat(m[1]);
      var tier;
      if (score >= 9) tier = 'high';
      else if (score >= 7) tier = 'good';
      else if (score >= 5) tier = 'mid';
      else tier = 'low';
      el.innerHTML = el.innerHTML.replace(
        scoreRe,
        '<span class="score-badge" data-tier="' + tier + '">' + m[1] + '</span>'
      );
    });
  }

  /** Add semantic classes to tag lines, source lines, and background paragraphs */
  function markSemanticElements() {
    var paragraphs = document.querySelectorAll('.main-content p');
    paragraphs.forEach(function (p) {
      var text = p.textContent.trim();

      if (/^(Tags|标签)\s*:/.test(text)) {
        p.classList.add('tag-line');
        return;
      }

      if (/^(rss|reddit|github|hackernews|hn|telegram)\s*·/i.test(text)) {
        p.classList.add('source-line');
        return;
      }
    });
  }

  function readLang() {
    try {
      var saved = localStorage.getItem('horizon-lang');
      return saved === 'en' ? 'en' : 'zh';
    } catch (e) {
      return 'zh';
    }
  }

  function loadFeedbackStore() {
    try {
      var raw = localStorage.getItem(FEEDBACK_KEY);
      if (!raw) return [];
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function saveFeedbackStore(entries) {
    try {
      localStorage.setItem(FEEDBACK_KEY, JSON.stringify(entries));
    } catch (e) { /* noop */ }
  }

  function normalizeUrl(url) {
    try {
      var parsed = new URL(url);
      var host = parsed.hostname.replace(/^www\./, '');
      var path = parsed.pathname.replace(/\/$/, '');
      return host + path;
    } catch (e) {
      return url;
    }
  }

  function findRating(entries, url) {
    var key = normalizeUrl(url);
    for (var i = entries.length - 1; i >= 0; i--) {
      if (normalizeUrl(entries[i].url) === key) {
        return entries[i].rating;
      }
    }
    return null;
  }

  function upsertFeedback(entry) {
    var entries = loadFeedbackStore();
    var key = normalizeUrl(entry.url);
    entries = entries.filter(function (item) {
      return normalizeUrl(item.url) !== key;
    });
    entries.push(entry);
    saveFeedbackStore(entries);
    return entries;
  }

  function showToast(message) {
    var toast = document.querySelector('.hz-feedback-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'hz-feedback-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    window.setTimeout(function () {
      toast.classList.remove('show');
    }, 1800);
  }

  function setupFeedbackControls() {
    var anchors = document.querySelectorAll('.main-content .hz-item-anchor');
    if (!anchors.length) return;

    anchors.forEach(function (anchor) {
      var url = anchor.getAttribute('data-hz-url');
      if (!url) return;

      var heading = anchor.nextElementSibling;
      if (!heading || heading.tagName !== 'H2') return;

      var bar = document.createElement('div');
      bar.className = 'hz-feedback';

      var upBtn = document.createElement('button');
      upBtn.type = 'button';
      upBtn.className = 'hz-feedback-btn';
      upBtn.setAttribute('data-rating', 'up');
      upBtn.textContent = readLang() === 'zh' ? '👍 有用' : '👍 Useful';

      var downBtn = document.createElement('button');
      downBtn.type = 'button';
      downBtn.className = 'hz-feedback-btn';
      downBtn.setAttribute('data-rating', 'down');
      downBtn.textContent = readLang() === 'zh' ? '👎 不太相关' : '👎 Not relevant';

      bar.appendChild(upBtn);
      bar.appendChild(downBtn);
      heading.insertAdjacentElement('afterend', bar);

      function paintActive(rating) {
        upBtn.classList.remove('active-up');
        downBtn.classList.remove('active-down');
        if (rating === 'up') upBtn.classList.add('active-up');
        if (rating === 'down') downBtn.classList.add('active-down');
      }

      paintActive(findRating(loadFeedbackStore(), url));

      function handleClick(rating) {
        var tagsRaw = anchor.getAttribute('data-hz-tags') || '';
        var tags = tagsRaw ? tagsRaw.split(',').map(function (t) { return t.trim(); }).filter(Boolean) : [];
        var entry = {
          url: url,
          title: anchor.getAttribute('data-hz-title') || heading.textContent.trim(),
          tags: tags,
          rating: rating,
          section: anchor.getAttribute('data-hz-section') || 'other',
          lang: readLang(),
          created_at: new Date().toISOString(),
          source: 'web'
        };
        upsertFeedback(entry);
        paintActive(rating);
        showToast(readLang() === 'zh' ? '已记录，记得导出同步' : 'Saved — export to sync');
      }

      upBtn.addEventListener('click', function () { handleClick('up'); });
      downBtn.addEventListener('click', function () { handleClick('down'); });
    });

    if (!document.querySelector('.hz-feedback-export')) {
      var exportBtn = document.createElement('button');
      exportBtn.type = 'button';
      exportBtn.className = 'hz-feedback-export';
      exportBtn.textContent = readLang() === 'zh' ? '导出偏好反馈' : 'Export feedback';
      exportBtn.addEventListener('click', exportFeedback);
      document.body.appendChild(exportBtn);
    }
  }

  function exportFeedback() {
    var entries = loadFeedbackStore();
    if (!entries.length) {
      showToast(readLang() === 'zh' ? '暂无反馈可导出' : 'No feedback yet');
      return;
    }

    var payload = {
      exported_at: new Date().toISOString(),
      entries: entries
    };

    var blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    var link = document.createElement('a');
    var stamp = new Date().toISOString().slice(0, 10);
    link.href = URL.createObjectURL(blob);
    link.download = 'horizon-feedback-' + stamp + '.json';
    link.click();
    URL.revokeObjectURL(link.href);
    showToast(
      readLang() === 'zh'
        ? '已下载，放入 feedback-inbox/ 后跑 ingest'
        : 'Downloaded — drop into feedback-inbox/'
    );
  }

  /** Set up EN/中文 language toggle as a page-level control */
  function setupLanguageToggle() {
    var toggle = document.createElement('div');
    toggle.className = 'lang-toggle';

    var btnEn = document.createElement('button');
    btnEn.textContent = 'EN';
    btnEn.type = 'button';

    var btnZh = document.createElement('button');
    btnZh.textContent = '中文';
    btnZh.type = 'button';

    toggle.appendChild(btnEn);
    toggle.appendChild(btnZh);
    document.body.insertBefore(toggle, document.body.firstChild);

    var saved = null;
    try { saved = localStorage.getItem('horizon-lang'); } catch (e) { /* noop */ }
    var currentLang = saved === 'en' ? 'en' : 'zh';

    function updateButtons(lang) {
      if (lang === 'en') {
        btnEn.classList.add('active');
        btnZh.classList.remove('active');
      } else {
        btnZh.classList.add('active');
        btnEn.classList.remove('active');
      }
    }

    var zhSection = document.getElementById('lang-zh');
    var enSection = document.getElementById('lang-en');

    function showSection(lang) {
      if (!zhSection || !enSection) return;
      if (lang === 'en') {
        enSection.classList.remove('hidden');
        zhSection.classList.add('hidden');
      } else {
        zhSection.classList.remove('hidden');
        enSection.classList.add('hidden');
      }
    }

    function switchArticleLang(lang) {
      var path = window.location.pathname;
      var target = null;
      if (lang === 'en' && /-zh(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-zh(\.html)?$/, '-en$1').replace(/-zh\/$/, '-en/');
      } else if (lang === 'zh' && /-en(?:\.html)?$/.test(path.replace(/\/$/, ''))) {
        target = path.replace(/-en(\.html)?$/, '-zh$1').replace(/-en\/$/, '-zh/');
      }
      if (target) window.location.href = target;
    }

    function setLang(lang) {
      currentLang = lang;
      updateButtons(lang);
      try { localStorage.setItem('horizon-lang', lang); } catch (e) { /* noop */ }
      if (zhSection && enSection) {
        showSection(lang);
      } else {
        switchArticleLang(lang);
      }
    }

    btnEn.addEventListener('click', function () { setLang('en'); });
    btnZh.addEventListener('click', function () { setLang('zh'); });

    updateButtons(currentLang);
    if (zhSection && enSection) {
      showSection(currentLang);
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    processScoreBadges();
    markSemanticElements();
    setupLanguageToggle();
    setupFeedbackControls();
  });
})();
