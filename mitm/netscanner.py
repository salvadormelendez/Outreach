#!/usr/bin/python

#############################################
# Network Scanner Python Script
# Designed and Written by Salvador Melendez
#############################################

import os
import sys
import threading

def init():
    tthread_1 = threading.Thread(target = banner)
    tthread_2 = threading.Thread(target = send_email)
    tthread_1.start()
    tthread_2.start()
    tthread_1.join()
    tthread_2.join()

def banner():
    msg = 'tput setaf 4'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    msg = 'bash -c \'echo -ne "\n**********"\''
    os.system(msg)
    msg = 'tput setaf 2'
    os.system(msg)
    msg = 'bash -c \'echo -ne "NETWORK SCANNER"\''
    os.system(msg)
    msg = 'tput setaf 4'
    os.system(msg)
    msg = 'bash -c \'echo -ne "**********\n"\''
    os.system(msg)
    msg = 'tput setaf 1'
    os.system(msg)
    msg = 'bash -c \'for i in {1..10}; do echo -ne "Loading configuration   \\r"; sleep 0.3; echo -ne "Loading configuration.\\r"; sleep 0.3; echo -ne "Loading configuration..\\r"; sleep 0.3; echo -ne "Loading configuration...\\r"; sleep 0.3; done\''
    os.system(msg)
    msg = 'tput sgr0'
    os.system(msg)

def please_wait():
    msg = 'tput bold'
    os.system(msg)
    msg = 'tput setaf 3'
    os.system(msg)
    msg = 'bash -c \'for i in {1..20}; do echo -ne "Please wait   \\r"; sleep 0.3; echo -ne "Please wait.\\r"; sleep 0.3; echo -ne "Please wait..\\r"; sleep 0.3; echo -ne "Please wait...\\r"; sleep 0.3; done\''
    os.system(msg)
    msg = 'tput sgr0'
    os.system(msg)

def loading_sniff():
    msg = 'tput bold'
    os.system(msg)
    msg = 'tput setaf 1'
    os.system(msg)
    msg = 'bash -c \'for i in {1..10}; do echo -ne "Loading network scanner   \\r"; sleep 0.3; echo -ne "Loading network scanner.\\r"; sleep 0.3; echo -ne "Loading network scanner..\\r"; sleep 0.3; echo -ne "Loading network scanner...\\r"; sleep 0.3; done\''
    os.system(msg)
    msg = 'tput sgr0'
    os.system(msg)

def send_email():
    team_members = {}
    team_emails = {}
    os.chdir("/home/pi/")
    s_email = '/home/pi/sent_email.txt'
    if not os.path.isfile(s_email):
        with open('/home/pi/team_members.txt', 'r') as tm:
            for i, line in enumerate(tm):
                team_members[i] = line.rstrip('\n')
        with open('/home/pi/team_emails.txt', 'r') as te:
            for j, line in enumerate(te):
                team_emails[j] = line.rstrip('\n')
                msg = './send_email.py ' + team_emails[j] + ' ' + '\'' + team_members[j] + '\''
                os.system(msg)
    os.chdir("/home/pi/Desktop")
