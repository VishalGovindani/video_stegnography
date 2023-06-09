
##This File for Text and text Document read
from stegano import lsb
import cv2
import os
import sys
import aesutil
import shutil
import numpy as np
from termcolor import cprint 
from pyfiglet import figlet_format
import rsautil1
from simple_colors import *
import time


def decrypt_file(file,method):
    global to_decrypt
    to_decrypt=file

    global decode_method
    decode_method=method

    global FRAMES

    global Encryption_Style
    global decoded

    os.system('cls' if os.name == 'nt' else 'clear')
    cprint(figlet_format('Group9', font='slant'),'green', attrs=['bold'])
    print(yellow('Video Steganography', ['bold']))
    print(blue('Group Members', ['bold']))
        # Prajwal Atram, Hitashri Patil, Nupur Shinde, Vishal Singh, Sameer Meshram
    print("\n")
    print("06 - Prajwal Atram")
    print("40 - Hitashri Patil")
    print("54 - Nupur Shinde")
    print("63 - Vishal Singh")
    print("76 - Sameer Meshram")

    print("\n\n")
    time.sleep(2)
    cprint(figlet_format('AES & RSA encrytion', font='digital'),'green', attrs=['bold'])
    global ENCODED_VIDEO 
    ENCODED_VIDEO = to_decrypt
    global temp_folder
    temp_folder = "tmp2"
    # frame_choice = int(input("1) Extract and enter frame numbers from image \n2) Enter frame numbers manually : \nEnter choice: "))
    frame_choice=2
    decoded = {}

    if frame_choice == 1:
        ENCODED_IMAGE = input("\n Enter image name with extension : ")
        res = lsb.reveal(ENCODED_IMAGE)
        print(f"Encrypted frame numbers : {res}")
        cprint("Select your encryption type \n 1) AES Encrypted {Symetric Encryption} \n 2) RSA Encrypted {Assysmetric Encryption}",'blue')
        Encryption_Style=int(input(""))
        if Encryption_Style == 1:
            key = input("Enter the asymetric key to create AES key : ")
            key_rsa = rsautil1.decrypt(message=key)
            key_rsa = key_rsa.decode('utf-8')
            print(f"Asymetric decrypted key \n {key_rsa}")
            key123=int(input("Choose key type to decrypt image   \n 2.ASCII : "))
            key = input("Enter the key to decrypt image : ")
            if key123==1:
                msg = aesutil.decrypt(key=key,source=res)
                msg1 = msg.decode('utf-8')
                cprint(f"Decoded image : \n {msg}",'green')
                FRAMES = list(map(int, input("Enter Above FRAME NUMBERS seperated by space: ").split()))
        
            else:
                msg = aesutil.decrypt(key=key,source=res,keyType='ascii')
                msg1 = msg.decode('utf-8')
                cprint(f"Decoded image: \n {msg1}",'green')
                FRAMES = list(map(int, input("Enter Above FRAME NUMBERS seperated by space: ").split()))
        else :
            cprint("Reading private key from keys \nfolder and trying to decrypt",'red')
            msg1 = rsautil1.decrypt(message=res)
            msg1 = msg1.decode('utf-8')
            cprint(f"Decoded image: \n {msg1}",'green')
            FRAMES = list(map(int, input("Enter Above FRAME NUMBERS seperated by space: ").split()))
    
        
    else :
        

        FRAMES = [i for i in range(1,16)]
        cprint("Select your decryption type \n 1) AES Encrypted {Symetric Encryption} \n 2) RSA Encrypted {Assysmetric Encryption}",'blue')
        Encryption_Style=int(decode_method)
        #print(FRAMES)
    createTmp()
    frames = countFrames()
    decodeVideo(frames)
    return arrangeAndDecrypt()
# pip3 install gTTS pyttsx3
def createTmp():
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

def countFrames():
    cap = cv2.VideoCapture(ENCODED_VIDEO)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def decodeVideo(number_of_frames):
    # First get the frame
    cap = cv2.VideoCapture(ENCODED_VIDEO)
    frame_number = -1
    while(frame_number<=number_of_frames):
        frame_number += 1
        frame_file_name = os.path.join(temp_folder,f"{frame_number}.png")
        encoded_frame_file_name = os.path.join(temp_folder,f"{frame_number}-enc.png")
        # print(f"Frame number {frame_number}")
        ret, frame = cap.read()

        if frame_number in FRAMES:
            cv2.imwrite(encoded_frame_file_name,frame)
            clear_message = lsb.reveal(encoded_frame_file_name)
            decoded[frame_number] = clear_message
            cprint(f"Frame {frame_number} DECODED: {clear_message}",'yellow')

def clean_tmp(path="./tmp2"):
    if os.path.exists(path):
        shutil.rmtree(path)
        cprint("[INFO] tmp files are cleaned up",'yellow')

def arrangeAndDecrypt():
    res=""
    if Encryption_Style == 1:
        
        for fn in FRAMES:
            res = res + decoded[fn]
        cprint(f"Final string: {res}",'green')
        key123=int(2)
        key = '1'
        if key123==1:

            msg = aesutil.decrypt(key=key,source=res)
            msg1 = msg.decode('utf-8')
           
            # s=msg
            # li=s.split(" ")
            # result=[]
            # a=[]
            # b=[]
            # print((li))
            # c=0
            # for i in range(154):

            #     for j in range(328):
            #         for k in range(3):
            #             b.append(int(li[c]))
            #             c+=1
            #         a.append(b)
            #         b=[]
            #     result.append(a)
            #     a=[]
            # # ans=[]
            # # for i in result:
            # #     for j in i:
            # #         for k in j:
            # #             ans.append(k)
            # # print((ans))
            # result=np.asarray(result)
            # result=result.astype(np.uint8)
            # # print(result.shape)
            # print(type(result))
            # cv2.imshow('avc',result)
            # cv2.waitKey(0)
            cprint(f"Decoded message: \n {msg}",'green')
            print(1)
            clean_tmp()
        else:
            msg = aesutil.decrypt(key=key,source=res,keyType='ascii')
            msg1 = msg.decode('utf-8')

            if(msg1[-1]=='2'):
                s=msg1[:-1]

                print(s)
                return "Output is \n"+s

            elif(msg1[-1]=='3'):

                s=msg1[:-7]
                r=int(msg1[-7:-4])
                co=int(msg1[-4:-1])
                print(r,co)
                print(type(r))

                li=s.split(" ")
                result=[]
                a=[]
                b=[]
               
                c=0
                print(len(li))
                for i in range(r):
                        
                        for j in range(co):
                            for k in range(3):
                                b.append(int(li[c]))
                                c+=1
                            a.append(b)
                            b=[]
                        result.append(a)
                        a=[]
                print(c)
                result=np.asarray(result)
                # print(result.shape)
                result=result.astype(np.uint8)
                print(result.shape)
                print(type(result))
                # cv2.imshow('Hidden Image',result)
                print("Wait until Image Opens!!")

                cv2.waitKey(0)




            elif(msg1[-1]=='4'):
                s=msg1[:-1]
                print(s)
            
            elif(msg1[-1]=='5'):



                pass

            elif(msg1[-1]=='6'):
                r=int(msg1[-7:-4])
                co=int(msg1[-4:-1])
                s=msg1[:-7]


                li=s.split(" ")
                c=0

                while(c<len(li)):

                    result=[]
                    a=[]
                    b=[]

                    for i in range(r):
                                
                                for j in range(co):
                                    for k in range(3):
                                        b.append(int(li[c]))
                                        c+=1
                                    a.append(b)
                                    b=[]
                                result.append(a)
                                a=[]
                    result=np.asarray(result)
                    # print(result.shape)
                    result=result.astype(np.uint8)
                    print(result.shape)
                    print(type(result))
                    cv2.imshow('Hidden Image',result)
                    # print("Wait until Image Opens!!")

                    cv2.waitKey(2000)








            # cprint(f"Decoded message: \n {msg1}",'red')
            # msg1.save("output.mp3")
            print(2)
            # Playing the converted file
            # os.system("output.mp3")
            clean_tmp()
    else :
        for fn in FRAMES:
            res = res + decoded[fn]
        cprint(f"Final string: {res}",'green')
        cprint("Reading private key from keys folder \nand trying to decrypt",'red')
        msg1 = rsautil1.decrypt(message=res)
        msg1 = msg1.decode('utf-8')
        

        
        cprint(f"Decoded text: \n {msg1}",'green')
        clean_tmp()

