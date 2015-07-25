#!/usr/bin/python
# -*- coding: utf-8 -*-

import Image, ImageDraw, ImageFont
font = ImageFont.truetype( "/Users/johnnysung/Library/Fonts/NotoSansCJKtc-Bold.otf", 24 )
im = Image.new( "RGB", (400,300) )
draw = ImageDraw.Draw( im )
draw.text( (20,20), u"好棒棒", font=font )
im.save( "text.jpg" )