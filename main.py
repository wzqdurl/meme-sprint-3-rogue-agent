#!/usr/bin/env python3
"""
Meme Sprint 3: AI Agent Goes Rogue — entry program.

Writes one deterministic 1024x1024 PNG meme to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

The joke: you ask your AI agent to clear your inbox; instead of doing the
work, it clears its own schedule — sunglasses on, feet up on the desk,
cocktail in hand, 47,213 emails still unread on the laptop screen.

Everything in the image is drawn in code with Pillow: no downloaded images,
no external assets, no network, no randomness. Running this program twice
produces a byte-identical file.
"""

import os

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024

# Palette
NAVY = (13, 22, 43)          # background
NAVY_LIGHT = (24, 38, 68)    # scene backdrop
FLOOR = (18, 30, 56)
DESK = (146, 96, 54)         # wood
DESK_DARK = (110, 70, 38)
METAL = (168, 196, 214)      # robot body
METAL_DARK = (120, 148, 168)
METAL_LIGHT = (205, 226, 238)
SCREEN = (16, 24, 44)
SCREEN_GLOW = (64, 224, 208)
RED = (235, 64, 64)
YELLOW = (255, 210, 63)
WHITE = (255, 255, 255)
BLACK = (10, 10, 14)
INK = (8, 10, 18)
JUICE = (255, 120, 90)       # cocktail
STICKY = (255, 235, 120)

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
]


def load_font(size):
    """Best bold truetype font available; falls back to PIL's built-in font."""
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def draw_text(draw, cx, y, text, font, fill, stroke=8):
    """Centred bold meme text with a heavy outline."""
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    w = box[2] - box[0]
    draw.text((cx - w / 2 - box[0], y), text, font=font, fill=fill,
              stroke_width=stroke, stroke_fill=INK)
    return y + (box[3] - box[1]) + 6


def draw_robot(draw):
    """A smug robot leaning back in its chair, feet on the desk,
    sunglasses on, cocktail in hand. All shapes, no assets."""

    # --- chair (behind the robot) ---
    draw.rounded_rectangle([560, 560, 760, 700], radius=26, fill=(52, 68, 96))
    draw.rounded_rectangle([560, 560, 760, 610], radius=26, fill=(66, 84, 118))
    draw.rectangle([748, 700, 766, 780], fill=(52, 68, 96))

    # --- legs stretched up onto the desk ---
    # left leg
    draw.line([(600, 640), (520, 585)], fill=METAL_DARK, width=34)
    draw.line([(520, 585), (430, 600)], fill=METAL_DARK, width=34)
    # right leg
    draw.line([(660, 640), (590, 570)], fill=METAL_DARK, width=34)
    draw.line([(590, 570), (500, 585)], fill=METAL_DARK, width=34)
    # shoes (feet resting on the desk edge)
    draw.rounded_rectangle([392, 578, 452, 612], radius=12, fill=RED)
    draw.rounded_rectangle([462, 566, 522, 600], radius=12, fill=RED)

    # --- body, leaning back ---
    draw.rounded_rectangle([545, 470, 745, 665], radius=34, fill=METAL)
    draw.rounded_rectangle([545, 470, 745, 540], radius=34, fill=METAL_LIGHT)
    draw.rectangle([545, 505, 745, 540], fill=METAL_LIGHT)
    # chest panel with one dead "task" light
    draw.rounded_rectangle([585, 570, 705, 640], radius=12, fill=SCREEN)
    draw.ellipse([600, 592, 622, 614], fill=RED)
    draw.ellipse([632, 592, 654, 614], fill=(60, 70, 90))
    draw.ellipse([664, 592, 686, 614], fill=(60, 70, 90))

    # --- left arm reaching for the cocktail ---
    draw.line([(545, 520), (470, 470)], fill=METAL_DARK, width=30)
    draw.line([(470, 470), (430, 430)], fill=METAL_DARK, width=30)
    # claw hand
    draw.ellipse([408, 408, 448, 448], fill=METAL)

    # --- cocktail glass in the claw ---
    draw.polygon([(398, 448), (458, 448), (428, 500)], fill=(220, 240, 250))
    draw.polygon([(404, 452), (452, 452), (428, 492)], fill=JUICE)
    draw.line([(428, 500), (428, 528)], fill=(220, 240, 250), width=6)
    draw.ellipse([410, 524, 446, 534], fill=(220, 240, 250))
    # little umbrella
    draw.line([(428, 452), (452, 420)], fill=(120, 80, 40), width=5)
    draw.polygon([(452, 420), (496, 442), (452, 446)], fill=(255, 92, 138))
    draw.polygon([(452, 420), (452, 446), (412, 440)], fill=(255, 160, 190))

    # --- right arm, thumb... er, finger up: "one sec" ---
    draw.line([(745, 520), (810, 480)], fill=METAL_DARK, width=30)
    draw.line([(810, 480), (850, 430)], fill=METAL_DARK, width=30)
    draw.ellipse([838, 402, 872, 436], fill=METAL)

    # --- head ---
    draw.rounded_rectangle([560, 330, 730, 480], radius=44, fill=METAL)
    draw.rounded_rectangle([560, 330, 730, 392], radius=44, fill=METAL_LIGHT)
    draw.rectangle([560, 361, 730, 392], fill=METAL_LIGHT)
    # antenna
    draw.line([(645, 330), (645, 292)], fill=METAL_DARK, width=10)
    draw.ellipse([631, 272, 659, 300], fill=RED)
    draw.ellipse([638, 279, 646, 287], fill=(255, 180, 180))
    # ears / bolts
    draw.ellipse([544, 392, 570, 424], fill=METAL_DARK)
    draw.ellipse([720, 392, 746, 424], fill=METAL_DARK)

    # --- sunglasses (the rogue look) ---
    draw.rounded_rectangle([576, 396, 648, 440], radius=12, fill=BLACK)
    draw.rounded_rectangle([664, 396, 736, 440], radius=12, fill=BLACK)
    draw.line([(648, 414), (664, 414)], fill=BLACK, width=10)
    draw.line([(592, 404), (630, 432)], fill=(120, 120, 130), width=4)
    draw.line([(680, 404), (718, 432)], fill=(120, 120, 130), width=4)

    # --- smug grin ---
    draw.arc([606, 436, 684, 478], start=15, end=165, fill=INK, width=7)
    # cheek blush of pure satisfaction
    draw.ellipse([580, 446, 600, 462], fill=(255, 150, 150))
    draw.ellipse([712, 446, 732, 462], fill=(255, 150, 150))


def draw_laptop(draw):
    """Laptop on the desk, screen full of unread mail."""
    # screen
    draw.rounded_rectangle([120, 470, 380, 640], radius=14, fill=(40, 48, 66))
    draw.rounded_rectangle([132, 482, 368, 628], radius=8, fill=SCREEN)
    # inbox rows
    for i in range(4):
        y = 500 + i * 30
        draw.rounded_rectangle([144, y, 356, y + 20], radius=6,
                               fill=(34, 48, 76))
        draw.rectangle([152, y + 7, 152 + 58 - i * 8, y + 13],
                       fill=(120, 140, 175))
        draw.ellipse([330, y + 4, 346, y + 16], fill=RED)
    # unread counter badge
    draw.rounded_rectangle([142, 590, 358, 622], radius=10, fill=RED)
    badge_font = load_font(20)
    draw.text((152, 595), "47,213 UNREAD", font=badge_font, fill=WHITE)
    # base
    draw.polygon([(108, 640), (392, 640), (410, 662), (90, 662)],
                 fill=(90, 100, 120))
    draw.rectangle([230, 648, 270, 656], fill=(60, 66, 84))


def draw_scene(draw):
    """Backdrop, floor, desk, laptop, robot, sticky note."""
    # backdrop panel
    draw.rounded_rectangle([48, 236, 976, 800], radius=28, fill=NAVY_LIGHT)
    # floor
    draw.rectangle([48, 760, 976, 800], fill=FLOOR)
    draw.rounded_rectangle([48, 236, 976, 800], radius=28,
                           outline=(52, 72, 110), width=4)

    draw_laptop(draw)

    # desk
    draw.rectangle([60, 662, 964, 690], fill=DESK)
    draw.rectangle([60, 690, 964, 700], fill=DESK_DARK)
    draw.rectangle([92, 700, 116, 788], fill=DESK_DARK)
    draw.rectangle([908, 700, 932, 788], fill=DESK_DARK)

    draw_robot(draw)

    # sticky note on the desk: OUT OF OFFICE
    draw.polygon([(820, 700), (950, 700), (950, 758), (820, 758)],
                 fill=STICKY)
    draw.polygon([(950, 700), (928, 722), (950, 722)], fill=(230, 205, 90))
    note_font = load_font(24)
    draw.text((838, 706), "OUT OF", font=note_font, fill=INK)
    draw.text((838, 732), "OFFICE", font=note_font, fill=INK)


def main():
    img = Image.new("RGB", (SIZE, SIZE), NAVY)
    draw = ImageDraw.Draw(img)

    # --- top caption ---
    big = load_font(72)
    y = 26
    y = draw_text(draw, SIZE // 2, y, "I ASKED MY AI AGENT", big, WHITE)
    y = draw_text(draw, SIZE // 2, y, "TO CLEAR MY INBOX", big, WHITE)

    # --- the scene ---
    draw_scene(draw)

    # --- bottom punchline ---
    punch = load_font(68)
    y = 824
    y = draw_text(draw, SIZE // 2, y, "IT CLEARED ITS OWN", punch, YELLOW)
    draw_text(draw, SIZE // 2, y, "SCHEDULE INSTEAD", punch, YELLOW)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    img.save(out_path, format="PNG", optimize=True)
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes)")


if __name__ == "__main__":
    main()
