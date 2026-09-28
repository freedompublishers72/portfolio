/* Sitewide utilities.
   Back to top: created here so the control only exists when JS can operate
   it. Revealed after one viewport of scroll; the click handler defers to CSS
   scroll-behavior, which is smooth normally and auto under
   prefers-reduced-motion. */

(function () {
  'use strict';

  var button = document.createElement('button');
  button.type = 'button';
  button.className = 'back-to-top';
  button.setAttribute('aria-label', 'Back to top');
  button.textContent = '↑ Back to top';

  var threshold = window.innerHeight;
  var queued = false;

  function update() {
    queued = false;
    button.classList.toggle('back-to-top--visible',
      window.scrollY > threshold);
  }

  function queue() {
    if (!queued) {
      queued = true;
      requestAnimationFrame(update);
    }
  }

  window.addEventListener('scroll', queue, { passive: true });
  window.addEventListener('resize', function () {
    threshold = window.innerHeight;
    queue();
  }, { passive: true });

  button.addEventListener('click', function () {
    window.scrollTo(0, 0);
  });

  document.body.appendChild(button);
  update();
})();

/* Deep-link whitepapers: open the targeted disclosure before the browser scrolls to it. */
(function () {
  'use strict';

  function openTargetedWhitepaper() {
    var hash = window.location.hash;
    if (!hash) return;

    var target = document.getElementById(hash.slice(1));
    if (!target || !target.closest('.case-study')) return;

    var disclosure = target.closest('.case-study');
    disclosure.open = true;

    window.requestAnimationFrame(function () {
      target.scrollIntoView({ block: 'start' });
    });
  }

  window.addEventListener('DOMContentLoaded', openTargetedWhitepaper);
  window.addEventListener('hashchange', openTargetedWhitepaper);
})();

/* Measured performance history: append the next dated report directly below the current one. */
(function () {
  'use strict';

  function addPerformanceHistoryEntry() {
    var current = document.querySelector('.performance-evidence-figure');
    if (!current || current.dataset.historyExtended === 'true') return;

    var next = document.createElement('figure');
    next.className = 'performance-evidence-figure';
    next.dataset.historyEntry = '2026-09-28';

    var image = document.createElement('img');
    image.src = 'assets/images/gtmetrix-score-sria-2026-09-28.webp';
    image.alt = 'GTmetrix performance report for siemreapinside.asia: Grade A, Performance 98 percent, Structure 98 percent, Largest Contentful Paint 929 milliseconds, Total Blocking Time 98 milliseconds, and Cumulative Layout Shift 0.01.';
    image.width = 1024;
    image.height = 140;

    next.appendChild(image);
    current.insertAdjacentElement('afterend', next);
    current.dataset.historyExtended = 'true';
  }

  window.addEventListener('DOMContentLoaded', addPerformanceHistoryEntry);
})();
