#!/usr/bin/python

#############################################
# Claim Prize Python Script
# Designed and Written by Salvador Melendez
#############################################

from Tkinter import *
import threading
import time
import random
import os
import sys
from subprocess import check_output
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

sounds_path = '/home/pi/sounds/'
event = 'AFC CCAA'
activity = 0
prize = 0
winner = 0
pointer_file = "/home/pi/pointer.txt"
with open(pointer_file, "r") as pfile:
    for i, line in enumerate(pfile):
        winner = int(line)
fig_color = [red, green, blue, white, yellow]
u_codes = {}
s_careers = {}
p_user = {}
p_pin = {}
p_year = {}
p_movie = {}
p_country = {}
p_color = {}
p_password = {}

def initial_setup():
    global winner
    os.system('clear')
    with open('/home/pi/Documents/raw/unique_codes.txt', 'r') as uc:
        for i, line in enumerate(uc):
           u_codes[i] = line.rstrip('\n')
    if(winner >= len(u_codes)):
        with open(pointer_file, "w+") as pfile:
            pfile.write('0')
        winner = 0
    with open('/home/pi/original_files/decoding.txt', 'r') as sc:
        for i, line in enumerate(sc):
            s_careers[i] = line.rstrip('\n')
    with open('/home/pi/original_files/ecybermission_profiles.txt', 'r') as ep:
        for i, line in enumerate(ep):
            if(i != 0):
                f_input = line.rstrip('\n')
                f_input = f_input.split('\r')
                f_input = f_input[0].split('\t')
                n_input = [x for x in f_input if x != '']
                p_user[i-1] = n_input[0]
                p_pin[i-1] = n_input[1]
                p_year[i-1] = n_input[2]
                p_movie[i-1] = n_input[3]
                p_country[i-1] = n_input[4]
                p_color[i-1] = n_input[5]
                p_password[i-1] = n_input[6]
    msg = 'tput sgr0'
    os.system(msg)

def light_answer(usr_answer):
    if(usr_answer == 1):
        color = (0,255,0)
    else:
        color = (255,0,0)
    flashes = 3
    x = 0
    while(x < flashes):
        for i in range(0,8):
            for j in range(0,8):
                sense.set_pixel(i,j,color)
        time.sleep(0.1)
        sense.clear()
        time.sleep(0.1)
        x=x+1

def initial_banner():
    global activity
    print '\n'
    os.system("echo $(tput bold)Please access the system $(tput setaf 1)AFTER$(tput sgr0)$(tput bold) you complete the $(tput setaf 3)Dumpster Diving$(tput sgr0)$(tput bold) Activity$(tput sgr0)$(tput bold) OR the $(tput setaf 3)Decoding$(tput sgr0)$(tput bold) Activity$(tput sgr0)")
    msg = 'tput setaf 4'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    msg = 'bash -c \'echo -ne "\n**********"\''
    os.system(msg)
    msg = 'tput setaf 2'
    os.system(msg)
    msg = 'bash -c \'echo -ne "SYSTEM ACCESS"\''
    os.system(msg)
    msg = 'tput setaf 4'
    os.system(msg)
    msg = 'bash -c \'echo -ne "**********\n\n"\''
    os.system(msg)
    msg = 'tput sgr0'
    os.system(msg)
    lock_activity = 1
    while(lock_activity):
	os.system("echo $(tput setaf 5)$(tput bold)What activity have you completed?$(tput sgr0)")
    	print '[1] Dumpster Diving'
    	print '[2] Decoding'
    	activity = raw_input('Type 1 for Dumpster Diving or 2 for Decoding: ')
	if(activity == '1' or activity == '2'):
		lock_activity = 0
	else:
		os.system("echo $(tput setaf 1)$(tput bold)Invalid Activity Number... Try again!$(tput sgr0)")
		print '\n'

def decoding():
    global prize
    print '\n'
    lock_answer1 = 1
    lock_answer2 = 1
    lock_answer3 = 1
    lock_answer4 = 1
    lock_answer5 = 1
    lock_answer6 = 1
    lock_answer7 = 1
    lock_answer8 = 1
    lock_answer9 = 1
    lock_answer10 = 1
    os.system("echo $(tput setaf 3)$(tput bold)DECODING CHALLENGE$(tput sgr0)")
    os.system("echo $(tput setaf 6)$(tput bold)Please answer the following questions: $(tput sgr0)")
    while(lock_answer1):
	print '\n'
	os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#1 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[0] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer1 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
	    os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer2):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#2 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[1] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer2 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer3):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#3 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[2] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer3 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer4):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#4 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[3] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer4 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer5):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#5 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[4] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer5 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer6):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#6 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[5] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer6 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer7):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#7 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[6] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer7 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer8):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#8 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[7] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer8 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer9):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#9 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[8] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer9 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer10):
	print '\n'
        os.system("echo $(tput bold)What is the $(tput setaf 3)Real Message \#10 $(tput sgr0)$(tput bold)found in the Decoding Worksheet?$(tput sgr0)")
        answer = raw_input()
        answer = answer.lower()
        if(s_careers[9] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer10 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
	    prize = 1
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)


def dumpsterdiving():
    global prize
    print '\n'
    lock_login = 1
    lock_answer1 = 1
    lock_answer2 = 1
    lock_answer3 = 1
    lock_answer4 = 1
    lock_answer5 = 1
    os.system("echo $(tput setaf 3)$(tput bold)DUMPSTER DIVING CHALLENGE$(tput sgr0)")
    os.system("echo $(tput setaf 6)$(tput bold)Please answer the following questions: $(tput sgr0)")
    while(lock_login):
	print '\n'
	c_user = -1
        while(lock_answer1):
            answer = raw_input('Username: ')
            answer = answer.lower()
            for i in p_user:
                if(p_user[i] == answer):
                    c_user = i
                    lock_answer1 = 0
                    num_attempts = 3
            if(c_user == -1):
		os.system("echo $(tput setaf 1)Invalid Username. Please try again...$(tput sgr0)")
		print '\n'
        while(lock_answer2 and num_attempts != 0):
            answer = raw_input('PIN: ')
            if(p_pin[c_user] == answer):
                msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
                os.system(msg)
                lock_answer2 = 0
                lock_login = 0
            else:
                num_attempts-=1
                if(num_attempts == 0):
		    os.system("echo $(tput setaf 1)Invalid PIN. You must start over or try another username!$(tput sgr0)")
                    c_user = -1
                    lock_answer1 = 1
                else:
                    if(num_attempts == 1):
			msg = 'tput setaf 1'
		        os.system(msg)
            		msg = 'bash -c \'echo -ne Invalid PIN. Please try again... "' + str(num_attempts) + ' attempt left!\n"\''
            		os.system(msg)
			msg = 'tput sgr0'
		        os.system(msg)
                    else:
			msg = 'tput setaf 1'
		        os.system(msg)
            		msg = 'bash -c \'echo -ne Invalid PIN. Please try again... "' + str(num_attempts) + ' attempt left!\n"\''
            		os.system(msg)
			msg = 'tput sgr0'
		        os.system(msg)
    print '\n'
    msg = 'tput setaf 1'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    msg = 'bash -c \'for i in {1..3}; do echo -ne "Connecting to server   \\r"; sleep 0.3; echo -ne "Connecting to server.\\r"; sleep 0.3; echo -ne "Connecting to server..\\r"; sleep 0.3; echo -ne "Connecting to server...\\r"; sleep 0.3; done\''
    os.system(msg)
    msg = 'Connecting to server...'
    print msg
    msg = 'tput setaf 1'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    msg = 'bash -c \'for i in {1..3}; do echo -ne "Waiting for response   \\r"; sleep 0.3; echo -ne "Waiting for response.\\r"; sleep 0.3; echo -ne "Waiting for response..\\r"; sleep 0.3; echo -ne "Waiting for response...\\r"; sleep 0.3; done\''
    os.system(msg)
    msg = 'tput sgr0'
    os.system(msg)
    os.system("echo $(tput setaf 3)$(tput bold)'\n\n'Congratulations!!!$(tput sgr0)$(tput bold) You have access to the $(tput setaf 1)Hacking System$(tput sgr0)$(tput bold). To claim a prize, please answer the following questions:$(tput sgr0)")
    time.sleep(1)
    sense.clear()
    while(lock_answer3):
        answer = raw_input('\nWhat is my favorite movie?\n')
        answer = answer.lower()
        if(p_movie[c_user] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer3 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer4):
        answer = raw_input('\nIn what year I was born?\n')
        answer = answer.lower()
        if(p_year[c_user] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer4 = 0
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
            image1(p_color[c_user])
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
    while(lock_answer5):
        answer = raw_input('\nWhat is the color of the ghost? (Hint: see SenseHat)\n')
        answer = answer.lower()
        if(p_color[c_user] == answer):
            msg = 'omxplayer -o both ' + sounds_path + '1_up.mp3 > log &'
            os.system(msg)
            lock_answer5 = 0
            sense.clear()
	    os.system("echo $(tput setaf 2)You are right!!!$(tput sgr0)")
            light_answer(1)
	    prize = 1
        else:
            os.system("echo $(tput setaf 1)Wrong answer. Please try again...$(tput sgr0)")
            light_answer(0)
            image1(p_color[c_user])

def draw_figure():
    image0()

def welcome():
    msg = 'figlet -f isometric2 \'' + event + '\' | lolcat -a -d 3 -F 5'
    os.system(msg)

#happy_face - image0
def image0():
    sense.clear()
    color = random.choice(fig_color)
    #column 1
    sense.set_pixel(0,5,color)
    #column 2
    sense.set_pixel(1,6,color)
    #column 3
    sense.set_pixel(2,1,color)
    sense.set_pixel(2,2,color)
    sense.set_pixel(2,3,color)
    sense.set_pixel(2,7,color)
    #column 4
    sense.set_pixel(3,7,color)
    #column 5
    sense.set_pixel(4,7,color)
    #column 6
    sense.set_pixel(5,1,color)
    sense.set_pixel(5,2,color)
    sense.set_pixel(5,3,color)
    sense.set_pixel(5,7,color)
    #column 7
    sense.set_pixel(6,6,color)
    #column 8
    sense.set_pixel(7,5,color)

#ghost - image1
def image1(u_color):
    sense.clear()
    if(u_color == 'red'):
        color = red
    elif(u_color == 'green'):
        color = green
    elif(u_color == 'blue'):
        color = blue
    elif(u_color == 'yellow'):
        color = yellow
    else:
        color = white
    #color = random.choice(fig_color)
    #column 1
    sense.set_pixel(0,2,color)
    sense.set_pixel(0,3,color)
    sense.set_pixel(0,4,color)
    sense.set_pixel(0,5,color)
    sense.set_pixel(0,6,color)
    sense.set_pixel(0,7,color)
    #column 2
    sense.set_pixel(1,1,color)
    sense.set_pixel(1,2,color)
    sense.set_pixel(1,3,color)
    sense.set_pixel(1,5,color)
    sense.set_pixel(1,6,color)
    #column 3
    sense.set_pixel(2,0,color)
    sense.set_pixel(2,1,color)
    sense.set_pixel(2,2,color)
    sense.set_pixel(2,5,color)
    sense.set_pixel(2,6,color)
    sense.set_pixel(2,7,color)
    #column 4
    sense.set_pixel(3,0,color)
    sense.set_pixel(3,1,color)
    sense.set_pixel(3,2,color)
    sense.set_pixel(3,3,color)
    sense.set_pixel(3,4,color)
    sense.set_pixel(3,5,color)
    sense.set_pixel(3,6,color)
    #column 5
    sense.set_pixel(4,0,color)
    sense.set_pixel(4,1,color)
    sense.set_pixel(4,2,color)
    sense.set_pixel(4,3,color)
    sense.set_pixel(4,4,color)
    sense.set_pixel(4,5,color)
    sense.set_pixel(4,6,color)
    #column 6
    sense.set_pixel(5,0,color)
    sense.set_pixel(5,1,color)
    sense.set_pixel(5,2,color)
    sense.set_pixel(5,3,color)
    sense.set_pixel(5,5,color)
    sense.set_pixel(5,6,color)
    sense.set_pixel(5,7,color)
    #column 7
    sense.set_pixel(6,1,color)
    sense.set_pixel(6,2,color)
    sense.set_pixel(6,5,color)
    sense.set_pixel(6,6,color)
    #column 8
    sense.set_pixel(7,2,color)
    sense.set_pixel(7,3,color)
    sense.set_pixel(7,4,color)
    sense.set_pixel(7,5,color)
    sense.set_pixel(7,6,color)
    sense.set_pixel(7,7,color)

    
while True:
	initial_setup()
	initial_banner()
	if(activity == '1'):
		dumpsterdiving()
	elif(activity == '2'):
		decoding()
	else:
		print 'Please complete an activity!'
	if(prize == 1):
		print '\n'
		os.system("echo $(tput bold)$(tput setaf 3)Congratulations!!!$(tput sgr0)$(tput bold) Your UNIQUE CODE is:")
		print '\n'
		msg = 'tput setaf 2'
		os.system(msg)
		print u_codes[winner]
		print '\n'
		winner=winner+1
                with open(pointer_file, "w+") as pfile:
                    pfile.write(str(winner))
                prize = 0
	else:
		print 'NO Prize.'
	os.system("echo $(tput setaf 1)Write down your UNIQUE CODE and press ENTER to finish...$(tput sgr0)")
	raw_input()
	os.system('clear')
