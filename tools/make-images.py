#!/usr/bin/env python3
"""Generates og.png (1200x630) and apple-touch-icon.png (180x180).

Run from the repo root:  python3 tools/make-images.py
Fonts fall back to DejaVu; swap SERIF/SANS below for Fraunces / Instrument Sans
to match the site exactly if you have them installed locally.
"""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ESPRESSO = (59, 36, 22)
INK      = (26, 19, 16)
CREAM    = (255, 246, 234)
AMBER    = (210, 128, 43)
MUTED    = (188, 166, 148)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS  = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def vgradient(size, top, bottom):
    w, h = size
    base = Image.new("RGB", (1, h))
    px = base.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        px[0, y] = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return base.resize((w, h))


def make_og():
    W, H = 1200, 630
    img = vgradient((W, H), (74, 46, 28), (30, 19, 13))
    d = ImageDraw.Draw(img)

    # warm glow behind the stamp row
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([820, 280, 1300, 700], fill=(210, 128, 43, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(130))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    d = ImageDraw.Draw(img)

    f_eyebrow = font(SANS, 22)
    f_h1      = font(SERIF, 64)
    f_sub     = font(SANS, 27)
    f_foot    = font(SANS, 23)

    x = 80
    d.text((x, 88), "PASSQR  ·  LOYALTY", font=f_eyebrow, fill=AMBER)

    d.text((x, 148), "The stamp card that's", font=f_h1, fill=CREAM)
    d.text((x, 224), "already in their phone.", font=f_h1, fill=CREAM)

    d.text((x, 336), "Apple Wallet and Google Wallet loyalty cards for",
           font=f_sub, fill=MUTED)
    d.text((x, 374), "cafés, salons, gyms, studios and market stalls.",
           font=f_sub, fill=MUTED)

    # stamp row: 4 filled of 10
    sx, sy, r, gap = x, 456, 21, 54
    for i in range(10):
        cx = sx + i * gap
        box = [cx, sy, cx + r * 2, sy + r * 2]
        if i < 4:
            d.ellipse(box, fill=AMBER)
            d.line([cx + 12, sy + 21, cx + 18, sy + 28, cx + 30, sy + 14],
                   fill=(42, 26, 18), width=4)
        else:
            d.ellipse(box, outline=(120, 96, 78), width=2)

    d.text((x, 538), "No app.  No signup.  Scan to stamp.", font=f_foot, fill=CREAM)

    img.save(os.path.join(ROOT, "og.png"), optimize=True)
    print("wrote og.png")


def make_icon():
    S = 180
    img = Image.new("RGB", (S, S), ESPRESSO)
    d = ImageDraw.Draw(img)
    # three QR finder squares + a stamp tick, echoing the site mark
    def finder(x, y, s):
        d.rounded_rectangle([x, y, x + s, y + s], radius=9, outline=CREAM, width=9)
    finder(26, 26, 54)
    finder(100, 26, 54)
    finder(26, 100, 54)
    d.ellipse([100, 100, 154, 154], fill=AMBER)
    d.line([112, 128, 123, 139, 143, 114], fill=INK, width=9,
           joint="curve")
    img.save(os.path.join(ROOT, "apple-touch-icon.png"), optimize=True)
    print("wrote apple-touch-icon.png")


if __name__ == "__main__":
    make_og()
    make_icon()
