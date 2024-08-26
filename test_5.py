from PIL import Image, ImageDraw, ImageFont

# Open the image
img = Image.open('E:\BQS\Code\sample_3.jpg')

# Create a drawing context
draw = ImageDraw.Draw(img)

# Define the text to be added
text = "HolyPython.com"

# Define the font
font = ImageFont.truetype('arial.ttf', 82)

# Get the size of the text
text_width, text_height = draw.textlength(text, font=font)

# Get the size of the image
image_width, image_height = img.size

# Calculate the position to center the text horizontally and place it near the bottom
x = (image_width - text_width) / 2
y = image_height - text_height - 300

# Add the text to the image
draw.text((x, y), text, font=font)

# Save the watermarked image
img.save('cake_watermarked.png')


