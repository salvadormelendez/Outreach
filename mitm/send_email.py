#!/usr/bin/python

#############################################
# Send Email Python Script
# Designed and Written by Salvador Melendez
#############################################

import sys
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

s_email = '/home/pi/sent_email.txt'
pwd = ''
with open('/home/pi/Documents/raw/pwd.txt', 'r') as pw:
    for i, line in enumerate(pw):
        pwd = line.rstrip('\n')

fromaddr = "afc.cyberteam@gmail.com"
toaddr = ''
team_member = ''
if(len(sys.argv)>1):
    toaddr = sys.argv[1]
    team_member = sys.argv[2]

#msg = './send_email.py ' + team_emails[j] + ' ' + '\'' + team_members[j] + '\''

os.chdir("/home/pi/")
msg = './cert_generator.py ' + '\'' + team_member + '\''
os.system(msg)

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "AFC Workshop - Certificate of Participation"

body = team_member + ":\nThanks for attending our workshop!\nAFC"
msg.attach(MIMEText(body,'plain'))

team_member = team_member.replace(' ','_')
filename = team_member + "_cert.jpg"
attachment = open("/home/pi/Music/certificates/certs/" + team_member + "_cert.jpg", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename = %s" % filename)

msg.attach(part)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pwd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    with open(s_email, "w") as se:
        se.write('1')
except:
    msg = 'tput setaf 3'
    os.system(msg)
    print "Check your Wi-Fi connection to get your certificate. Connect to a Wireless Network and then restart this script again.\n\n"
    msg = 'tput setaf 1'
    os.system(msg)
    if os.path.isfile("/home/pi/sent_email.txt"):
        os.system("rm /home/pi/sent_email.txt")
