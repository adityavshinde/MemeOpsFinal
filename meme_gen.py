from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
from io import BytesIO

# ✅ Drake Meme Template (online)
DRAKE_TEMPLATE_URL = "https://i.imgflip.com/30b1gx.jpg"  # Drake Format

# ✅ Download image from URL
def download_template(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# ✅ Draw text on image
def add_captions(img, top_text, bottom_text):
    draw = ImageDraw.Draw(img)
    width, height = img.size

    try:
        font = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 60)
    except:
        font = ImageFont.load_default()

    def wrap_text(text, max_width):
        lines = []
        words = text.split()
        line = ""
        for word in words:
            test_line = line + word + " "
            w, _ = draw.textbbox((0, 0), test_line, font=font)[2:]
            if w > max_width:
                lines.append(line.rstrip())
                line = word + " "
            else:
                line = test_line
        lines.append(line.rstrip())
        return lines

    def draw_wrapped_text(text, y_start):
        max_width = width // 2 - 40  # only right half
        x_offset = width // 2 + 20

        lines = []
        for part in text.split('\n'):
            lines.extend(wrap_text(part, max_width))

        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = x_offset + (max_width - text_width) // 2
            y = y_start + i * (text_height + 10)
            outline_range = 2
            for ox in range(-outline_range, outline_range + 1):
                for oy in range(-outline_range, outline_range + 1):
                    draw.text((x + ox, y + oy), line, font=font, fill="black")
            draw.text((x, y), line, font=font, fill="gray")

    draw_wrapped_text(top_text, 40)
    draw_wrapped_text(bottom_text, height // 2 + 40)

    return img



# ✅ Main meme generator
def generate_drake_meme(title, output_filename="generated_drake_meme.jpg"):
    lowered = title.lower()

    # Smart split keywords
    separators = [
        " but ",
        " instead of ",
        " vs ",
        " versus ",
        " rather than ",
        " not ",
        " don't ",
        ", then "
    ]

    top_text = bottom_text = ""

    for sep in separators:
        if sep in lowered:
            parts = title.split(sep, 1)
            if len(parts) == 2:
                top_text = parts[0].strip()
                bottom_text = parts[1].strip()
                break

    # Fallback split (just in case)
    if not top_text or not bottom_text:
        words = title.strip().split()
        midpoint = len(words) // 2
        top_text = " ".join(words[:midpoint])
        bottom_text = " ".join(words[midpoint:])

    print("🔺 Top:", top_text)
    print("🔻 Bottom:", bottom_text)

    img = download_template(DRAKE_TEMPLATE_URL)
    img = add_captions(img, top_text, bottom_text)
    img.save(output_filename)
    print(f"✅ Meme saved as '{output_filename}'")

# ✅ Run directly
if __name__ == "__main__":
    # 💬 You can change this to Reddit title later
    test_title = "When you debug for 3 hours and realize it was a missing semicolon"
    generate_drake_meme(test_title)
