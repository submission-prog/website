/* PESTIMESH — shared behaviour (vanilla JS, no dependencies) */
(function () {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];




  /* ---- Preloader: hold on the logo, then split the panels open ---- */
  (function () {
    const pl = document.getElementById('preload');
    if (!pl) { document.body.classList.remove('preloading'); return; }
    requestAnimationFrame(() => pl.classList.add('ready'));   // fade the logo in
    const MIN = matchMedia('(prefers-reduced-motion: reduce)').matches ? 200 : 1000;
    const t0 = performance.now();
    let done = false;
    const open = () => {
      if (done) return; done = true;
      setTimeout(() => {
        pl.classList.add('done');
        document.body.classList.remove('preloading');
        setTimeout(() => pl.classList.add('gone'), 950);
      }, Math.max(0, MIN - (performance.now() - t0)));
    };
    document.readyState === 'complete' ? open() : addEventListener('load', open);
    setTimeout(open, 5000);                       // never trap the visitor behind a slow asset
  })();

  /* ---- Home hero sequence: a frame sequence drawn on canvas. The page is held on the
         opening scene; the first scroll (or tap on the cue) plays it once to the end
         scene, reveals the hero copy, and releases the page. ---- */
  (function () {
    const hero = document.querySelector('[data-heroseq]');
    if (!hero) return;
    const canvas = hero.querySelector('.seq-canvas'), ctx = canvas.getContext('2d');
    const N = +hero.dataset.frames || 121, DURATION = 3000;
    const small = Math.min(innerWidth, innerHeight * 1.2) < 820;
    const src = i => `assets/heroseq/${small ? 'm' : 'f'}_${String(i + 1).padStart(3, '0')}.jpg`;
    const frames = new Array(N), root = document.documentElement;
    let current = -1, state = 'intro';

    const size = () => {
      const dpr = Math.min(devicePixelRatio || 1, 1.5);
      canvas.width = Math.round(hero.clientWidth * dpr); canvas.height = Math.round(hero.clientHeight * dpr);
      const keep = current; current = -1; draw(Math.max(0, keep));
    };
    const draw = i => {
      const img = frames[i];
      if (!img || !img.complete || !img.naturalWidth) return false;
      const cw = canvas.width, ch = canvas.height, s = Math.max(cw / img.naturalWidth, ch / img.naturalHeight);
      const w = img.naturalWidth * s, h = img.naturalHeight * s;
      // on narrow screens drift the focal point from the tunnel (centre) to the technician (right of centre)
      const fx = 0.5 + (cw < ch ? 0.18 : 0) * (i / (N - 1));
      const x = Math.min(0, Math.max(cw - w, cw / 2 - w * fx));
      ctx.drawImage(img, x, (ch - h) / 2, w, h);
      current = i; return true;
    };
    const load = i => new Promise(res => { const im = new Image(); im.onload = im.onerror = () => res(); im.src = src(i); frames[i] = im; });

    const end = instant => {
      state = 'ended';
      hero.classList.remove('playing'); hero.classList.add('ended');
      root.classList.remove('seq-lock');
      if (instant) load(N - 1).then(() => draw(N - 1));
    };
    const play = () => {
      if (state !== 'intro' || document.body.classList.contains('preloading')) return;
      state = 'playing'; hero.classList.add('playing');
      const t0 = performance.now();
      const tick = t => {
        const p = Math.min(1, (t - t0) / DURATION), eased = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
        let target = Math.round(eased * (N - 1));
        while (target > current && !draw(target)) target--;          // hold on the newest loaded frame
        if (p < 1) requestAnimationFrame(tick);
        else { draw(N - 1); end(false); }
      };
      requestAnimationFrame(tick);
    };

    const skip = matchMedia('(prefers-reduced-motion: reduce)').matches || location.hash.length > 1 || scrollY > 10;
    addEventListener('resize', size);
    if (skip) { size(); end(true); return; }

    root.classList.add('seq-lock'); scrollTo(0, 0);
    load(0).then(() => { size(); (async () => { for (let i = 1; i < N; i++) { await load(i); } })(); });

    addEventListener('wheel', e => { if (state !== 'ended') { e.preventDefault(); if (e.deltaY > 0) play(); } }, { passive: false });
    let ty = 0;
    addEventListener('touchstart', e => { ty = e.touches[0].clientY; }, { passive: true });
    addEventListener('touchmove', e => { if (state !== 'ended') { if (ty - e.touches[0].clientY > 8) play(); e.preventDefault(); } }, { passive: false });
    addEventListener('keydown', e => { if (state === 'intro' && ['ArrowDown', 'PageDown', ' ', 'Enter', 'End'].includes(e.key)) { e.preventDefault(); play(); } });
    hero.addEventListener('click', play);          // a tap anywhere on the opening scene also plays it
    // in-page links (e.g. "Book an inspection") should never be trapped behind the intro
    document.addEventListener('click', e => { const a = e.target.closest('a[href*="#"]'); if (a && state !== 'ended') end(true); });
  })();

  /* ---- Nav: solid on scroll, mobile menu ---- */
  const nav = $('.nav');
  const onScroll = () => nav && nav.classList.toggle('scrolled', window.scrollY > 40);
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });
  const burger = $('.burger'), mob = $('.mobile-menu');
  if (burger && mob) {
    burger.addEventListener('click', () => {
      const open = mob.classList.toggle('open');
      document.body.style.overflow = open ? 'hidden' : '';
      nav.classList.toggle('scrolled', open || window.scrollY > 40);
    });
  }
  // mark active nav link
  const here = location.pathname.split('/').pop() || 'index.html';
  $$('.nav-links > li > a, .mobile-menu a').forEach(a => {
    if ((a.getAttribute('href') || '').split('#')[0] === here) a.classList.add('active');
  });


  /* ---- Services dropdown: open on hover, close after a short delay so the
         pointer can travel diagonally into the panel without it vanishing ---- */
  $$('.nav-links > li').filter(li => $('.mega', li)).forEach(li => {
    let t;
    const open = () => { clearTimeout(t); li.classList.add('open'); };
    const close = () => { clearTimeout(t); t = setTimeout(() => li.classList.remove('open'), 260); };
    li.addEventListener('pointerenter', open);
    li.addEventListener('pointerleave', close);
    li.addEventListener('focusin', open);
    li.addEventListener('focusout', close);
    $('.mega', li).addEventListener('pointerenter', open);
  });

  /* ---- Hero headline: one sentence per line, each line rises into place ---- */
  $$('.hero .display[data-split]').forEach(h => {
    const lines = h.textContent.trim().split(/(?<=\.)\s+/).filter(Boolean);
    h.innerHTML = lines.map((l, i) => `<span class="ln"><span style="animation-delay:${0.15 + i * 0.12}s">${l}</span></span>`).join('');
  });

  /* ---- Reveal on scroll ---- */
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0, rootMargin: '0px 0px -12% 0px' });   // fires as soon as any part enters, works for very tall blocks
  $$('.reveal, .reveal-stagger, .line-reveal').forEach(el => io.observe(el));

  /* ---- Counters ---- */
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; cio.unobserve(e.target);
    const el = e.target, end = parseFloat(el.dataset.count), dec = (el.dataset.count.split('.')[1] || '').length;
    const suffix = el.dataset.suffix || '', t0 = performance.now(), dur = 1600;
    const tick = t => {
      const p = Math.min(1, (t - t0) / dur), ease = 1 - Math.pow(1 - p, 3);
      const v = (end * ease).toFixed(dec); el.textContent = (end >= 10000 ? v.replace(/\B(?=(\d{3})+(?!\d))/g, ',') : v) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }), { threshold: 0.5 });
  $$('[data-count]').forEach(el => cio.observe(el));

  /* ---- Parallax on framed images ---- */
  const par = $$('.frame.parallax img, .page-hero .bg');
  if (par.length && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const upd = () => {
      par.forEach(img => {
        const r = img.getBoundingClientRect(), vh = innerHeight;
        if (r.bottom < 0 || r.top > vh) return;
        const p = (r.top + r.height / 2 - vh / 2) / vh; // -0.5..0.5
        img.style.transform = `scale(1.15) translateY(${p * -40}px)`;
      });
    };
    upd(); window.addEventListener('scroll', upd, { passive: true });
  }

  /* ---- Cursor glow on cards + 3D tilt on certs (delegated so cloned nodes work) ---- */
  document.addEventListener('pointermove', e => {
    const c = e.target.closest('.card.glow');
    if (c) { const r = c.getBoundingClientRect(); c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px'); }
    const t = e.target.closest('.cert');
    if (t && !t.closest('.cert-slider')) { const r = t.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5; t.style.transform = `perspective(900px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) translateY(-6px)`; }
  });
  document.addEventListener('pointerout', e => { const t = e.target.closest('.cert'); if (t && !t.contains(e.relatedTarget)) t.style.transform = ''; });

  /* ---- Lightbox (certs + galleries) ---- */
  const lb = document.createElement('div');
  lb.className = 'lightbox';
  lb.innerHTML = `<button class="close" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
  <button class="navb prev" aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg></button>
  <img alt=""><div class="cap"></div>
  <button class="navb next" aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg></button>`;
  document.body.appendChild(lb);
  let group = [], idx = 0;
  const show = i => {
    idx = (i + group.length) % group.length;
    const el = group[idx];
    lb.querySelector('img').src = el.dataset.full || el.querySelector('img')?.src;
    const cap = lb.querySelector('.cap');
    cap.innerHTML = `<span>${el.dataset.title || ''}</span>` + (el.dataset.pdf ? `<a href="${el.dataset.pdf}" target="_blank" rel="noopener">Open original PDF ↗</a>` : '');
    lb.classList.add('open'); document.body.style.overflow = 'hidden';
    lb.querySelectorAll('.navb').forEach(b => b.style.display = group.length > 1 ? '' : 'none');
  };
  const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; };
  document.addEventListener('click', e => {
    const el = e.target.closest('[data-lightbox]');
    if (!el || el.closest('.auto-slider')?.dataset.dragged === '1') return;
    e.preventDefault();
    const seen = new Set();
    group = $$(`[data-lightbox="${el.dataset.lightbox}"]`).filter(x => !x.classList.contains('hide') && !seen.has(x.dataset.full) && seen.add(x.dataset.full));
    show(Math.max(0, group.findIndex(x => x.dataset.full === el.dataset.full)));
  });
  lb.querySelector('.close').addEventListener('click', close);
  lb.querySelector('.prev').addEventListener('click', () => show(idx - 1));
  lb.querySelector('.next').addEventListener('click', () => show(idx + 1));
  lb.addEventListener('click', e => { if (e.target === lb) close(); });
  document.addEventListener('keydown', e => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1);
  });

  /* ---- Horizontal scroller buttons ---- */
  $$('[data-hscroll]').forEach(wrap => {
    const track = $('.hscroll', wrap);
    $$('.hs-nav button', wrap).forEach(b => b.addEventListener('click', () => {
      track.scrollBy({ left: (b.dataset.dir === 'next' ? 1 : -1) * (track.clientWidth * .8), behavior: 'smooth' });
    }));
  });

  /* ---- Sub-nav active state ---- */
  const subLinks = $$('.subnav a[href^="#"]');
  if (subLinks.length) {
    const secs = subLinks.map(a => $(a.getAttribute('href'))).filter(Boolean);
    const sio = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) subLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
    }), { rootMargin: '-40% 0px -55% 0px' });
    secs.forEach(s => sio.observe(s));
  }

  /* ---- Enquiry form → WhatsApp / email ---- */
  const WA = '6586681988', MAIL = 'enquiry@pestimesh.com.sg';
  $$('form.form').forEach(f => {
    const msg = () => {
      const d = Object.fromEntries(new FormData(f).entries());
      return `Hi, I'm ${d.name || ''}${d.company ? ' from ' + d.company : ''}. I would like to enquire about ${d.concern || 'pest control'} treatment for a ${d.property || ''} property.${d.message ? ' ' + d.message : ''}${d.phone ? ' My contact: ' + d.phone : ''}${d.email ? ' / ' + d.email : ''}`;
    };
    f.addEventListener('submit', e => {
      e.preventDefault();
      if (!f.reportValidity()) return;
      const d = Object.fromEntries(new FormData(f).entries());
      const body = `Name: ${d.name}\nCompany: ${d.company || '-'}\nPhone: ${d.phone}\nEmail: ${d.email}\nArea of concern: ${d.concern}\nProperty type: ${d.property}\n\n${d.message || ''}`;
      location.href = `mailto:${MAIL}?subject=${encodeURIComponent('Quotation request — ' + d.concern + ' (' + d.property + ')')}&body=${encodeURIComponent(body)}`;
    });
    const wa = $('[data-wa-submit]', f);
    if (wa) wa.addEventListener('click', () => {
      window.open(`https://wa.me/${WA}?text=${encodeURIComponent(msg())}`, '_blank', 'noopener');
    });
  });
  // pre-select concern from ?concern= or hash
  const q = new URLSearchParams(location.search).get('concern');
  if (q) $$('select[name="concern"]').forEach(s => { s.value = q; });


  /* ---- Certificate filter + auto-scrolling slider ---- */
  $$('.auto-slider[data-autoscroll]').forEach(slider => {
    const track = $('.track', slider), master = [...track.children].map(n => n.cloneNode(true));
    const section = slider.closest('section'), filters = $$('.filters button', section), label = $('[data-count-label]', section);
    let x = 0, half = 0, paused = false, dragging = false, startX = 0, startPos = 0, moved = 0, resumeAt = 0;
    const speed = 1.6; // px per frame (~96px/s)
    const render = cat => {
      const items = master.filter(n => cat === 'all' || n.dataset.cat === cat).map(n => n.cloneNode(true));
      const loop = items.concat(items.map(n => n.cloneNode(true)));           // duplicate for seamless loop
      track.innerHTML = ''; loop.forEach(n => track.appendChild(n));
      x = 0; track.style.transform = 'translateX(0)';
      half = track.scrollWidth / 2;
      if (label) label.textContent = `${items.length} ${items.length === 1 ? 'credential' : 'credentials'} · hover to pause, drag to browse`;
    };
    render('all');
    filters.forEach(b => b.addEventListener('click', () => { filters.forEach(o => o.classList.remove('on')); b.classList.add('on'); render(b.dataset.filter); }));
    const wrap = () => { if (x >= half) x -= half; if (x < 0) x += half; };
    const tick = t => {
      if (!paused && !dragging && t > resumeAt) { x += speed; wrap(); track.style.transform = `translateX(${-x}px)`; }
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
    slider.addEventListener('pointerenter', () => paused = true);
    slider.addEventListener('pointerleave', () => { paused = false; dragging = false; });
    slider.addEventListener('pointerdown', e => { dragging = true; startX = e.clientX; startPos = x; moved = 0; slider.setPointerCapture(e.pointerId); });
    slider.addEventListener('pointermove', e => { if (!dragging) return; moved = Math.abs(e.clientX - startX); x = startPos - (e.clientX - startX); wrap(); track.style.transform = `translateX(${-x}px)`; });
    const endDrag = () => { if (!dragging) return; dragging = false; resumeAt = performance.now() + 1500; slider.dataset.dragged = moved > 6 ? '1' : '0'; setTimeout(() => slider.dataset.dragged = '0', 60); };
    slider.addEventListener('pointerup', endDrag); slider.addEventListener('pointercancel', endDrag);
    slider.addEventListener('click', e => { if (slider.dataset.dragged === '1') { e.preventDefault(); e.stopPropagation(); } }, true);
    slider.addEventListener('dragstart', e => e.preventDefault());
    $$('.hs-nav button', section).forEach(b => b.addEventListener('click', () => {
      const item = track.firstElementChild, gap = 22, step = (item ? item.getBoundingClientRect().width + gap : 320) * 2 * (b.dataset.dir === 'next' ? 1 : -1), from = x, t0 = performance.now();
      resumeAt = performance.now() + 2500;
      const anim = t => { const p = Math.min(1, (t - t0) / 500), e = 1 - Math.pow(1 - p, 3); x = from + step * e; wrap(); track.style.transform = `translateX(${-x}px)`; if (p < 1) requestAnimationFrame(anim); };
      requestAnimationFrame(anim);
    }));
    addEventListener('resize', () => { half = track.scrollWidth / 2; });
  });


  /* ---- Slanted 3D certificate wall: alternate columns drift in opposite directions, tied to scroll + gentle idle drift ---- */
  $$('[data-slant]').forEach(stage => {
    const cols = $$('.slant-col', stage).map(c => ({ el: $('.slant-inner', c), dir: +c.dataset.dir, half: 0 }));
    const measure = () => cols.forEach(c => c.half = c.el.scrollHeight / 2);
    measure(); addEventListener('resize', measure); addEventListener('load', measure);
    const mod = (a, n) => ((a % n) + n) % n;
    let drift = 0;
    const frame = () => {
      const r = stage.getBoundingClientRect(), vh = innerHeight;
      if (r.bottom > -200 && r.top < vh + 200) {
        const progress = (r.top + r.height / 2 - vh / 2) / vh;   // -1..1 while passing through the viewport
        drift += 1.1;
        cols.forEach((c, i) => {
          if (!c.half) return;
          const v = c.dir * (progress * 650 + drift) + i * 90;
          c.el.style.transform = `translateY(${-mod(v, c.half)}px)`;
        });
      }
      requestAnimationFrame(frame);
    };
    requestAnimationFrame(frame);
  });



  /* ---- Certificate grid filter ---- */
  const cg = $('#certgrid');
  if (cg) {
    const cards = $$('.cert', cg), label = $('[data-count-label]');
    $$('.filters button').forEach(b => b.addEventListener('click', () => {
      $$('.filters button').forEach(o => o.classList.remove('on')); b.classList.add('on');
      const cat = b.dataset.filter; let n = 0;
      cards.forEach(c => { const show = cat === 'all' || c.dataset.cat === cat; c.classList.toggle('hide', !show); if (show) n++; });
      if (label) label.textContent = cat === 'all' ? `Showing all ${n} credentials` : `Showing ${n} ${n === 1 ? 'credential' : 'credentials'} in ${cat}`;
    }));
  }

  /* ---- Elastic expanding gallery: hover or click a panel to spring it open ---- */
  $$('[data-elastic]').forEach(gal => {
    const panels = $$('.panel', gal);
    const open = p => { panels.forEach(o => o.classList.toggle('on', o === p)); };
    panels.forEach(p => {
      p.addEventListener('pointerenter', () => { if (matchMedia('(hover:hover)').matches) open(p); });
      p.addEventListener('click', e => { if (!p.classList.contains('on')) { e.preventDefault(); open(p); } });
      p.addEventListener('focus', () => open(p));
    });
  });

  /* ---- Marquee: duplicate content for seamless loop ---- */
  $$('.marquee .track').forEach(t => { t.innerHTML += t.innerHTML; });

  /* ---- Footer year ---- */
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
