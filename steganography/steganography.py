#!/usr/bin/env python3

##################################################
# Steganography Python Script
# Designed and Written by Salvador Melendez
##################################################

import sys
import os
from PIL import Image
import numpy as np
import random as rand

#DECLARE VARIABLES
i_file = 'image.png' #input file
o_file = 'new_image' #output file
#DEFINE ALPHABET - Alphanumeric & Binary
characters = ['', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '"', '\'', '<', '>', ',', '.', '?', '/']
binary = ['000000000', '000000001', '000000010', '000000011', '000000100', '000000101', '000000110', '000000111', '000001000', '000001001', '000001010', '000001011', '000001100', '000001101', '000001110', '000001111', '000010000', '000010001', '000010010', '000010011', '000010100', '000010101', '000010110', '000010111', '000011000', '000011001', '000011010', '000011011', '000011100', '000011101', '000011110', '000011111', '000100000', '000100001', '000100010', '000100011', '000100100', '000100101', '000100110', '000100111', '000101000', '000101001', '000101010', '000101011', '000101100', '000101101', '000101110', '000101111', '000110000', '000110001', '000110010', '000110011', '000110100', '000110101', '000110110', '000110111', '000111000', '000111001', '000111010', '000111011', '000111100', '000111101', '000111110', '000111111', '001000000', '001000001', '001000010', '001000011', '001000100', '001000101', '001000110', '001000111', '001001000', '001001001', '001001010', '001001011', '001001100', '001001101', '001001110', '001001111', '001010000', '001010001', '001010010', '001010011', '001010100', '001010101', '001010110', '001010111', '001011000', '001011001', '001011010', '001011011', '001011100', '001011101', '001011110', '001011111']
option = 0 #'1' - Encode / '2' - Decode
encoded_msg = []
decoded_msg = ''

#USERS MAIN MENU - ENCODE OR DECODE
def menu():
    global option
    m_lock = 1
    while(m_lock):
        u_input = input('Encode or Decode Image? (Type 1 or E to Encode. Type 2 or D to Decode)\n')
        if(u_input == '1' or u_input == 'E' or u_input == 'e'):
            option = 1
            m_lock = 0
        elif(u_input == '2' or u_input == 'D' or u_input == 'd'):
            option = 2
            m_lock = 0
        else:
            print('Invalid selection. Try again!\n')


#CHECK IF NUMBER EVEN OR ODD
def checker(num):
    if(num%2 == 0):
        return '0' #EVEN
    else:
        return '1' #ODD


#RESTORE CHARACTER FROM PIXELS
def restore_char_pixels(encoded_img, y):
    global decoded_msg
    width, height = Image.open(encoded_img).size
    img = np.array(Image.open(encoded_img).convert('RGB')) # [x][y][r,g,b]
    word_lock = 1
    while(word_lock):
        for i in range(width):
            s_pixel = i * 3
            e_pixel = s_pixel + 3
            bits_char = []
            for x in range(s_pixel,e_pixel):
                bits_char.append(checker(img[x][y][0])) #R
                bits_char.append(checker(img[x][y][1])) #G
                bits_char.append(checker(img[x][y][2])) #B
            dec_char = ''
            for j in range(len(bits_char)):
                dec_char += bits_char[j]
            if(dec_char in binary):
                decoded_msg += characters[binary.index(dec_char)]
            if(decoded_msg[-3:] == '\\n*'):
                word_lock = 0
                break
    print('\nDecoded Message --> ' + decoded_msg[:-3])


#ENCODE BITS IF ODD OR EVEN --> ODD - 1 / EVEN - 0
def odd_even(pixel,msg):
    new_pixel = []
    #CHECK IF PIXEL IS EVEN OR ODD AND BIT IS "0" OR "1"
    for i in range(len(msg)):
        if((pixel[i]%2 == 0) and msg[i] == '0'): #PIXEL IS EVEN AND BIT IS '0'
            new_pixel.append(pixel[i])
        elif((pixel[i]%2 == 0) and msg[i] == '1'): #PIXEL IS EVEN AND BIT IS '1'
            new_pixel.append(pixel[i] + 1)
        elif((pixel[i]%2 != 0) and msg[i] == '0'): #PIXEL IS ODD AND BIT IS '0'
            new_pixel.append(pixel[i] - 1)
        elif((pixel[i]%2 != 0) and msg[i] == '1'): #PIXEL IS ODD AND BIT IS '1'
            new_pixel.append(pixel[i])
        else:
            print('error!')
    return (new_pixel[0], new_pixel[1], new_pixel[2])


#STORE CHARACTER IN PIXELS
def store_char_pixels():
    global o_file
    num_chars = len(encoded_msg) # message characters + 3 ending characters
    img = np.array(Image.open(i_file).convert('RGB')) # [x-height][y-width][r,g,b]
    y = rand.randrange(img.shape[1])
    o_file += '_' + str(y) + '.png'
    for i in range(num_chars):
        msg = encoded_msg[i]
        s_pixel = i * 3
        e_pixel = s_pixel + 3
        j = 0
        for x in range(s_pixel,e_pixel):
            pixel = []
            pixel.append(img[x][y][0]) #R
            pixel.append(img[x][y][1]) #G
            pixel.append(img[x][y][2]) #B
            s_msg = j * 3
            e_msg = s_msg + 3
            [r,g,b] = odd_even(pixel,msg[s_msg:e_msg])
            img[x][y][0] = r #R
            img[x][y][1] = g #G
            img[x][y][2] = b #B
            j+=1
    #Convert modified image to array
    arr = np.array(img)
    #Save modified image from array
    img = Image.fromarray(arr)
    img.save(o_file)
    return y


#ENCODE MESSAGE TO IMAGE
def msg_to_img():
    global encoded_msg
    u_msg = input('\nEnter a message you want to hide within the image...\n')
    #CONVERT MESSAGE TO BINARY
    for i in u_msg:
        encoded_msg.append(binary[characters.index(i)])
    encoded_msg.append('001010100') #\
    encoded_msg.append('000001111') #n
    encoded_msg.append('001001001') #*
    img_num = store_char_pixels()
    print('Message encoded on image #' + str(img_num) + '!')


#DECODE IMAGE TO MESSAGE
def img_to_msg():
    files = []
    cwd = os.getcwd()
    for i in os.listdir(cwd):
        files = [i for i in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, i)) and 'new_image_' in i]
    if(len(files) == 0):
        print('\nThere are NO images to decode!')
    else:
        print('\nAvailable images to decode:')
        for j in files:
            print('[' + str(files.index(j)) + '] ' + j)
        lock_sel = 1
        option = 0
        while(lock_sel):
            user_sel = input('\nFrom the list above, which image do you want to decode? Enter the number between []: ')
            try:
                option = int(user_sel)
                if(option >= 0 and option < len(files)):
                    lock_sel = 0
                else:
                    print('Invalid selection... Try again!\n')
            except:
                print('Invalid selection... Try again!\n')
        encoded_img = files[option]
        tmp1 = encoded_img.split('new_image_')
        tmp2 = tmp1[1].split('.png')
        y = int(tmp2[0])
        restore_char_pixels(encoded_img, y)


#MAIN FUNCTION
def main():
    print('Hello!')
    menu()
    if(option == 1):
        msg_to_img()
    elif(option == 2):
        img_to_msg()
    else:
        print('Invalid selection. Try again!\n')
    
if __name__ == "__main__":
    main()

