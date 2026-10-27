// Creates a Stripe Checkout session for the cart posted from site/shop.html.
// Prices are taken from catalogue.json on the server, never from the browser, so they cannot be tampered with.
// Needs the environment variable STRIPE_SECRET_KEY (set in the Vercel project; use the sk_test_ key first).
const catalogue = require('../catalogue.json');

module.exports = async (req, res) => {
  if (req.method !== 'POST') { res.setHeader('Allow', 'POST'); return res.status(405).json({ error: 'POST only' }); }
  const key = process.env.STRIPE_SECRET_KEY;
  if (!key) return res.status(503).json({ error: 'not_configured', message: 'Online payment is not switched on yet.' });

  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch { body = null; } }
  const cart = body && Array.isArray(body.items) ? body.items : [];
  const byId = Object.fromEntries(catalogue.items.map(i => [i.id, i]));
  const line_items = [];
  for (const row of cart) {
    const item = byId[row.id]; const qty = Math.floor(Number(row.qty));
    if (!item || !(qty >= 1 && qty <= 50)) continue;
    line_items.push({
      quantity: qty,
      price_data: { currency: catalogue.currency, unit_amount: item.price,
        product_data: { name: item.name, description: `${item.desc.replace(' Sample item.', '')} (${item.unit})` } },
    });
  }
  if (!line_items.length) return res.status(400).json({ error: 'empty_cart' });

  const stripe = require('stripe')(key);
  const proto = req.headers['x-forwarded-proto'] || 'https';
  const origin = `${proto}://${req.headers['x-forwarded-host'] || req.headers.host}`;
  try {
    const session = await stripe.checkout.sessions.create({
      mode: 'payment',
      line_items,
      phone_number_collection: { enabled: true },
      billing_address_collection: 'required',
      custom_fields: [{ key: 'service_address', label: { type: 'custom', custom: 'Service address (unit, block, postal code)' }, type: 'text', optional: false }],
      success_url: `${origin}/thank-you.html?session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${origin}/shop.html?cancelled=1`,
    });
    return res.status(200).json({ url: session.url });
  } catch (err) {
    console.error('stripe error', err.message);
    return res.status(502).json({ error: 'stripe_error', message: 'Could not start the payment. Please try again or WhatsApp us.' });
  }
};
