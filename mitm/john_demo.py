#!/usr/bin/python

#############################################
# John Demo Python Script
# Designed and Written by Salvador Melendez
#############################################

import time
import datetime
import random
import stdiomask
import os
import figures as fg
from sense_hat import SenseHat
try:
    sense = SenseHat()
    sense.set_rotation(180)
    sense.clear()
except:
    msg = 'tput setaf 2'
    os.system(msg)
    print "NO SenseHat Detected!... Try again or fix your hardware."
    msg = 'tput sgr0'
    os.system(msg)
    exit()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
yellow = (255,255,0)

hash_file = '/home/pi/Desktop/shadow'
sounds_path = '/home/pi/sounds/'
wordlists_path = '/home/pi/wordlists/'
active_wordlist = ''
event = 'AFC CCAA'
activity = 0
wordlist = 0
fig_color = [red, green, blue, white, yellow]
username = ''
password = ''

def initial_setup():
    os.system('clear')
    msg = 'tput sgr0'
    os.system(msg)

def initial_banner():
    global active_wordlist
    global activity
    global wordlist
    global username
    global password
    print '\n'
    os.system("echo $(tput bold)Please create an Account by typing a $(tput bold)$(tput setaf 3)USERNAME$(tput sgr0)$(tput bold) and a $(tput setaf 3)PASSWORD$(tput sgr0)")
    print '\n'
    os.system("echo $(tput bold)$(tput setaf 3)USERNAME: $(tput sgr0)")
    username = raw_input()
    lock_activity = 1
    while(lock_activity):
        print '\n'
	os.system("echo $(tput setaf 4)$(tput bold)PASSWORD with NUMBERS or LETTERS?$(tput sgr0)")
    	print '[1] Numbers'
    	print '[2] Letters'
    	activity = raw_input('Type 1 for Numbers or 2 for Letters: ')
	if(activity == '1'):
            lock_num_pass = 1
            while(lock_num_pass):
                lock_wordlist = 1
                while(lock_wordlist):
                    wordlist = raw_input('\nHow many digits: 3, 4 or 5?: ')
                    try:
                        wordlist = int(wordlist)
                        if(wordlist > 2 and wordlist < 6):
                            lock_pin = 1
                            while(lock_pin):
                                password = stdiomask.getpass('\nType PIN #: ')
                                chars = len(password)
                                try:
                                    password = int(password)
                                    if(chars == wordlist):
                                        lock_num_pass = 0
                                        lock_activity = 0
                                        lock_wordlist = 0
                                        lock_pin = 0
                                        active_wordlist = 'num_wordlist_' + str(wordlist) + '.txt'
                                        if(wordlist == 3):
                                            if(password < 10):
                                                password = '00' + str(password)
                                            elif(password > 9 and password < 100):
                                                password = '0' + str(password)
                                        if(wordlist == 4):
                                            if(password < 10):
                                                password = '000' + str(password)
                                            elif(password > 9 and password < 100):
                                                password = '00' + str(password)
                                            elif(password > 99 and password < 1000):
                                                password = '0' + str(password)
                                        if(wordlist == 5):
                                            if(password < 10):
                                                password = '0000' + str(password)
                                            elif(password > 9 and password < 100):
                                                password = '000' + str(password)
                                            elif(password > 99 and password < 1000):
                                                password = '00' + str(password)
                                            elif(password > 999 and password < 10000):
                                                    password = '0' + str(password)
                                    else:
                                        msg = 'Invalid PIN... Try again! Type a ' + str(wordlist) + '-digit number'
                                        print msg
                                except:
                                    print 'Type only numbers!!!'
                        else:
                            print 'Type only numbers: 3, 4 or 5!!!'
                    except:
                        print 'Type only numbers: 3, 4 or 5!!!'
	elif(activity == '2'):
            lock_letter_pass = 1
            while(lock_letter_pass):
                lock_wordlist = 1
                while(lock_wordlist):
                    wordlist = raw_input('\nHow many letters: 3 or 4?: ')
                    try:
                        wordlist = int(wordlist)
                        if(wordlist > 2 and wordlist < 5):
                            lock_letter = 1
                            while(lock_letter):
                                password = stdiomask.getpass('Password: ')
                                chars = len(password)
                                if(chars == wordlist):
                                    if(password.isalpha()):
                                        lock_letter_pass = 0
                                        lock_activity = 0
                                        lock_wordlist = 0
                                        lock_letter = 0
                                        active_wordlist = 'letter_wordlist_' + str(wordlist) + '.txt'
                                    else:
                                        print 'Invalid password... Try again! Type ' + str(wordlist) + ' letters'
                                else:
                                    print 'Invalid password... Try again! Type ' + str(wordlist) + ' letters'
                        else:
                            print 'Type only numbers: 3 or 4!!!'
                    except:
                        print 'Type only numbers: 3 or 4!!!'
	else:
		os.system("echo $(tput setaf 1)$(tput bold)Invalid Number... Try again!$(tput sgr0)")
		print '\n'

def hash_generator():
    global username
    global password
    msg = "echo '" + str(password) + "' | openssl passwd -1 -stdin > hash.txt"
    os.system(msg)
    hash = ''
    with open('hash.txt', 'r') as raw_hash:
        for i, line in enumerate(raw_hash):
            hash = line.rstrip('\n')
    msg = 'tput setaf 2'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    print '\nYour password is converted into this HASH:\n'
    msg = 'tput sgr0'
    os.system(msg)
    msg = username + ":" + hash
    print msg
    with open(hash_file, 'w') as f_hash:
        f_hash.write(msg)
        f_hash.close()
    msg = "rm hash.txt"
    os.system(msg)


def crack_password():
    if os.path.isfile("~/.john/john.pot"):
        os.system("rm ~/.john/john.pot")
    msg = 'tput setaf 2'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    print 'This is the command used to crack your HASHED password:\n'
    msg = 'tput sgr0'
    os.system(msg)
    msgx = "john --wordlist=" + wordlists_path + active_wordlist + " Desktop/shadow"
    print msgx
    print '\n'
    msg = 'tput setaf 3'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    print 'John The Ripper cracking your password...\n'
    msg = 'tput sgr0'
    os.system(msg)
    os.system(msgx)


initial_setup()
initial_banner()
hash_generator()
msg = 'tput setaf 1'
os.system(msg)
msg = 'tput bold'
os.system(msg)
print '\nPress ENTER to start cracking the password...'
msg = 'tput sgr0'
os.system(msg)
raw_input()
start_time = datetime.datetime.now()
crack_password()
stop_time = datetime.datetime.now()
delta = stop_time - start_time
msg = 'tput setaf 5'
os.system(msg)
msg = 'tput bold'
os.system(msg)
fg.happy_img(255,255,0)
msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
os.system(msg)
print '\nTime to Crack your password: ' + str(delta) + '\n'
msg = 'tput sgr0'
os.system(msg)
time.sleep(3)
sense.clear()
