#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageOps

background = Image.open("result.jpg")
im = Image.open("b.jpg")
background.convert('RGBA')
im.convert('RGBA')

bg = Image.new("RGBA", (background.size[0] * 3, background.size[1]), (255,255,255, 255))
for x in xrange(0,3):
	bg.paste(background, (x * background.size[0], 0))

# width=190
# ratio = float(width)/im.size[0]
# height = int(im.size[1]*ratio)
# nim = im.resize( (width, height), Image.BILINEAR )

mask = Image.open('mask.png').convert('L')
nim = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
nim.putalpha(mask)
bg.paste(nim, (55, 140), nim)

bg.save("a.jpg")
