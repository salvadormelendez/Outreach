#!/usr/bin/python
import os
import sys
import time
import subprocess
sys.path.insert(0, '/home/pi')
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
sense.clear()
time.sleep(2)

colors = [(255,255,255), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255), (255,0,255), (255,125,0), (0,255,125), (125,0,255), (125,255,0), (0,125,255), (255,0,125)]
line_counter = -1
row = 0
color = 0

while True:
    time.sleep(0.2)
    line_counter += 1
    col = line_counter%8
    print '(' + str(row) + ',' + str(col) + ')'
    sense.set_pixel(col,row,colors[color])
    if col == 7:
        row += 1
        if row > 7:
            row = 0
            color += 1
            if color >= len(colors):
                color = 0