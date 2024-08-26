import random
from PIL import Image, ImageDraw, ImageFont

def generate_watermark(image_path, text, font_size=30, num_watermarks=10):
    original_img = Image.open(image_path).convert('RGB')
    width, height = original_img.size
    font = ImageFont.truetype("arial.ttf", font_size)
    draw = ImageDraw.Draw(original_img)

    for _ in range(num_watermarks):
        x = random.randint(0, width - 200)
        y = random.randint(0, height - 50)
        draw.text((x, y), text, fill=(0, 0, 0), font=font)

    original_img.save('watermarked_' + image_path)

def main():
    image_path = input("Enter the path to the image: ")
    watermark_text = input("Enter the text for watermark: ")
    generate_watermark(image_path, watermark_text)

if __name__ == "__main__":
    main()
