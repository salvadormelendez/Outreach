#!/usr/bin/env python3

from tkinter import *
import time
import random
import os
import sys

shift_num = 0
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def decode_msg():
    decoded_number = {}
    decoded_index = 0
    decoded_msg = ''
    msg = str(e1.get())
    msg = msg.upper()
    shift_num = int(e2.get())
    real_shift = shift_num%(len(alphabet)-1)
    if len(msg) != 0:
        for s in msg:
            if s in alphabet:
                string_index = alphabet.index(s)
                new_index = string_index - shift_num
                if new_index < 0:
                    new_index = new_index + len(alphabet)
                decoded_number[decoded_index] = new_index
                decoded_index += 1
            elif s == ' ':
                decoded_number[decoded_index] = len(alphabet)+1
                decoded_index += 1
        for i in range(0,decoded_index):
            if(decoded_number[i] == len(alphabet)+1):
                decoded_msg += ' '
            else:
                decoded_msg += alphabet[decoded_number[i]]
        if all(x.isalpha() or x.isspace() for x in msg):
            msg = decoded_msg
            result_label.configure(text=msg, fg='green')
        else:
            msg = 'Enter a valid message to DECODE'
            result_label.configure(text=msg, fg='yellow')
    else:
        msg = 'Enter a valid message to DECODE'
        result_label.configure(text=msg, fg='yellow')

def encode_msg():
    encoded_number = {}
    encoded_index = 0
    encoded_msg = ''
    msg = str(e1.get())
    msg = msg.upper()
    shift_num = int(e2.get())
    real_shift = shift_num%(len(alphabet)-1)
    if len(msg) != 0:
        for s in msg:
            if s in alphabet:
                string_index = alphabet.index(s)
                new_index = string_index + shift_num
                if new_index > (len(alphabet)-1):
                    new_index = new_index - len(alphabet)
                encoded_number[encoded_index] = new_index
                encoded_index += 1
            elif s == ' ':
                encoded_number[encoded_index] = len(alphabet)+1
                encoded_index += 1
        for i in range(0,encoded_index):
            if(encoded_number[i] == len(alphabet)+1):
                encoded_msg += ' '
            else:
                encoded_msg += alphabet[encoded_number[i]]
        if all(x.isalpha() or x.isspace() for x in msg):
            msg = encoded_msg
            result_label.configure(text=msg, fg='red')
        else:
            msg = 'Enter a valid message to ENCODE'
            result_label.configure(text=msg, fg='yellow')
    else:
        msg = 'Enter a valid message to ENCODE'
        result_label.configure(text=msg, fg='yellow')
            
def dec_enc():
    if(var.get() == 1):
        decode_msg()
    else:
        encode_msg()

def quit():
    exit()

master = Tk()
master.title("DECODER / ENCODER")
master.configure(background='black')
w = 1000
h = 300
ws = master.winfo_screenwidth()
hs = master.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
master.geometry('%dx%d+%d+%d' % (w, h, x, y))

msg_label = Label(master, wraplength=150, text="Message:", font="Verdana 20 bold", background='black', fg='gold')
msg_label.grid(row=0, column=0)
e1 = Entry(master, width=50)
e1.grid(row=0, column=1)
e1.insert(50,"fbehu dwwdfn")

shift_label = Label(master, wraplength=100, text="Shift:", font="Verdana 20 bold", background='black', fg='gold')
shift_label.grid(row=1, column=0)
e2 = Entry(master, width=10)
e2.grid(row=1, column=1)
e2.insert(10,"3")

op_label = Label(master, wraplength=150, text="Dec/Enc?:", font="Verdana 20 bold", background='black', fg='gold')
op_label.grid(row=2, column=0)
var = IntVar()
var.set(1)
decode_button = Radiobutton(master, text="Decode", variable=var, value=1, background='black', fg='green')
decode_button.grid(row=2, column=1)
encode_button = Radiobutton(master, text="Encode", variable=var, value=2, background='black', fg='red')
encode_button.grid(row=3, column=1)

result_label = Label(master, wraplength=400, text="", font="Verdana 14 bold", background='black', fg='gold')
result_label.grid(row=5, column=2)

get_msr = Button(master, text='Get Message!', command=lambda: dec_enc(), height=2, width=10, wraplength=150, font="Times 20 bold", background='RoyalBlue1', highlightthickness='0', activebackground='orange', fg='gold')
get_msr.grid(row=5, column=1, sticky=W, pady=4)

quit_button = Button(master, text='QUIT', command=lambda: quit(), height=1, width=10, wraplength=80, font="Times 20 bold", background='slate gray', highlightthickness='0', activebackground='orange', fg='gold')
quit_button.grid(row=6, column=1, sticky=W, pady=4)
    
mainloop()
