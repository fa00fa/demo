from PIL import Image, ImageDraw, ImageFont
import random, string


import cv2

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

img = Image.new('RGB', (160, 40), color=random_color())
canvas = ImageDraw.Draw(img)
size = img.size

def random_xy():
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    return (x, y)


font = ImageFont.FreeTypeFont('arial.ttf', size=32)
for x in range(size[0]):
    for y in range(size[1]):
        canvas.point((x,y),fill=random_color())
for i in range(4):
    canvas.line((random_xy(), random_xy()), fill=random_color(), width=2)
    canvas.text((i*40,0),random.choice(string.ascii_letters+string.digits),font=font,fill=random_color())
img.save('vcode.png')
img.show()


