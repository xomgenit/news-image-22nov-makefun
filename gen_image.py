# gen_image.py — draws entry.png for news-image-20261122.
# Built fresh in this session for Sunday 22 November 2026.
# Run: python3 gen_image.py  (writes entry.png next to this file)
import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1024, 1024
PAPER = (247, 242, 231)
NAVY = (20, 33, 61)
NAVY2 = (30, 48, 88)
RED = (193, 39, 45)
GOLD = (212, 160, 60)
TEAL = (14, 110, 110)
INK = (28, 28, 28)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)
CREAM = (255, 251, 240)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def card(draw, box, fill=CREAM, outline=(200, 190, 170), width=2):
    draw.rectangle(box, fill=fill, outline=outline, width=width)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- MASTHEAD ----------
d.rectangle([0, 0, W, 96], fill=NAVY)
d.rectangle([0, 96, W, 100], fill=GOLD)
d.text((24, 22), "SUNDAY 22 NOVEMBER 2026", font=font(BOLD, 40), fill=WHITE)
d.text((24, 72), "THE WORLD IN ONE DAY", font=font(BOLD, 15), fill=GOLD)
_stats = "21 STORIES  ·  8 REGIONS"
_sw = d.textlength(_stats, font=font(BOLD, 22))
d.text((1000 - _sw, 30), _stats, font=font(BOLD, 22), fill=GOLD)

# ---------- LEAD: COP31 ----------
card(d, [24, 116, 1000, 336])
cx, cy, r = 205, 226, 88
d.ellipse([cx - r - 12, cy - r - 12, cx + r + 12, cy + r + 12], fill=GOLD)
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 111, 183))
d.ellipse([cx - 66, cy - 52, cx - 5, cy - 5], fill=(62, 155, 79))
d.ellipse([cx + 5, cy + 10, cx + 66, cy + 57], fill=(62, 155, 79))
d.ellipse([cx + 28, cy - 57, cx + 71, cy - 19], fill=(62, 155, 79))
d.ellipse([cx - 71, cy + 24, cx - 28, cy + 62], fill=(62, 155, 79))
for k in (-45, 0, 45):
    d.arc([cx - r, cy - r, cx + r, cy + r], 90 + k, 270 + k, fill=WHITE, width=2)
d.line([cx - r, cy, cx + r, cy], fill=WHITE, width=2)
d.ellipse([332, 128, 372, 168], fill=(232, 106, 23))
for ang in range(0, 360, 45):
    a = math.radians(ang)
    d.line([352 + 27 * math.cos(a), 148 + 27 * math.sin(a),
            352 + 38 * math.cos(a), 148 + 38 * math.sin(a)],
           fill=(232, 106, 23), width=4)
d.text((400, 126), "CLIMATE  ·  ANTALYA, TURKEY", font=font(BOLD, 19), fill=RED)
d.text((400, 150), "CLIMATE TALKS STALL", font=font(BOLD, 46), fill=NAVY)
d.text((400, 198), "IN OVERTIME", font=font(BOLD, 46), fill=NAVY)
lead_body = ("COP31 enters a second day of overtime. The new draft still "
             "says nothing about fossil fuels — Germany calls it "
             "unacceptable, France warns of a step back.")
for i, ln in enumerate(wrap(d, lead_body, font(REG, 21), 580)):
    d.text((400, 252 + i * 26), ln, font=font(REG, 21), fill=INK)

# ---------- PANEL 1: KYIV ----------
card(d, [24, 352, 502, 546])
d.rectangle([26, 354, 500, 438], fill=(43, 58, 85))
d.rectangle([70, 378, 210, 438], fill=(74, 74, 85))
d.rectangle([230, 392, 330, 438], fill=(90, 90, 100))
for wx in (85, 115, 145, 175):
    for wy in (386, 404, 422):
        d.rectangle([wx, wy, wx + 16, wy + 11], fill=(255, 209, 102))
for wx in (245, 275, 305):
    for wy in (400, 418):
        d.rectangle([wx, wy, wx + 14, wy + 10], fill=(255, 209, 102))
for (sx, sy, sr) in ((360, 402, 20), (386, 380, 23), (412, 398, 17), (440, 408, 15)):
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(150, 150, 155))
d.polygon([(340, 438), (368, 398), (382, 438)], fill=(232, 106, 23))
d.text((40, 446), "14 MISSING AFTER DRONE", font=font(BOLD, 24), fill=NAVY)
d.text((40, 474), "HITS FLATS", font=font(BOLD, 24), fill=NAVY)
d.text((40, 504), "Kyiv region, Ukraine — rescuers dig through", font=font(REG, 15), fill=GREY)
d.text((40, 522), "a wrecked apartment block.", font=font(REG, 15), fill=GREY)

# ---------- PANEL 2: INDONESIA FIRE ----------
card(d, [522, 352, 1000, 546])
d.rectangle([524, 354, 998, 438], fill=(58, 31, 22))
d.rectangle([560, 402, 760, 438], fill=(31, 31, 31))
d.rectangle([780, 378, 800, 438], fill=(31, 31, 31))
d.rectangle([820, 396, 900, 438], fill=(31, 31, 31))
for wx in (580, 620, 660, 700, 840, 870):
    d.rectangle([wx, 414, wx + 18, 428], fill=(255, 209, 102))
d.polygon([(600, 438), (640, 368), (680, 438)], fill=(232, 106, 23))
d.polygon([(660, 438), (700, 382), (740, 438)], fill=(240, 160, 30))
d.polygon([(720, 438), (755, 392), (790, 438)], fill=(232, 106, 23))
d.polygon([(630, 438), (660, 402), (690, 438)], fill=(245, 200, 60))
for (sx, sy, sr) in ((920, 392, 24), (945, 378, 20), (965, 398, 18)):
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(120, 110, 105))
d.text((538, 446), "7 BODIES FOUND, ~50 STILL", font=font(BOLD, 24), fill=NAVY)
d.text((538, 474), "MISSING", font=font(BOLD, 24), fill=NAVY)
d.text((538, 504), "Candy factory fire, Cikande, Banten — the", font=font(REG, 15), fill=GREY)
d.text((538, 522), "search goes on a day after the blaze.", font=font(REG, 15), fill=GREY)

# ---------- BRIEFS GRID ----------
d.rectangle([0, 560, W, 590], fill=NAVY2)
d.text((24, 565), "AROUND THE WORLD  —  SUNDAY 22 NOVEMBER", font=font(BOLD, 20), fill=WHITE)
d.text((760, 566), "EACH STORY, ONE LINE", font=font(BOLD, 15), fill=GOLD)

TAG_COLOR = {"EUROPE": NAVY2, "MIDEAST": (140, 40, 40), "ASIA": TEAL,
             "S. ASIA": (120, 70, 10), "OCEANIA": (20, 90, 90),
             "N. AMERICA": (90, 30, 90), "AFRICA": (110, 70, 0)}
briefs = [
    ("EUROPE", "Man Utd win 2-1 at Anfield — Maguire 84'"),
    ("EUROPE", "Zverev v Alcaraz, Turin final 18:00 CET"),
    ("EUROPE", "France: 4th weekend of cost protests"),
    ("MIDEAST", "Tanker hit by projectile in Hormuz"),
    ("MIDEAST", "Gaza aid call after floods"),
    ("MIDEAST", "Iraqi troops enter militia base"),
    ("EUROPE", "Russian ship still burning off Finland"),
    ("ASIA", "Seoul minister quits over AI cheating"),
    ("ASIA", "S. Korea readies market rescue funds"),
    ("S. ASIA", "Nepal PM Shah lands in India"),
    ("OCEANIA", "India 720/9, lead New Zealand by 352"),
    ("S. ASIA", "Chahal joins BJP; MP Wadkute dies, 72"),
    ("OCEANIA", "Australia hits back at US over AUKUS"),
    ("N. AMERICA", "Verstappen wins Las Vegas GP"),
    ("N. AMERICA", "Miley Cyrus weds in California"),
    ("N. AMERICA", "US report: $12bn Venezuela oil cash"),
    ("AFRICA", "Nigeria boat sinks, 24 dead"),
    ("AFRICA", "S. Africa mourns Mlambo-Ngcuka, 71"),
]
for i, (tag, text) in enumerate(briefs):
    col = i % 2
    row = i // 2
    x0 = 24 + col * 500
    y0 = 600 + row * 29
    d.rectangle([x0, y0 + 4, x0 + 10, y0 + 14], fill=TAG_COLOR[tag])
    d.text((x0 + 16, y0), tag, font=font(BOLD, 15), fill=TAG_COLOR[tag])
    tw = d.textlength(tag, font=font(BOLD, 15))
    d.text((x0 + 16 + tw + 8, y0), text, font=font(BOLD, 17), fill=INK)

# ---------- TIMELINE ----------
d.rectangle([0, 866, W, 922], fill=(233, 226, 208))
d.text((24, 872), "THROUGH THE DAY (UTC)", font=font(BOLD, 15), fill=NAVY)
slots = [
    ("OVERNIGHT", "Verstappen wins Las Vegas GP"),
    ("MORNING", "COP31 draft lands in Antalya"),
    ("AFTERNOON", "Man Utd 2-1 at Anfield"),
    ("EVENING", "Turin final: Zverev v Alcaraz"),
]
for i, (lab, txt) in enumerate(slots):
    x0 = 24 + i * 250
    d.text((x0, 892), lab, font=font(BOLD, 14), fill=RED)
    d.text((x0, 908), txt, font=font(REG, 14), fill=INK)

# ---------- DATE-CHECK STRIP ----------
d.rectangle([0, 926, W, 980], fill=(250, 230, 225))
d.text((24, 932), "DATE-CHECKED — NOT FROM TODAY (first reported earlier):",
       font=font(BOLD, 15), fill=RED)
dc = ("Shenzhen summit 19 Nov  ·  Rohingya ruling 19 Nov  ·  US stocks slide 20 Nov  ·  "
      "Riemann claim 20 Nov  ·  El Chapo Isidro held 21 Nov  ·  Bahrain strikes 21 Nov  ·  "
      "BepiColombo at Mercury 21 Nov  ·  EU–Indonesia deal signed 21 Nov")
for j, ln in enumerate(wrap(d, dc, font(REG, 14), 976)):
    d.text((24, 951 + j * 16), ln, font=font(REG, 14), fill=INK)

# ---------- SOURCES ----------
d.text((24, 988), "Sources checked 22 Nov 2026: Reuters · AP · BBC · AFP · Al Jazeera · The Guardian ·",
       font=font(REG, 14), fill=GREY)
d.text((24, 1004), "F1.com · ATP Tour · One Turn · Cognoscere — every story happened or was first reported on this day.",
       font=font(REG, 14), fill=GREY)

img.save(os.path.join(HERE, "entry.png"), optimize=True)
print("saved", os.path.join(HERE, "entry.png"))
