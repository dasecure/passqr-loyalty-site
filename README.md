# loyalty.passqr.com

Marketing site for **PassQR Loyalty** — wallet stamp cards for cafés, salons, gyms,
pilates studios and farmers market stalls.

Static, no build step. `index.html` is the whole site; everything else is assets.

## Files

| | |
|---|---|
| `index.html` | The entire landing page — markup, CSS and the one inline script |
| `og.png` | 1200×630 social card |
| `favicon.svg`, `apple-touch-icon.png` | Icons |
| `robots.txt`, `sitemap.xml` | Indexing |
| `_headers` | Cloudflare Pages response headers |
| `tools/make-images.py` | Regenerates `og.png` and `apple-touch-icon.png` |

## The demo link

Every CTA on the page is repointed at runtime from one constant near the bottom of
`index.html`:

```js
var DEMO_URL = "https://demo.dasecure.com";
```

Change that line and every button follows — including if the demo grows a vertical
query param (`?v=pilates`). The `href` attributes in the markup carry the same URL so
the links still work with JavaScript disabled.

## Deploy — Cloudflare Pages

1. **Pages → Create → Connect to Git →** `dasecure/passqr-loyalty-site`
2. Framework preset **None**; build command **empty**; output directory **`/`**
3. Deploy, then **Custom domains → Set up a custom domain →** `loyalty.passqr.com`
   (the `passqr.com` zone is already on this Cloudflare account, so the CNAME is
   created for you)

No environment variables, no secrets.

## Prices

The pricing section mirrors the public `cafe_*` plans in
`dasecure_billing.plans` / `plan_entitlements`. If those change, change them here too:

| Plan | Monthly | Yearly | Shops | Seats | New cards/mo | Broadcasts/mo | History |
|---|---|---|---|---|---|---|---|
| Trial | free | — | 1 | 1 | 50 | 4 | 14 d |
| Solo | $29 | $290 | 1 | 3 | 2,000 | 4 | 90 d |
| Growth | $79 | $790 | 3 | 10 | 6,000 | 8 | 365 d |
| Chain | $199 | $1,990 | 10 | 30 | 20,000 | 20 | 365 d |
| Group | $449 | $4,490 | 25 | ∞ | 100,000 | 40 | 730 d |

`cafe_group_*` and `cafe_founding` are `is_public = false`, so Group appears on the
page as "talk to us" rather than as a price.
