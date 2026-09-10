# loyalty.passqr.com

Marketing site for **PassQR Loyalty** — wallet stamp cards for cafés, salons, gyms,
pilates studios and farmers market stalls.

Static, no framework. `index.html` is the whole site; everything else is assets.

## Files

| | |
|---|---|
| `index.html` | The entire landing page — markup, CSS and the one inline script |
| `404.html` | Branded not-found page (without it, Pages serves `index.html` at status 200 for every unknown path) |
| `og.png` | 1200×630 social card |
| `favicon.svg`, `apple-touch-icon.png` | Icons |
| `robots.txt`, `sitemap.xml` | Indexing |
| `_headers` | Cloudflare Pages response headers |
| `tools/make-images.py` | Regenerates `og.png` and `apple-touch-icon.png` |

## Deploy

Cloudflare Pages project **`passqr-loyalty`**, git-connected to this repo.
**A push to `main` deploys production automatically.** No environment variables,
no secrets.

The "build" is a copy step that stages only the public files, so `tools/` and
`README.md` are never served:

```
mkdir -p _site && cp index.html 404.html og.png favicon.svg apple-touch-icon.png robots.txt sitemap.xml _headers _site/
```

Output directory is `_site`. **If you add a public file, add it to that command**
(Pages dashboard → Settings → Builds & deployments) or it will not ship.

## The demo link

Every CTA is repointed at runtime from one constant near the bottom of `index.html`
(and a matching one in `404.html`):

```js
var DEMO_URL = "https://demo.passqr.com";
```

Change those two lines and every button follows — including if the demo grows a
vertical query param (`?v=pilates`). The `href` attributes in the markup carry the
same URL, so links still work with JavaScript disabled.

Not covered by the constant: the QR in the dark band is a real, scannable QR
encoding `https://demo.passqr.com`, drawn as an inline SVG path. Regenerate it if
the demo URL ever changes.

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

## Case study

The Golden Coast Broth section is real deployment fact, not marketing copy — three
San Diego market stalls, 8 stamps for a free 16 oz jar, geofenced per market. There
is deliberately **no pull-quote**: none has been given. If one is, add a
`.quoteblock` div inside the left column of `section#case`; the CSS is already there.
