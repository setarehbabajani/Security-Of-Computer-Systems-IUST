from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    original_image = Image.open(input_image_path).convert("RGBA")
    new_image = Image.new("RGB", original_image.size, (255, 255, 255))
    new_image.paste(original_image, (0, 0), original_image)
    font = ImageFont.truetype("arial.ttf", 36)
    d = ImageDraw.Draw(new_image)
    textwidth, textheight = d.textsize(watermark_text, font)
    width, height = new_image.size
    x = (width - textwidth) // 4
    y = (height - textheight) // 10
    d.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
    new_image.save(output_image_path, "JPEG")

input_image_path = "input.png" 
output_image_path = "output.jpg" 
watermark_text = "IUST watermark"
add_watermark(input_image_path, output_image_path, watermark_text)
