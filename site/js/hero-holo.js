/* Home hero (4 Nov 2026): holographic screens float around the pointing hand. Each card starts at the
   fingertip and flies to its spot when the page loads; positions are fractions of the hero (data-pos on
   wide screens, data-mpos on phones) so they stay anchored however the hero resizes. No WebGL needed. */
(() => {
  const sec = document.querySelector('[data-hero-holo]'); if (!sec) return;
  const team = sec.querySelector('.hh-team'), cards = [...sec.querySelectorAll('.hh-card')];
  const reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
  const place = () => {
    const w = sec.clientWidth, h = sec.clientHeight, wide = w > 900;
    const tr = team.getBoundingClientRect(), sr = sec.getBoundingClientRect(); const [fx, fy] = (team.dataset.finger || '0,0').split(',').map(Number);
    const sx = tr.left - sr.left + tr.width * fx, sy = tr.top - sr.top + tr.height * fy;
    sec.style.setProperty('--sx', sx + 'px'); sec.style.setProperty('--sy', sy + 'px');
    cards.forEach(c => { const [px, py] = ((wide ? c.dataset.pos : c.dataset.mpos) || c.dataset.pos).split(',').map(Number);
      const x = px * w, y = py * h; c.style.setProperty('--x', x + 'px'); c.style.setProperty('--y', y + 'px'); c.style.setProperty('--dx', (sx - x) + 'px'); c.style.setProperty('--dy', (sy - y) + 'px'); });
  };
  const go = () => { place(); if (reduce) { sec.classList.add('hh-in'); return; }
    sec.classList.add('emerging'); requestAnimationFrame(() => requestAnimationFrame(() => sec.classList.add('hh-in')));
    setTimeout(() => sec.classList.remove('emerging'), 400 + cards.length * 180 + 1100); };
  // sequence: wait for the preloader to open, bring the team in, then let the screens fly out
  const imgReady = () => new Promise(res => { if (team.complete) res(); else { team.addEventListener('load', res, { once: true }); setTimeout(res, 2500); } });
  const preloaderDone = () => new Promise(res => { if (!document.body.classList.contains('preloading')) return res();
    const mo = new MutationObserver(() => { if (!document.body.classList.contains('preloading')) { mo.disconnect(); res(); } }); mo.observe(document.body, { attributes: true, attributeFilter: ['class'] }); setTimeout(() => { mo.disconnect(); res(); }, 6000); });
  Promise.all([imgReady(), preloaderDone()]).then(() => { place(); setTimeout(() => { sec.classList.add('hh-team-in'); setTimeout(go, reduce ? 0 : 750); }, reduce ? 0 : 450); });
  addEventListener('resize', place);
})();
