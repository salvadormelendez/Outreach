#!/usr/bin/python

#############################################
# MITM Python Script
# Designed and Written by Salvador Melendez
#############################################

import os
import sys
import time
import threading
import random
from termios import tcflush, TCIFLUSH
from sense_hat import SenseHat
try:
    sense = SenseHat()
    sense.set_rotation(180)
    sense.clear()
except:
    os.system("echo $(tput setaf 2)NO SenseHat Detected!... Try again or fix your hardware.$(tput sgr0)")
    exit()
import figures as fg

workshop_num = -1
lock_workshop = 1
lock_ip = 1
lock_ifconfig = 1
lock_reboot = 1
total_questions = 10
lock_answer = total_questions
path = ''
path_file = '/home/pi/Documents/path.txt'
with open(path_file, 'r') as pf:
    for i, line in enumerate(pf):
        path = line.rstrip('\n')

event_file = '/home/pi/event.txt'
with open(event_file, 'r') as ev:
    for i, line in enumerate(ev):
        event = line.rstrip('\n')
ip_file = '/home/pi/ip_address'
sounds_path = '/home/pi/sounds/'
mitm_qa = 'mitm_q&a.txt'
ans_file = path + mitm_qa
mitm_questions = {}
mitm_answers = {}
mitm_shuffle = list(range(total_questions))
random.shuffle(mitm_shuffle)
with open(ans_file, 'r') as qa:
    for i, line in enumerate(qa):
        line = line.rstrip('\n')
        f_input = line.rstrip('\n')
        f_input = f_input.split('\r')
        f_input = f_input[0].split('\t')
        n_input = [x for x in f_input if x != '']
        mitm_questions[i] = n_input[0]
        mitm_answers[i] = n_input[1]

def check_code(w_code):
    global workshop_num
    code_flag = 1
    file_workshop_code = path + 'valid_workshop_codes.txt'
    with open(file_workshop_code, 'r') as code_handler:
        for i, line in enumerate(code_handler):
	    f_input = line.rstrip('\n')
            f_input = f_input.split('\r')
            f_input = f_input[0].split('\t')
            if(w_code == f_input[1]):
		workshop_num = int(f_input[0])
		mitm_worksheets = sorted(os.listdir('/home/pi/original_files/worksheets'))
		instr = 'cp /home/pi/original_files/worksheets/' + mitm_worksheets[workshop_num] + ' /home/pi/Desktop/'
                os.system(instr)
                code_flag = 0
		break
    if(code_flag == 0):
        os.system("echo $(tput setaf 2)Workshop Code is Valid!!!$(tput sgr0)")
	return 0
    else:
        os.system("echo $(tput setaf 1)Invalid Workshop Code!... Try again!$(tput sgr0)")
	return 1

def check_ip(user_ip):
    ip_flag = 1
    file_ip_address = path + 'valid_ip_addressses.txt'
    with open(file_ip_address, 'r') as ip_handler:
        for i, line in enumerate(ip_handler):
            line = line.rstrip('\n')
            if(user_ip == line):
                ip_flag = 0
		break
    if(ip_flag == 0):
        with open(ip_file, "w") as ipf:
            ipf.write(ip_address)
	os.system('ifconfig eth0 ' + str(ip_address))
	os.system('/home/pi/config_gems.py ' + str(ip_address))
	return 0
    else:
        os.system("echo $(tput setaf 1)Invalid IP address!... Try again!$(tput sgr0)")
	return 1

def sound_answer(usr_answer):
    sounds = ['terrible_shot', 'yes', 'heating_up', 'on_fire', 'boom_shakalaka']
    if(usr_answer == 1):
        msg = 'omxplayer -o both ' + sounds_path + sounds[random.choice(range(1,5))] +'.mp3 > log &'
    else:
        msg = 'omxplayer -o both ' + sounds_path + sounds[0] +'.mp3 > log &'
    os.system(msg)

def light_answer(usr_answer, img_lock):
    if(usr_answer == 1):
        color = (0,255,0)
    else:
        color = (255,0,0)
    flashes = 18
    x = 0
    while(x < flashes):
        for i in range(0,8):
            for j in range(0,8):
                sense.set_pixel(i,j,color)
        time.sleep(0.1)
        sense.clear()
        time.sleep(0.1)
        x=x+1
    if(img_lock == 1):
        fg.lock_img()
    else:
        fg.unlock_img()

def check_answer(answer, num):
    answer = answer.lower()
    if(answer == mitm_answers[num]):
        if (lock_answer != 1):
            tthread_1 = threading.Thread(target = sound_answer(1))
            tthread_2 = threading.Thread(target = light_answer(1,1))
            tthread_1.start()
            tthread_2.start()
            tthread_1.join()
            tthread_2.join()
            os.system("echo $(tput setaf 2)You are right!!!... Please answer the next question$(tput sgr0)")
            return 1
	else:
            tthread_1 = threading.Thread(target = sound_answer(1))
            tthread_2 = threading.Thread(target = light_answer(1,0))
            tthread_1.start()
            tthread_2.start()
            tthread_1.join()
            tthread_2.join()
            os.system("echo $(tput setaf 2)You are right!!!...$(tput setaf 3)$(tput bold) Congratulations! You have unlocked the secret file'(s'\) needed to complete this workshop.$(tput sgr0)")
            global workshop_num
	    if(workshop_num == 0):
	    	instr = 'chmod +x /home/pi/original_files/traffic.py'
                os.system(instr)
                instr = 'cp /home/pi/original_files/traffic.py /home/pi/Desktop/'
                os.system(instr)
	    elif(workshop_num == 1):
                instr = 'cp /home/pi/original_files/pro_traffic.py /home/pi/Desktop/traffic.py'
                os.system(instr)
		instr = 'chmod 777 /home/pi/Desktop/traffic.py'
                os.system(instr)
		instr = 'cp /home/pi/original_files/pieces/* /home/pi/Desktop/'
                os.system(instr)
	    else:
                instr = 'cp /home/pi/original_files/pro_traffic.py /home/pi/Desktop/traffic.py'
                os.system(instr)
		instr = 'chmod 777 /home/pi/Desktop/traffic.py'
                os.system(instr)
            return 1
    else:
        tthread_1 = threading.Thread(target = sound_answer(0))
        tthread_2 = threading.Thread(target = light_answer(0,1))
        tthread_1.start()
        tthread_2.start()
        tthread_1.join()
        tthread_2.join()
        os.system("echo $(tput setaf 1)Your answer is wrong... Please try again!$(tput sgr0)")
        return 0

def welcome():
    msg = 'omxplayer -o both ' + sounds_path + 'duck_hunt.mp3 > log &'
    os.system(msg)
    msg = 'figlet -f isometric2 \'' + event + '\' | lolcat -a -d 3 -F 5'
    os.system(msg)

def hat_figure():
    fg.rainbow()

os.system("./reset.py")
msg = 'tput sgr0'
os.system(msg)
msg = 'figlet -f doom Welcome to\n'
os.system(msg)
g = threading.Thread(target = hat_figure)
g.start()
t = threading.Thread(target = welcome)
t.start()
g.join()
t.join()


team_name = ''
team_emails = {}
team_members = {}
lock_menu = 1
f_emails = '/home/pi/team_emails.txt'
m_names = '/home/pi/team_members.txt'
s_emails = '/home/pi/sent_email.txt'
if os.path.isfile(f_emails):
    msg = 'rm ' + f_emails
    os.system(msg)
if os.path.isfile(m_names):
    msg = 'rm ' + m_names
    os.system(msg)
if os.path.isfile(s_emails):
    msg = 'rm ' + s_emails
    os.system(msg)
while(lock_menu):
    team_name = raw_input('\nWhat is your team name?: ')
    team_name = team_name.upper()
    input_validation = team_name.replace(' ','')
    if(input_validation != ''):
        f_team = '/home/pi/team_name.txt'
        with open(f_team, "w") as ft:
            ft.write(team_name)
        msg = 'figlet -f slant HELLO'
        os.system(msg)
        msg = 'tput setaf ' + str(random.choice(range(1,7)))
        os.system(msg)
        msg = 'figlet -f starwars ' + team_name
        os.system(msg)
        msg = 'tput sgr0'
        os.system(msg)
        sense.clear()
        time.sleep(2)
        lock_menu = 0
        lock_members = 1
        total_team_members = 0
        print '\nAt the end of this workshop, you will get an email with a certificate of participation!\nPlease enter the e-mail address of each of the team members (one by one):\n'
        while(lock_members):
            total_emails = raw_input('How many members in your team? ')
            try:
                total_team_members = int(total_emails)
                lock_members = 0
            except:
                os.system("echo $(tput setaf 1)Invalid number! Try again...$(tput sgr0)")
                print '\n'
                os.system(msg)
        for i in range(0,total_team_members):
            valid_email = 1
            while(valid_email):
                m_name = raw_input('Name of team member #' + str(i+1) + ': ')
                e_address1 = raw_input('Email address of team member #' + str(i+1) + ': ')
                e_address1 = e_address1.lower()
                e_address2 = raw_input('Confirm Email address of team member #' + str(i+1) + ': ')
                e_address2 = e_address2.lower()
                if(e_address1 == e_address2):
                    team_emails[i] = e_address1
                    team_members[i] = m_name
                    valid_email = 0
                else:
                    os.system("echo $(tput setaf 1)Emails do NOT match. Try again!$(tput sgr0)")
        for i in range(0,total_team_members):
            with open(f_emails, "a+") as fe:
                fe.write(team_emails[i])
                if(i != total_team_members-1):
                    fe.write('\n')
        for j in range(0,total_team_members):
            with open(m_names, "a+") as mn:
                mn.write(team_members[j])
                if(j != total_team_members-1):
                    mn.write('\n')
    else:
        os.system("echo $(tput setaf 1)Invalid team name... try again!$(tput sgr0)")


msg = 'tput bold'
os.system(msg)
msg = 'tput setaf ' + str(random.choice(range(1,7)))
os.system(msg)
animal_msg = ['bud-frogs', 'default', 'dragon', 'elephant', 'ghostbusters', 'koala', 'moose', 'sheep', 'stegosaurus', 'turkey', 'turtle', 'tux']
msg = 'cowsay -f ' + random.choice(animal_msg) + ' \"Hello ' + team_name + '! Let\'s build a Network Scanner by answering the following questions...\"'
os.system(msg)
msg = 'tput sgr0'
os.system(msg)
time.sleep(1)

while(lock_workshop):
    workshop_code = raw_input('\nWhat is the Workshop Code?\n')
    workshop_code = workshop_code.lower()
    lock_workshop = check_code(workshop_code)

while(lock_ip):
    ip_address = raw_input('\nWhat is your IP address?\n')
    lock_ip = check_ip(ip_address)

while(lock_ifconfig):
    command = raw_input('\n\nEnter the command to get your IP address: ')
    command = command.lower()
    if(command == 'ifconfig eth0'):
        os.system('ifconfig eth0')
	lock_ifconfig = 0
    else:
        os.system("echo $(tput setaf 1)Invalid command... Try again!$(tput sgr0)")

msg = 'tput setaf 3'
os.system(msg)
msg = 'tput bold'
os.system(msg)
raw_input('Please press ENTER to continue...')
msg = 'tput sgr0'
os.system(msg)
print '\n\nPlease answer the following questions (' + str(total_questions) + ' questions total).\nIf your answer is wrong, please try again until you get it right.\nIf your answer is right, continue answering the next questions until you get the secret file(s) needed to complete the workshop.\n'
sense.clear()
fg.lock_img()

while(lock_answer):
    for i in range(0,total_questions):
        ret_lock_answer = 0
        while(ret_lock_answer == 0):
            msg = 'tput setaf 3'
            os.system(msg)
            msg = 'tput bold'
            os.system(msg)
            msg = 'bash -c \'echo -ne "\nQuestion #"\''
            os.system(msg)
            aux = i+1
            msg = 'bash -c \'echo -ne ' + str(aux) + '\''
            os.system(msg)
            msg = 'bash -c \'echo -ne ": "\''
            os.system(msg)
            msg = 'tput sgr0'
            os.system(msg)
            aux = mitm_questions[mitm_shuffle[i]]
            msg = 'bash -c \'echo -ne "' + aux + '\n"\''
            os.system(msg)
            answer = raw_input()
            tcflush(sys.stdin, TCIFLUSH)
            ret_lock_answer = check_answer(answer,mitm_shuffle[i])
            lock_answer -= ret_lock_answer

print '\nThe Raspberry Pi has saved your configuration. Changes will take effect after the system restarts. In order to continue, you must reboot the Raspberry Pi...\n'
while(lock_reboot):
    command = raw_input('\n\nEnter the command to reboot the Raspberry Pi: ')
    command = command.lower()
    if(command == 'reboot'):
        sense.clear()
        os.system('reboot')
    else:
        os.system("echo $(tput setaf 1)Invalid command... Try again!$(tput sgr0)")
