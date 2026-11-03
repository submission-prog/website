/* "Pests We Treat" hologram band (3 Nov 2026). All pests stand in one row on a floor line; the centre one is
   large, sharp and spinning, the neighbours are small, dim and blurred (two canvases, the back one CSS-blurred).
   three.js is fetched only when the band is about to scroll into view, so other pages pay nothing. */
(() => {
  const sec = document.querySelector('[data-holo]');
  if (!sec || !window.WebGLRenderingContext) return;
  const V = '0.128.0', CDN = `https://cdn.jsdelivr.net/npm/three@${V}/`;
  const load = src => new Promise((res, rej) => { const s = document.createElement('script'); s.src = src; s.onload = res; s.onerror = rej; document.head.appendChild(s); });
  const start = async () => {
    try {
      await load(CDN + 'build/three.min.js');
      await Promise.all([load(CDN + 'examples/js/loaders/GLTFLoader.js'), load(CDN + 'examples/js/loaders/DRACOLoader.js'), load(CDN + 'examples/js/controls/OrbitControls.js')]);
      init();
    } catch (e) { sec.classList.add('no3d'); }
  };
  const io = new IntersectionObserver(es => { if (es.some(e => e.isIntersecting)) { io.disconnect(); start(); } }, { rootMargin: '600px 0px' });
  io.observe(sec);

  function init() {
    const PESTS = [...sec.querySelectorAll('[data-pest]')].map(el => ({ el, name: el.dataset.name, file: el.dataset.pest, href: el.dataset.href, blurb: el.dataset.blurb, scale: +el.dataset.scale || 1 }));
    const reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
    const mk = id => { const r = new THREE.WebGLRenderer({ canvas: sec.querySelector(id), antialias: true, alpha: true }); r.setPixelRatio(Math.min(devicePixelRatio, 2)); r.setClearColor(0, 0); return r; };
    const rBack = mk('.holo-back'), rFront = mk('.holo-front');
    const sBack = new THREE.Scene(), sFront = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(30, 1, .01, 100);
    const controls = new THREE.OrbitControls(camera, sec.querySelector('.holo-front'));
    Object.assign(controls, { enableDamping: true, enableZoom: false, enablePan: false, minPolarAngle: 1.0, maxPolarAngle: 1.45, minAzimuthAngle: -.6, maxAzimuthAngle: .6 });
    controls.target.set(0, .22, 0);   // phones: row sits low under the centred text; wide screens raise it (see resize)
    const fres = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, uniforms: { c: { value: new THREE.Color(0x6fc3ff) }, t: { value: 0 } },
      vertexShader: 'varying vec3 vN,vV;void main(){vec4 mv=modelViewMatrix*vec4(position,1.);vN=normalize(normalMatrix*normal);vV=normalize(-mv.xyz);gl_Position=projectionMatrix*mv;}',
      fragmentShader: 'uniform vec3 c;uniform float t;varying vec3 vN,vV;void main(){float f=pow(1.-max(dot(vN,vV),0.),2.2);float s=.85+.15*sin(gl_FragCoord.y*.25+t*6.);gl_FragColor=vec4(c*(.25+f*1.2)*s,(.15+f*.85));}' });
    const wire = new THREE.MeshBasicMaterial({ color: 0x4fb4ff, wireframe: true, transparent: true, opacity: .32 });
    const fill = new THREE.MeshBasicMaterial({ color: 0x0b2a66, transparent: true, opacity: .55 });
    const dl = new THREE.DRACOLoader(); dl.setDecoderPath(CDN + 'examples/js/libs/draco/'); const loader = new THREE.GLTFLoader(); loader.setDRACOLoader(dl);
    const models = new Array(PESTS.length).fill(null), clones = new Array(PESTS.length).fill(null);
    const prep = (g, p) => {
      const root = g.scene; const box = new THREE.Box3().setFromObject(root); const size = box.getSize(new THREE.Vector3());
      const s = 1.9 * p.scale / Math.max(size.x, size.y, size.z); root.scale.setScalar(s);
      const b2 = new THREE.Box3().setFromObject(root); const ctr = b2.getCenter(new THREE.Vector3()); const off = ctr.clone().multiplyScalar(-1); off.y += -.5 - (b2.min.y - ctr.y);
      const ms = []; root.traverse(o => { if (o.isMesh) ms.push(o); });
      ms.forEach(o => { o.material = fill; o.add(new THREE.Mesh(o.geometry, wire)); o.add(new THREE.Mesh(o.geometry, fres)); });
      const g2 = new THREE.Group(); root.position.copy(off); g2.add(root); return g2;
    };
    // the centre pest first, then its neighbours, so the band comes alive as soon as one file lands
    const order = [0, 1, PESTS.length - 1, ...PESTS.slice(2, -1).map((_, k) => k + 2)];
    (async () => { for (const i of order) await new Promise(res => loader.load(PESTS[i].file, g => { models[i] = prep(g, PESTS[i]); sBack.add(models[i]); clones[i] = models[i].clone(); clones[i].visible = false; sBack.add(clones[i]); born(i); place(); res(); }, undefined, () => res())); })();

    let onScreen = false, pendingBirth = [], lastBirth = 0;
    const birthIO = new IntersectionObserver(es => { onScreen = es.some(e => e.isIntersecting); if (onScreen) { const q = pendingBirth; pendingBirth = []; q.forEach(born); } }, { threshold: .25 });
    birthIO.observe(sec);
    function born(i) { return;   // no entrance animation: pests simply appear in place (client, 4 Nov 2026)
      if (!onScreen || reduce) { if (!reduce) pendingBirth.push(i); return; } const t = Math.max(performance.now(), lastBirth + 160); lastBirth = t; models[i].userData.born = t; sec.classList.add('emerging'); clearTimeout(born.t); born.t = setTimeout(() => sec.classList.remove('emerging'), t - performance.now() + 1200); }
    let cur = 0, pos = 0, target = 0, gap = 1.25, shift = 0;
    const team = sec.querySelector('.holo-team'), finger = new THREE.Vector3(0, -1.6, 0); let fingerOn = false;
    const n = PESTS.length, half = n / 2;
    const wrap = o => ((o + half) % n + n) % n - half;            // offset folded into (-n/2, n/2]
    const sizeAt = x => Math.max(.38, 1 - .68 * Math.min(1, Math.abs(x) / gap));
    const ease = k => 1 - Math.pow(1 - k, 3);
    const put = (m, x, born) => { const sc0 = sizeAt(x); let px = x + shift, py = -.5 + .5 * sc0, sc = sc0;
      if (born) { const k = Math.min(1, (performance.now() - born) / 1100); const e = ease(k);               // fly out of the fingertip into the slot
        px = finger.x + (px - finger.x) * e; py = finger.y + (py - finger.y) * e; sc = sc0 * (.04 + .96 * e); if (k >= 1) m.userData.born = 0; }
      m.position.set(px, py, 0); m.scale.setScalar(sc); m.visible = Math.abs(x) < gap * (shift ? 2.5 : 3.3); };
    function place() {
      models.forEach((m, i) => {
        if (!m) return; const o = wrap(i - pos), x = o * gap; put(m, x, m.userData.born);
        const wantFront = Math.abs(x) < gap * .42 && !m.userData.born, inFront = m.parent === sFront;
        if (wantFront && !inFront) { sBack.remove(m); sFront.add(m); } if (!wantFront && inFront) { sFront.remove(m); sBack.add(m); }
        // the far pest shows at both ends while it crosses the seam
        const c = clones[i]; if (!c) return;
        if (o > half - 1) put(c, (o - n) * gap, m.userData.born); else if (o < 1 - half) put(c, (o + n) * gap, m.userData.born); else c.visible = false;
        c.rotation.y = m.rotation.y;
      });
    }
    const nameEl = sec.querySelector('.holo-name'), blurb = sec.querySelector('.holo-blurb'), link = sec.querySelector('.holo-link');
    // a small name under each pest in the row; clicking one brings that pest to the centre
    const labels = document.createElement('div'); labels.className = 'holo-labels'; sec.appendChild(labels);
    const lbl = PESTS.map((p, i) => { const b = document.createElement('button'); b.type = 'button'; b.className = 'holo-lbl'; b.textContent = p.name; b.onclick = () => go(i); labels.appendChild(b); return b; });
    const setText = i => { lbl.forEach((d, j) => d.classList.toggle('on', j === i)); nameEl.querySelector('span').textContent = PESTS[i].name; blurb.textContent = PESTS[i].blurb; link.href = PESTS[i].href; };
    const go = i => { if (i === cur) return; target = pos + wrap(i - pos); cur = i; nameEl.classList.add('out'); setTimeout(() => { setText(i); nameEl.classList.remove('out'); }, 300); };
    const next = () => go((cur + 1) % n), prev = () => go((cur - 1 + n) % n);
    const nb = sec.querySelector('.holo-next'), pb = sec.querySelector('.holo-prev'); if (nb) nb.onclick = next; if (pb) pb.onclick = prev;
    sec.addEventListener('keydown', e => { if (e.key === 'ArrowRight') next(); if (e.key === 'ArrowLeft') prev(); });
    let sx = 0; sec.addEventListener('pointerdown', e => sx = e.clientX); sec.addEventListener('pointerup', e => { const d = e.clientX - sx; if (Math.abs(d) > 90) (d < 0 ? next : prev)(); });
    let timer = reduce ? null : setInterval(() => { if (!document.hidden) next(); }, 7000);
    ['pointerdown', 'keydown'].forEach(ev => sec.addEventListener(ev, () => { if (timer) clearInterval(timer); if (!reduce) timer = setInterval(() => { if (!document.hidden) next(); }, 9000); }));
    const W = () => sec.clientWidth, H = () => sec.clientHeight;
    function labelsPlace() {
      const w = W(), h = H();
      models.forEach((m, i) => {
        const b = lbl[i]; if (!m) { b.style.display = 'none'; return; }
        const c = clones[i]; const src = (c && c.visible && Math.abs(c.position.x) < Math.abs(m.position.x)) ? c : m;
        if (!src.visible) { b.style.display = 'none'; return; }
        const v = new THREE.Vector3(src.position.x, -.66, 0).project(camera);
        b.style.display = ''; b.style.transform = `translate(${((v.x + 1) / 2 * w).toFixed(1)}px,${((1 - v.y) / 2 * h).toFixed(1)}px) translate(-50%,0)`;
      });
    }
    const floor = () => { camera.updateMatrixWorld(); const v = new THREE.Vector3(0, -.5, 0).project(camera); sec.style.setProperty('--floor', ((1 - v.y) / 2 * 100).toFixed(1) + '%'); };
    function resize() {
      const w = sec.clientWidth, h = sec.clientHeight; [rBack, rFront].forEach(r => r.setSize(w, h, false));
      camera.aspect = w / h; camera.fov = camera.aspect < 1 ? 46 : 30; camera.updateProjectionMatrix();
      gap = camera.aspect < 1 ? 1.1 : 1.25; controls.target.set(0, w >= 1000 ? .62 : .5, 0);
      shift = 0;
      const span = camera.aspect < 1 ? 1.25 : 3 * gap + .9;          // half-width that must fit: phones show the centre pest, wide screens the whole loop
      const d = Math.max(5.6, span / (.92 * Math.tan(camera.fov * Math.PI / 360) * camera.aspect)); camera.position.set(0, 1.1 * d / 5.6, d); controls.update(); floor();
      // where the pests come from: the pointing fingertip on wide screens, below the row on phones
      fingerOn = w >= 1000 && team && getComputedStyle(team).display !== 'none';
      if (fingerOn) { const r = team.getBoundingClientRect(), s0 = sec.getBoundingClientRect(); const [fx, fy] = (team.dataset.finger || '0,0').split(',').map(Number);
        const px = r.left - s0.left + r.width * fx, py = r.top - s0.top + r.height * fy; sec.style.setProperty('--sx', px + 'px'); sec.style.setProperty('--sy', py + 'px');
        const ndc = new THREE.Vector3(px / w * 2 - 1, 1 - py / h * 2, .5).unproject(camera); const dir = ndc.sub(camera.position).normalize(); const t = -camera.position.z / dir.z; finger.copy(camera.position).add(dir.multiplyScalar(t)); }
      else finger.set(0, -1.8, 0);
    }
    addEventListener('resize', resize); resize();
    const t0 = performance.now(); let last = t0, frames = 0;
    (function loop() {
      requestAnimationFrame(loop); const now = performance.now(), dt = Math.min(.05, (now - last) / 1000); last = now;
      if (document.hidden) return;
      fres.uniforms.t.value = (now - t0) / 1000;
      pos += (target - pos) * Math.min(1, dt * 5.5); if (Math.abs(target - pos) < .0005) { pos = target = ((target % n) + n) % n; }
      models.forEach((m, i) => { if (m && !reduce) m.rotation.y += dt * (i === cur ? .5 : .18); });
      place(); controls.update(); if (++frames % 30 === 0) floor(); rBack.render(sBack, camera); rFront.render(sFront, camera); labelsPlace();
    })();
    setText(0); sec.classList.add('ready');
  }
})();
