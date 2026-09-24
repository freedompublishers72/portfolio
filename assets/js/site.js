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
