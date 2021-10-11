#!/usr/bin/python

#############################################
# Cheating MITM Python Script
# Designed and Written by Salvador Melendez
#############################################

import os
import sys

key = ''
pwd = ''
with open('/home/pi/Documents/raw/key.txt', 'r') as pw:
    for i, line in enumerate(pw):
        pwd = line.rstrip('\n')

if(len(sys.argv)>1):
	key = sys.argv[1]

if(key == pwd):
	os.system('/home/pi/config_gems.py 192.168.11.1')
	if os.path.isfile('/home/pi/Desktop/traffic.py'):
		instr = 'mv /home/pi/Desktop/traffic.py /home/pi/Desktop/YOUR_traffic.py'
		os.system(instr)
	instr = 'chmod +x /home/pi/original_files/traffic.py'
	os.system(instr)
	instr = 'cp /home/pi/original_files/traffic.py /home/pi/Desktop/'
	os.system(instr)
	if os.path.isfile('/home/pi/Desktop/YOUR_traffic.py'):
		instr = 'diff /home/pi/Desktop/traffic.py /home/pi/Desktop/YOUR_traffic.py'
		os.system(instr)
