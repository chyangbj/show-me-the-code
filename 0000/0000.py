__author__ = 'chenyang'
from PIL import Image, ImageDraw, ImageFont

im = Image.open('1.jpeg')

x,y = im.size
text = str(5)
fill = (255,0,0)
font = ImageFont.truetype('arial.ttf', 30)

draw = ImageDraw.Draw(im)
draw.text((x-20,5),text,fill,font)

im.save('2.jpg')
