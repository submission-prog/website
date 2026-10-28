/* Shop cart: kept in localStorage, checkout via /api/checkout (Stripe Checkout). */
(function () {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const KEY = 'pm_cart';
  const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } };
  const save = c => { try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {} };
  const items = Object.fromEntries($$('.item').map(el => [el.dataset.id, { name: el.dataset.name, price: +el.dataset.price }]));
  const money = c => 'S$' + (c / 100).toLocaleString('en-SG', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  let cart = load();
  const cartEl = $('#cart'), fab = $('#cartfab'), veil = $('.cart-veil'), lines = $('.cart-lines'), sum = $('.sum'), msg = $('.cart-msg');

  function render() {
    const ids = Object.keys(cart).filter(id => items[id] && cart[id] > 0);
    let total = 0;
    lines.innerHTML = ids.length ? ids.map(id => {
      const q = cart[id], it = items[id]; total += q * it.price;
      return `<div class="line" data-id="${id}"><div><b>${it.name}</b><span>${money(it.price)} × ${q}</span></div><div class="qty"><button type="button" data-q="-1" aria-label="Less">−</button><span>${q}</span><button type="button" data-q="1" aria-label="More">+</button></div><b>${money(q * it.price)}</b><button type="button" class="rm" data-rm aria-label="Remove">×</button></div>`;
    }).join('') : '<p class="muted small">Your cart is empty.</p>';
    sum.textContent = money(total);
    const n = ids.reduce((a, id) => a + cart[id], 0);
    fab.hidden = n === 0; $('.count', fab).textContent = n;
    $('[data-checkout]').disabled = n === 0;
    save(cart);
  }
  const open = () => { cartEl.hidden = false; veil.hidden = false; void cartEl.offsetWidth; cartEl.classList.add('open'); };   // reflow so the slide-in still animates after display:none
  const close = () => { cartEl.classList.remove('open'); setTimeout(() => { cartEl.hidden = true; veil.hidden = true; }, 350); };

  $$('.item').forEach(el => {
    const inp = $('input', el);
    $$('[data-q]', el).forEach(b => b.addEventListener('click', () => { inp.value = Math.min(50, Math.max(1, (+inp.value || 1) + +b.dataset.q)); }));
    $('.add', el).addEventListener('click', () => {
      cart[el.dataset.id] = Math.min(50, (cart[el.dataset.id] || 0) + (+inp.value || 1));
      inp.value = 1; render(); open();
    });
  });
  lines.addEventListener('click', e => {
    const line = e.target.closest('.line'); if (!line) return;
    const id = line.dataset.id;
    if (e.target.closest('[data-rm]')) delete cart[id];
    else if (e.target.closest('[data-q]')) { cart[id] = Math.min(50, Math.max(0, cart[id] + +e.target.closest('[data-q]').dataset.q)); if (!cart[id]) delete cart[id]; }
    render();
  });
  $$('[data-open-cart]').forEach(b => b.addEventListener('click', open));
  $$('[data-close-cart]').forEach(b => b.addEventListener('click', close));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !cartEl.hidden) close(); });

  $('[data-checkout]').addEventListener('click', async () => {
    const btn = $('[data-checkout]'); btn.disabled = true; msg.hidden = true;
    const body = { items: Object.keys(cart).map(id => ({ id, qty: cart[id] })) };
    try {
      const r = await fetch('/api/checkout', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      const d = await r.json().catch(() => ({}));
      if (r.ok && d.url) { location.href = d.url; return; }
      msg.textContent = d.message || 'Online payment is not available right now. Please WhatsApp us to book.';
    } catch (e) { msg.textContent = 'Could not reach the payment service. Please WhatsApp us to book.'; }
    msg.hidden = false; btn.disabled = false;
  });
  if (new URLSearchParams(location.search).get('cancelled')) { msg.textContent = 'Payment was cancelled. Your cart is still here.'; msg.hidden = false; open(); }
  render();
})();
