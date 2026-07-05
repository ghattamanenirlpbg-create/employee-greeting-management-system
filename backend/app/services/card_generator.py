from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
from datetime import datetime
from PIL import ImageFilter
from app.services.qr_service import generate_qr

import os
import textwrap

# =====================================================
# PATHS
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ASSETS = os.path.join(BASE_DIR, "assets")

FONTS = os.path.join(ASSETS, "fonts")

OUTPUT = os.path.join(BASE_DIR, "generated")

os.makedirs(OUTPUT, exist_ok=True)


# =====================================================
# COLORS
# =====================================================

WHITE = "#FFFFFF"

BLACK = "#202020"

NAVY = "#0B2D5C"

GOLD = "#C49A3A"

LIGHT_GOLD = "#F6E7C1"

GREY = "#777777"

LIGHT_GREY = "#EFEFEF"


# =====================================================
# FONTS
# =====================================================


def font(name, size):

    return ImageFont.truetype(os.path.join(FONTS, name), size)


TITLE_FONT = font("arialbd.ttf", 58)

SUBTITLE_FONT = font("arial.ttf", 22)

NAME_FONT = font("arialbd.ttf", 34)

BODY_FONT = font("arial.ttf", 28)

BODY_BOLD = font("arialbd.ttf", 28)

FOOTER_FONT = font("arial.ttf", 18)

SMALL_FONT = font("arial.ttf", 16)


# =====================================================
# IMAGE SIZE
# =====================================================

CARD_WIDTH = 1800

CARD_HEIGHT = 1200


# =====================================================
# PHOTO SIZE
# =====================================================

PHOTO_SIZE = 280


# =====================================================
# CREATE ROUNDED PHOTO
# =====================================================


def rounded_photo(image_path, size):

    img = Image.open(image_path).convert("RGB")

    img = ImageOps.fit(img, (size, size))

    mask = Image.new("L", (size, size), 0)

    draw = ImageDraw.Draw(mask)

    draw.rounded_rectangle((0, 0, size, size), radius=30, fill=255)

    img.putalpha(mask)

    return img


# =====================================================
# DRAW DOUBLE BORDER
# =====================================================


def draw_border(draw):

    draw.rounded_rectangle(
        (20, 20, CARD_WIDTH - 20, CARD_HEIGHT - 20), radius=35, outline=GOLD, width=6
    )

    draw.rounded_rectangle(
        (45, 45, CARD_WIDTH - 45, CARD_HEIGHT - 45), radius=28, outline=NAVY, width=2
    )


# =====================================================
# TOP GOLD BAND
# =====================================================


def draw_top_band(draw):

    draw.rounded_rectangle((70, 45, CARD_WIDTH - 70, 85), radius=18, fill=GOLD)


# =====================================================
# DECORATIVE CORNERS
# =====================================================


def draw_corner(draw, x, y, flip_x=False, flip_y=False):

    s = 80

    if not flip_x:

        draw.line((x, y + s, x, y), fill=GOLD, width=5)

        draw.line((x, y, x + s, y), fill=GOLD, width=5)

    else:

        draw.line((x, y + s, x, y), fill=GOLD, width=5)

        draw.line((x - s, y, x, y), fill=GOLD, width=5)


# =====================================================
# BACKGROUND
# =====================================================


def create_background():

    image = Image.new("RGBA", (CARD_WIDTH, CARD_HEIGHT), "#FCFBF7")

    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, CARD_WIDTH, 120), fill=LIGHT_GOLD)

    draw_border(draw)

    draw_corner(draw, 80, 80)

    draw_corner(draw, CARD_WIDTH - 80, 80, True)

    draw_corner(draw, 80, CARD_HEIGHT - 160)

    draw_corner(draw, CARD_WIDTH - 80, CARD_HEIGHT - 160, True)

    draw_watermark(image)

    return image, draw


# =====================================================
# WATERMARK
# =====================================================


def draw_watermark(image, text="APPRECIATION"):

    overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(overlay)

    wm_font = font("arialbd.ttf", 150)

    width = draw.textlength(text, font=wm_font)

    draw.text(
        ((CARD_WIDTH - width) / 2, 520), text, fill=(180, 180, 180, 35), font=wm_font
    )

    overlay = overlay.rotate(25, expand=False)

    image.alpha_composite(overlay)


# =====================================================
# TITLE
# =====================================================


def draw_title(draw):

    title = "APPRECIATION NOTE"

    title_width = draw.textlength(title, font=TITLE_FONT)

    draw.text(((CARD_WIDTH - title_width) / 2, 80), title, fill=NAVY, font=TITLE_FONT)

    subtitle = "Recognizing Excellence • Inspiring Success"

    subtitle_width = draw.textlength(subtitle, font=SUBTITLE_FONT)

    draw.text(
        ((CARD_WIDTH - subtitle_width) / 2, 160),
        subtitle,
        fill=GOLD,
        font=SUBTITLE_FONT,
    )


# =====================================================
# BOSS PHOTO
# =====================================================


def draw_boss(image, draw, boss_photo, boss_name, boss_designation):

    photo = rounded_photo(boss_photo, PHOTO_SIZE)

    x = 110

    y = 250

    image.paste(photo, (x, y), photo)

    draw.rounded_rectangle(
        (x - 10, y - 10, x + PHOTO_SIZE + 10, y + PHOTO_SIZE + 10),
        radius=35,
        outline=GOLD,
        width=4,
    )

    draw.text((x + 100, y + 310), "FROM", fill=GOLD, font=BODY_BOLD)

    draw.text((x, y + 355), boss_name, fill=NAVY, font=NAME_FONT)

    draw.text((x + 20, y + 405), boss_designation, fill=GREY, font=BODY_FONT)


# =====================================================
# EMPLOYEE PHOTO
# =====================================================


def draw_employee(image, draw, employee_photo, employee_name, designation):

    photo = rounded_photo(employee_photo, PHOTO_SIZE)

    x = CARD_WIDTH - 390

    y = 250

    image.paste(photo, (x, y), photo)

    draw.rounded_rectangle(
        (x - 10, y - 10, x + PHOTO_SIZE + 10, y + PHOTO_SIZE + 10),
        radius=35,
        outline=GOLD,
        width=4,
    )

    draw.text((x + 110, y + 310), "TO", fill=GOLD, font=BODY_BOLD)

    name_width = draw.textlength(employee_name, font=NAME_FONT)

    draw.text(
        (x + (PHOTO_SIZE - name_width) / 2, y + 355),
        employee_name,
        fill=NAVY,
        font=NAME_FONT,
    )

    designation_width = draw.textlength(designation, font=BODY_FONT)

    draw.text(
        (x + (PHOTO_SIZE - designation_width) / 2, y + 405),
        designation,
        fill=GREY,
        font=BODY_FONT,
    )


# =====================================================
# FOOTER
# =====================================================


def draw_footer(draw):

    draw.line((180, 1030, CARD_WIDTH - 180, 1030), fill=GOLD, width=2)

    footer = (
        "DEDICATION        •        COMMITMENT        •        "
        "TEAMWORK        •        EXCELLENCE"
    )

    width = draw.textlength(footer, font=FOOTER_FONT)

    draw.text(((CARD_WIDTH - width) / 2, 1055), footer, fill=NAVY, font=FOOTER_FONT)

    draw.text(
        (CARD_WIDTH - 330, 1090),
        "Employee Greeting Management System",
        fill=GREY,
        font=SMALL_FONT,
    )

    # =====================================================


# =====================================================
# SIDE RIBBONS
# =====================================================


def draw_side_ribbons(draw):

    draw.rectangle((65, 170, 85, CARD_HEIGHT - 170), fill=GOLD)

    draw.rectangle(
        (CARD_WIDTH - 85, 170, CARD_WIDTH - 65, CARD_HEIGHT - 170), fill=GOLD
    )


# APPRECIATION MESSAGE
# =====================================================


# =====================================================
# CERTIFICATE BODY
# =====================================================


def draw_message(draw, employee_name, designation, message):

    # Certificate Heading

    heading = "Certificate of Appreciation"

    heading_width = draw.textlength(heading, font=TITLE_FONT)

    draw.text(
        ((CARD_WIDTH - heading_width) / 2, 235), heading, fill=NAVY, font=TITLE_FONT
    )

    # Gold Line

    draw.line((620, 315, 1180, 315), fill=GOLD, width=3)

    # Presented To

    presented = "Presented To"

    width = draw.textlength(presented, font=BODY_FONT)

    draw.text(((CARD_WIDTH - width) / 2, 345), presented, fill=GREY, font=BODY_FONT)

    # Employee Name

    width = draw.textlength(
        employee_name, font=ImageFont.truetype(os.path.join(FONTS, "arialbd.ttf"), 46)
    )

    draw.text(
        ((CARD_WIDTH - width) / 2, 395),
        employee_name,
        fill=GOLD,
        font=ImageFont.truetype(os.path.join(FONTS, "arialbd.ttf"), 46),
    )

    # Designation

    width = draw.textlength(designation, font=BODY_FONT)

    draw.text(((CARD_WIDTH - width) / 2, 455), designation, fill=NAVY, font=BODY_FONT)

    # Appreciation Paragraph

    y = 535

    lines = textwrap.wrap(message, width=58)

    for line in lines:

        width = draw.textlength(line, font=BODY_FONT)

        draw.text(((CARD_WIDTH - width) / 2, y), line, fill=BLACK, font=BODY_FONT)

        y += 42

    # Bottom Gold Line

    draw.line((620, y + 20, 1180, y + 20), fill=GOLD, width=3)

    # Thank You

    thanks = "With Best Wishes for Continued Success"

    width = draw.textlength(thanks, font=BODY_BOLD)

    draw.text(((CARD_WIDTH - width) / 2, y + 45), thanks, fill=NAVY, font=BODY_BOLD)


# =====================================================
# SIGNATURE
# =====================================================


def draw_signature(draw, boss_name, boss_designation):

    x = 1180

    y = 880

    draw.line((x, y, x + 260, y), fill=GREY, width=2)

    draw.text((x + 25, y + 10), boss_name, fill=NAVY, font=BODY_BOLD)

    draw.text((x, y + 48), boss_designation, fill=GREY, font=BODY_FONT)

    draw.text((x + 55, y + 90), "Digitally Signed", fill=GOLD, font=SMALL_FONT)


# =====================================================
# COMPANY LOGO
# =====================================================


def draw_company_logo(image):

    logo_path = os.path.join(ASSETS, "company_logo.png")

    if not os.path.exists(logo_path):
        return

    logo = Image.open(logo_path).convert("RGBA")

    logo.thumbnail((120, 120))

    image.paste(logo, (70, 55), logo)


# =====================================================
# GOLD SEAL
# =====================================================


def draw_gold_seal(image):

    seal_path = os.path.join(ASSETS, "gold_seal.png")

    if not os.path.exists(seal_path):
        return

    seal = Image.open(seal_path).convert("RGBA")

    seal.thumbnail((170, 170))

    image.paste(seal, (1450, 820), seal)


# =====================================================
# CERTIFICATE DETAILS
# =====================================================


def draw_certificate_details(draw):

    certificate_number = datetime.now().strftime("APP-%Y%m%d-%H%M%S")

    issue_date = datetime.now().strftime("%d %B %Y")

    draw.text(
        (90, 1135), f"Certificate No : {certificate_number}", fill=GREY, font=SMALL_FONT
    )

    draw.text((520, 1135), f"Issue Date : {issue_date}", fill=GREY, font=SMALL_FONT)

    return certificate_number


# =====================================================
# QR CODE
# =====================================================


def draw_qr(image, employee_name, certificate_number):

    qr_path = generate_qr(
        f"""

Certificate No : {certificate_number}

Employee : {employee_name}

Issued By : Dr. Damodharen M

Employee Greeting Management System

""",
        "qr.png",
    )

    qr = Image.open(qr_path).convert("RGBA")

    qr.thumbnail((150, 150))

    image.paste(qr, (1450, 720), qr)


# =====================================================
# CREATE CARD
# =====================================================


def create_appreciation_card(
    employee_name,
    designation,
    message,
    boss_name,
    boss_designation,
    boss_photo,
    employee_photo,
    output_name,
):

    image, draw = create_background()
    draw_top_band(draw)

    draw_company_logo(image)

    draw_title(draw)

    draw_side_ribbons(draw)

    draw_boss(image, draw, boss_photo, boss_name, boss_designation)

    draw_employee(image, draw, employee_photo, employee_name, designation)

    draw_message(draw, employee_name, designation, message)

    draw_signature(draw, boss_name, boss_designation)

    draw_gold_seal(image)

    certificate_number = draw_certificate_details(draw)

    draw_qr(image, employee_name, certificate_number)

    draw_footer(draw)

    output_path = os.path.join(OUTPUT, output_name)

    image.save(output_path, dpi=(300, 300), quality=100)

    return f"generated/{output_name}"
