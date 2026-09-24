/* animations.js: hero entrance, scroll reveals, counters, parallax, progress bar */
(() => {
  'use strict';

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  /* ---------- hero entrance ---------- */
  const heroEls = $$('[data-hero-el]');
  heroEls.forEach((el) => el.style.setProperty('--el-delay', el.dataset.heroDelay || 0));
  requestAnimationFrame(() =>
    requestAnimationFrame(() => heroEls.forEach((el) => el.classList.add('is-in')))
  );

  /* ---------- hero scroll button ---------- */
  const heroBtn = document.getElementById('hero-scroll');
  if (heroBtn) {
    heroBtn.addEventListener('click', () => {
      const t = document.getElementById('trust') || document.getElementById('problem');
      if (t) t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
    });
  }

  /* ---------- counters ---------- */
  const runCount = (el) => {
    const end = parseFloat(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    if (reduce || isNaN(end)) { el.textContent = end + suffix; return; }
    const start = performance.now();
    const dur = 1400;
    const tick = (now) => {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(end * eased) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  /* ---------- scroll reveals ---------- */
  const targets = $$('[data-reveal], [data-stagger]');
  $$('[data-stagger]').forEach((group) => {
    Array.from(group.children).forEach((child, i) => {
      if (!child.style.getPropertyValue('--i')) child.style.setProperty('--i', i);
    });
  });

  if (!('IntersectionObserver' in window) || reduce) {
    targets.forEach((el) => el.classList.add('is-visible'));
    $$('[data-count]').forEach(runCount);
  } else {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          el.classList.add('is-visible');
          $$('[data-count]', el).forEach(runCount);
          io.unobserve(el);
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -8% 0px' }
    );
    targets.forEach((el) => io.observe(el));

    // counters that live outside a reveal group (hero proof)
    const co = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { runCount(e.target); co.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    $$('[data-count]').forEach((el) => {
      if (!el.closest('[data-reveal], [data-stagger]')) co.observe(el);
    });
  }

  /* ---------- scroll progress bar + hero blob parallax ---------- */
  const bar = document.createElement('div');
  bar.className = 'scroll-progress';
  bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);
  const hero = document.querySelector('.hero');
  let ticking = false;

  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.setProperty('--p', max > 0 ? (window.scrollY / max).toFixed(4) : 0);
      if (hero && !reduce && window.scrollY < window.innerHeight * 1.2) {
        hero.style.setProperty('--sy', (window.scrollY * 0.18).toFixed(1));
      }
      ticking = false;
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- hero pointer parallax + spotlight ---------- */
  const visual = document.querySelector('.hero__visual');
  if (hero && visual && !reduce && window.matchMedia('(pointer: fine)').matches) {
    let tx = 0, ty = 0, x = 0, y = 0, running = false;
    const loop = () => {
      x += (tx - x) * 0.08;
      y += (ty - y) * 0.08;
      visual.style.setProperty('--px', x.toFixed(3));
      visual.style.setProperty('--py', y.toFixed(3));
      if (Math.abs(tx - x) > 0.002 || Math.abs(ty - y) > 0.002) requestAnimationFrame(loop);
      else running = false;
    };
    hero.addEventListener('pointermove', (e) => {
      const r = visual.getBoundingClientRect();
      tx = Math.max(-1, Math.min(1, ((e.clientX - r.left) / r.width) * 2 - 1));
      ty = Math.max(-1, Math.min(1, ((e.clientY - r.top) / r.height) * 2 - 1));
      const h = hero.getBoundingClientRect();
      hero.style.setProperty('--mx', e.clientX - h.left + 'px');
      hero.style.setProperty('--my', e.clientY - h.top + 'px');
      if (!running) { running = true; requestAnimationFrame(loop); }
    });
    hero.addEventListener('pointerleave', () => {
      tx = 0; ty = 0;
      if (!running) { running = true; requestAnimationFrame(loop); }
    });
  }

  /* ---------- service card spotlight ---------- */
  if (!reduce) {
    $$('.svc-card').forEach((card) => {
      card.addEventListener('pointermove', (e) => {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--mx', e.clientX - r.left + 'px');
        card.style.setProperty('--my', e.clientY - r.top + 'px');
      });
    });
  }
})();
