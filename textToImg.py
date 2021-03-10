# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
 
def draw_image(new_img, text, show_image=False):
    text = str(text)
    draw = ImageDraw.Draw(new_img)
    img_size = new_img.size
 
    font_size = 40
    fnt = ImageFont.truetype('simsun.ttc', font_size)
    fnt_size = fnt.getsize(text)
    while fnt_size[0] > img_size[0] or fnt_size[0] > img_size[0]:
        font_size -= 5
        fnt = ImageFont.truetype('simsun.ttc', font_size)
        fnt_size = fnt.getsize(text)
 
    x = (img_size[0] - fnt_size[0]) / 2
    y = (img_size[1] - fnt_size[1]) / 2
    draw.text((x, y), text, font=fnt, fill=(0, 0, 0))
 
    if show_image:
        new_img.show()
    del draw

 
def new_image(name, text='default', color=(255, 255, 255), show_image=False):
    new_img = Image.new('RGB', (300, 300), color)
    draw_image(new_img, text, show_image)
    new_img.save('./data2/{0:07d}_orig.png'.format(name))
    del new_img
 
 
def new_image_with_file(fn):
    #66742
    num = 133484
    with open(fn, encoding='utf-8') as f:
        for l in f:
            if len(l) > 1:
                new_image(num, l)
                num = num + 1
            if num > 200000:
                break
            

if '__main__' == __name__:
    
    new_image_with_file('文字.txt')
 
 
