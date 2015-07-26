#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageOps, ImageDraw, ImageFont
import json
from random import choice as rchoice

font = ImageFont.truetype( "/Users/johnnysung/Library/Fonts/NotoSansCJKtc-Bold.otf", 65 )
font2 = ImageFont.truetype( "/Users/johnnysung/Library/Fonts/NotoSansCJKtc-Bold.otf", 45 )

def generateImg(data, pos1, pos2):
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

	im = Image.open("images/"+str(pos1+1)+".jpg")
	drawRoundPic(im, (89, 171))

	im = Image.open("images/"+str(pos2+1)+".jpg")
	drawRoundPic(im, (609, 171))

	draw = ImageDraw.Draw( bg )
	deepBlue = (0,62,142)
	draw.text( (430, 282), u"加上", font=font, fill=deepBlue )
	draw.text( (928, 282), u"好棒棒", font=font, fill=deepBlue )

	drawCenterText(data[pos1]['name'], (85,480))
	drawCenterText(data[pos2]['name'], (608,480))
	return bg


jsonData=u'[{"name":"鰹魚調味料","promo":"該品牌單筆指定品滿150送15現金紅利","url":"http://www.savesafe.com.tw/Products/ProductView.aspx?s_id=f9897fe9bacfb5f718bf711e7a1d738b"},{"name":"靠得住","promo":"大促銷$149元","url":"http://www.savesafe.com.tw/Products/ProductView.aspx?s_id=bf19a2a50bb1208b257ac4c6fd5c91c0"},{"name":"100%純橄欖油","promo":"","url":"http://www.savesafe.com.tw/Products/ProductView.aspx?t_s_id=43013&s_id=717123634b662e150798d4667d3c6047"},{"name":"青蔥蘇打餅乾","promo":"","url":"http://www.savesafe.com.tw/Products/ProductView.aspx?t_s_id=41592&s_id=4266242f39cfc67bda72e62f7e050b92"},{"name":"堅果山核桃","promo":"熱賣商品","url":""},{"name":"鮮奶油","promo":"熱賣商品","url":""},{"name":"紅燒鰻","promo":"","url":"http://www.savesafe.com.tw/Products/ProductView.aspx?s_id=9684a1353c4b44f0342ac73cf2da1d46"}]'
words=[u'加上', u'混合', u'搭配']
words2=[u'好棒棒', u'好厲害', u'猴塞雷', u'好有事', u'搖一搖', u'好壞壞', u'真好人', u'好勵志', u'就甘心']

data=json.loads(jsonData)
rset=range(0, len(data))

mylist = range(len(data))
res=0
while mylist:
    choice1 = rchoice(mylist)
    mylist.remove(choice1)
    if mylist:
	    choice2 = rchoice(mylist)
	    mylist.remove(choice2)
	    img = generateImg(data, choice1, choice2)
	    res+=1
	    img.save("result/r"+str(res)+".jpg")

