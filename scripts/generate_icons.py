
import os
from PIL import Image, ImageDraw

# Design System colors
TERRACOTTA = (147, 68, 26)  # #93441A
TAUPE = (182, 115, 50)      # #B67332
GOLD = (218, 171, 58)       # #DAAB3A
WHITE = (255, 255, 255)
CREAM = (229, 231, 230)     # #E5E7E6

OUTPUT_DIR = r"c:\Users\Loris\Documents\bricoloc\maelJtm\assets\icons2"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_base_img(size=512):
    return Image.new("RGBA", (size, size), (255, 255, 255, 0))

def save(img, name):
    path = os.path.join(OUTPUT_DIR, f"{name}.png")
    img.save(path)
    print(f"Saved: {path}")

# 1. Cloud
img = create_base_img()
draw = ImageDraw.Draw(img)
# Simple cloud shape (connected circles)
draw.ellipse([100, 200, 250, 350], fill=TERRACOTTA)
draw.ellipse([180, 150, 380, 350], fill=TERRACOTTA)
draw.ellipse([300, 220, 450, 350], fill=TERRACOTTA)
draw.rectangle([175, 250, 375, 350], fill=TERRACOTTA)
save(img, "cloud")

# 2. Server
img = create_base_img()
draw = ImageDraw.Draw(img)
draw.rounded_rectangle([100, 100, 412, 412], radius=20, fill=TERRACOTTA)
# Lines for rack
for i in range(3):
    y = 150 + i * 100
    draw.line([150, y, 362, y], fill=WHITE, width=15)
    draw.ellipse([380, y-10, 400, y+10], fill=GOLD)
save(img, "server")

# 3. Security (Shield)
img = create_base_img()
draw = ImageDraw.Draw(img)
points = [(256, 50), (450, 150), (400, 400), (256, 480), (112, 400), (62, 150)]
draw.polygon(points, fill=TERRACOTTA)
save(img, "security")

# 4. Gear
img = create_base_img()
draw = ImageDraw.Draw(img)
# Simple cog (circle with teeth)
draw.ellipse([150, 150, 362, 362], fill=TAUPE)
for i in range(8):
    # Just a trick to draw teeth without complex math since I'm a generator
    draw.ellipse([256-40, 50, 256+40, 130], fill=TAUPE) # Top one
    img = img.rotate(45, resample=Image.BICUBIC, center=(256, 256))
    draw = ImageDraw.Draw(img)
draw.ellipse([216, 216, 296, 296], fill=(255,255,255,0)) # Hole
save(img, "gear")

# 5. Message
img = create_base_img()
draw = ImageDraw.Draw(img)
draw.rounded_rectangle([50, 100, 462, 350], radius=40, fill=GOLD)
draw.polygon([(100, 350), (150, 450), (200, 350)], fill=GOLD)
save(img, "message")

# 6. Cart
img = create_base_img()
draw = ImageDraw.Draw(img)
draw.line([100, 100, 150, 100, 200, 350, 450, 350], fill=TERRACOTTA, width=20)
draw.rectangle([180, 150, 420, 300], fill=TERRACOTTA)
draw.ellipse([200, 380, 240, 420], fill=TERRACOTTA)
draw.ellipse([380, 380, 420, 420], fill=TERRACOTTA)
save(img, "cart")

# 7. Stock (Box)
img = create_base_img()
draw = ImageDraw.Draw(img)
# Cube-ish
draw.polygon([(256, 100), (450, 200), (450, 400), (256, 500), (62, 400), (62, 200)], fill=TAUPE)
draw.line([256, 100, 256, 500], fill=WHITE, width=5)
draw.line([256, 300, 450, 200], fill=WHITE, width=5)
draw.line([256, 300, 62, 200], fill=WHITE, width=5)
save(img, "stock")

# 8. Globe
img = create_base_img()
draw = ImageDraw.Draw(img)
draw.ellipse([50, 50, 462, 462], fill=GOLD)
draw.arc([50, 50, 462, 462], 0, 360, fill=WHITE, width=5)
draw.line([256, 50, 256, 462], fill=WHITE, width=5)
draw.line([50, 256, 462, 256], fill=WHITE, width=5)
save(img, "globe")

# 9. Database
img = create_base_img()
draw = ImageDraw.Draw(img)
draw.ellipse([150, 50, 362, 150], fill=TERRACOTTA)
draw.rectangle([150, 100, 362, 400], fill=TERRACOTTA)
draw.ellipse([150, 350, 362, 450], fill=TERRACOTTA)
save(img, "database")

# 10. User
img = create_base_img()
draw = ImageDraw.Draw(img)
draw.ellipse([206, 50, 306, 150], fill=TERRACOTTA)
draw.chord([100, 180, 412, 500], 180, 0, fill=TERRACOTTA)
save(img, "user")
