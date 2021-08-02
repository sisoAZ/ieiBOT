from PIL import Image, ImageDraw, ImageFont

def merge_iei(file, text = None):
    image = Image.open(file)
    bg_image = Image.open('./files/iei.png')

    base = Image.new('RGBA', bg_image.size, (255, 255, 255, 0))
    resize_image = image.resize(size=(428, 546))
    base.paste(resize_image.convert("L"), (142, 142))
    base.paste(bg_image, (0, 0), bg_image)
    resize_image.convert("L")
    if text != None:
        draw = ImageDraw.Draw(base)
        font = ImageFont.truetype("HGRSGU.TTC", size=70)
        draw.text((340, 400), text, fill=(255, 0, 0), font=font, anchor="mm")
    base.save(file, quality=100)
    return file