#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageOps, ImageDraw, ImageFont
font = ImageFont.truetype( "/Users/johnnysung/Library/Fonts/NotoSansCJKtc-Bold.otf", 65 )
font2 = ImageFont.truetype( "/Users/johnnysung/Library/Fonts/NotoSansCJKtc-Bold.otf", 45 )

background = Image.open("bg.png")
background.convert('RGBA')
bg = Image.new("RGBA", background.size, (255,255,255,255))

bg.paste(background, (0, 0))

def drawRoundPic(im, xy):
	im.convert('RGBA')
	mask = Image.open('mask.png').convert('L')
	nim = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
	nim.putalpha(mask)
	bg.paste(nim, xy, nim)

def drawCenterText(msg, xy, wh=(300,50)):
	draw.textsize(msg, font=font2)
	fsize = font2.getsize( msg )
	draw.text(((wh[0] - fsize[0])/2 + xy[0],(wh[1]-fsize[1])/2 + xy[1]), msg, font=font2, fill="black")

im = Image.open("images/1.jpg")
drawRoundPic(im, (89, 171))

im = Image.open("images/2.jpg")
drawRoundPic(im, (609, 171))

draw = ImageDraw.Draw( bg )
deepBlue = (0,62,142)
draw.text( (430, 282), u"加上", font=font, fill=deepBlue )
draw.text( (928, 282), u"好棒棒", font=font, fill=deepBlue )

drawCenterText(u"芥末蛋糕", (85,480))
drawCenterText(u"芥末蛋糕", (608,480))

bg.save("a.jpg")
