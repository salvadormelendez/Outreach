#!/usr/bin/python

#############################################
# Certificate Generator Python Script
# Designed and Written by Salvador Melendez
#############################################

import datetime
import sys
from PIL import Image, ImageDraw, ImageFont

image = Image.open('/home/pi/Music/certificates/cert_template.jpg')
draw = ImageDraw.Draw(image)

#TEAM NAME
x_axis = 1650
if(len(sys.argv)>1):
    message = sys.argv[1]
name = message
num_chars = len(message)
offset = (x_axis/2)-((num_chars/2)*48)
font = ImageFont.truetype('imposs.ttf', size=80)
(x,y) = (offset,465)
color = 'rgb(0,0,255)'
draw.text((x,y), message, fill=color, font=font)

#PLACE
location_file = '/home/pi/location.txt'
with open(location_file, 'r') as lf:
    for i, line in enumerate(lf):
        location = line.rstrip('\n')
#message = location
message = 'Army Futures Command'
num_chars = len(message)
offset = (x_axis/2)-((num_chars/2)*30)
font = ImageFont.truetype('imposs.ttf', size=50)
(x,y) = (offset,710)
color = 'rgb(0,0,0)'
draw.text((x,y), message, fill=color, font=font)

#DATE
months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
now = datetime.datetime.now()
date = str(now.day) + ' ' + months[now.month] + ' ' + str(now.year)
message = date
num_chars = len(message)
offset = (x_axis/2)-((num_chars/2)*27)
font = ImageFont.truetype('imposs.ttf', size=35)
(x,y) = (offset,760)
color = 'rgb(0,0,0)'
draw.text((x,y), message, fill=color, font=font)

cert_name = '/home/pi/Music/certificates/certs/' + name.replace(' ','_') + '_cert.jpg'
image.save(cert_name)
