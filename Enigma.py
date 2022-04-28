'''
ENIGMA (PORTABLE .EXE)
'''
import tkinter as tk
from tkinter import *
import sys
window=tk.Tk()
window.title("Enigma 8GP - Made by Rion Dutt")
window.geometry("700x550")
window.resizable(width=False, height=False)
#window.configure(bg='#804000')
outputbox = Text(window, height=6, width = 75, font=("Calibri",12))
inputbox = Text(window, height=6, width = 75, font=("Calibri",12))
#grey = tk.Canvas(window, bg="#454545", height=700, width=700)
#grey.place(x = 40, y=40)
outputbox.place(x= 50, y = 50)
output = ""
lettercount = 0
inputbox.place(x=50, y=380)
rotor1box = Text(window, height=1, width = 2, font=("Calibri",20))
rotor2box = Text(window, height=1, width = 2, font=("Calibri",20))
rotor3box = Text(window, height=1, width = 2, font=("Calibri",20))
rotor1box.place(x=80, y=255)
rotor2box.place(x=130, y=255)
rotor3box.place(x=180, y=255)



def save():
    global rotor1
    global rotor2
    global rotor3
    global ref
    global rotors
    rotor11 = rot1.get("1.0","end")
    rotor21 = rot2.get("1.0","end")
    rotor31 = rot3.get("1.0","end")
    ref1 = refl.get("1.0","end")
    rotor1 = []
    rotor2 = []
    rotor3 = []
    ref = []
    for i in range(0, 26):
        rotor1.append(rotor11[i])
        rotor2.append(rotor21[i])
        rotor3.append(rotor31[i])
        ref.append(ref1[i])
    rotors = [rotor1,rotor2,rotor3,ref]
rot1 = Text(window, height=1, width = 26, font=("Consolas",13))
rot2 = Text(window, height=1, width = 26, font=("Consolas",13))
rot3 = Text(window, height=1, width = 26, font=("Consolas",13))
refl = Text(window, height=1, width = 26, font=("Consolas",13))
alph = Label(window, text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", font=("Consolas",13)).place(x = 379,y = 180)
r1t = Label(window, text = "Rotor 1:", font=("Consolas",15)).place(x = 260,y = 210)
r2t = Label(window, text = "Rotor 2:", font=("Consolas",15)).place(x = 260,y = 240)
r3t = Label(window, text = "Rotor 3:", font=("Consolas",15)).place(x = 260,y = 270)
reft = Label(window, text = "Reflector:", font=("Consolas",15)).place(x = 260,y = 300)
savewiring = tk.Button(window, text="Save Wiring", font = ("Calibri",13),command = save, activebackground = "Grey", activeforeground = "Grey")
savewiring.place(x=440, y=328)
rot1.place(x =380, y=210)
rot2.place(x =380, y=240)
rot3.place(x =380, y=270)
refl.place(x =380, y=300)

rotor11 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rotor21 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor31 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
ref1 =    'YRUHQSLDPXNGOKMIEBFZCWVJAT'
alpha =   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rotor1 = []
rotor2 = []
rotor3 = []

rotor1turnover = 17
rotor2turnover = 5
rotor3turnover = 22 
ref = []

rotor1tick = 1
rotor2tick = 1
rotor3tick = 1
for i in rotor11:
    rotor1.append(i)
for i in rotor21:
    rotor2.append(i)
for i in rotor31:
    rotor3.append(i)
for i in ref1:
    ref.append(i)
rotors = [rotor1,rotor2,rotor3,ref]
rotorticks = [rotor1tick,rotor2tick,rotor3tick]
enigma = True

rot1.insert("1.0", "".join(map(str, rotor1)))
rot2.insert("1.0", "".join(map(str, rotor2)))
rot3.insert("1.0", "".join(map(str, rotor3)))
refl.insert("1.0", "".join(map(str, ref)))
strip = ""


def encrypt():
    global active
    change(3, False)
    change(2, False)
    change(1, False)
    change(4, False)
    change(1, True)
    change(2, True)
    change(3, True)
    
def change(rotor,reversebool):
    global active
    if reversebool == True:
        active = ((rotors[rotor-1])[active])
        active = alpha.find(active)
    else:
        active = alpha[active]
        active = (rotors[rotor-1]).index(active)
    
def rotincrement(rotor,reversebool):
    global rotor1tick
    global rotor2tick
    global rotor3tick
    if reversebool == False:
        temprot = (rotors[rotor-1])[0]
        rotors[rotor-1].remove((rotors[rotor-1])[0])
        (rotors[rotor-1]).insert(25,temprot)
        if rotorticks[rotor-1] < 26:
            rotorticks[rotor-1] += 1
        else:
            rotorticks[rotor-1] = 1
        
    else:
        temprot = (rotors[rotor-1])[25]
        (rotors[rotor-1]).remove((rotors[rotor-1])[25])
        (rotors[rotor-1]).insert(0,temprot)
        if rotorticks[rotor-1] > 1:
            rotorticks[rotor-1] -= 1
        else:
            rotorticks[rotor-1] = 26        
    
def rotate(count,reversebool):
    global rotor1
    global rotor2
    global rotor3
    global rotor1tick
    global rotor2tick
    global rotor3tick
    #ROLL FORWARD
    if reversebool == False:
        rotincrement(3, False)
        if rotorticks[2] == rotor3turnover:
            rotincrement(2, False)     
            if rotorticks[1] == rotor2turnover:
                rotincrement(1, False)
                
    #ROLL BACKWARD
    elif reversebool == True:
        for i in range (1, count+1):
            rotincrement(3, True)
            if rotorticks[2] == rotor3turnover:
                rotincrement(2, True)
                if rotorticks[1] == rotor2turnover:
                    rotincrement(1, True)

#DEFINE BUTTONS FOR ROTOR SETTING

r1plus = tk.Button(window, text ="➕", font = ("Calibri",12),command = lambda:rotincrement(1,False), activebackground = "Grey", activeforeground = "Grey").place(x=80, y=200)
r2plus = tk.Button(window, text ="➕", font = ("Calibri",12),command = lambda:rotincrement(2,False), activebackground = "Grey", activeforeground = "Grey").place(x=130, y=200)
r3plus = tk.Button(window, text ="➕", font = ("Calibri",12),command = lambda:rotincrement(3,False), activebackground = "Grey", activeforeground = "Grey").place(x=180, y=200)
r1min = tk.Button(window, text ="➖", font = ("Calibri",12), command = lambda:rotincrement(1,True), activebackground = "Grey", activeforeground = "Grey").place(x=80, y=310)
r2min = tk.Button(window, text ="➖", font = ("Calibri",12),command = lambda:rotincrement(2,True), activebackground = "Grey", activeforeground = "Grey").place(x=130, y=310)
r3min = tk.Button(window, text ="➖", font = ("Calibri",12),command = lambda:rotincrement(3,True), activebackground = "Grey", activeforeground = "Grey").place(x=180, y=310)

'''
  __  __          _____ _   _     _      ____   ____  _____  _ 
 |  \/  |   /\   |_   _| \ | |   | |    / __ \ / __ \|  __ \| |
 | \  / |  /  \    | | |  \| |   | |   | |  | | |  | | |__) | |
 | |\/| | / /\ \   | | | . ` |   | |   | |  | | |  | |  ___/| |
 | |  | |/ ____ \ _| |_| |\  |   | |___| |__| | |__| | |    |_|
 |_|  |_/_/    \_\_____|_| \_|   |______\____/ \____/|_|    (_)
                                                                                                                         
'''




while enigma:
    
#UPDATE UI ROTORTICKS/USER INPUT
    try:
        rotor3box.delete("1.0",END)
        rotor3box.insert("1.0",rotorticks[2])
        rotor2box.delete("1.0",END)
        rotor2box.insert("1.0",rotorticks[1])
        rotor1box.delete("1.0",END)
        rotor1box.insert("1.0",rotorticks[0])
        uinput = inputbox.get("1.0",END)
    except:
        sys.exit()
#LETTER COUNT UPDATE DETECTION
    
    if lettercount != len(uinput):
        if lettercount < len(uinput)and len(uinput) > 1:
            if len(uinput)-lettercount > 1:
                for i in range (1, len(uinput)-lettercount+1):
                    active = alpha.find(uinput[i-1].upper())
                    encrypt()
                    rotate(1,False)
                    outputbox.insert(END,alpha[active])
                
            else:
                active = alpha.find(uinput[len(uinput)-2].upper())
                encrypt()
                rotate(1,False)
                outputbox.insert(END,alpha[active])
                
        elif  lettercount > len(uinput):
            if lettercount-len(uinput) < 2:
                rotate(1,True)
                uoutput = outputbox.get("1.0",END)
                strip = uoutput[:-2]
                outputbox.delete("1.0",END)
                outputbox.insert("1.0",strip)
                
            else:
                rotate(lettercount-len(uinput),True)
                uoutput = outputbox.get("1.0",END)
                strip = uoutput[:((lettercount-len(uinput))*-1)-1]
                outputbox.delete("1.0",END)
                outputbox.insert("1.0",strip)
                
        #UPDATE ROTOR WIRING BOXES  
        rot1.delete("1.0",END)
        rot1.insert("1.0", "".join(map(str, rotor1)))
        rot2.delete("1.0",END)
        rot2.insert("1.0", "".join(map(str, rotor2)))
        rot3.delete("1.0",END)
        rot3.insert("1.0", "".join(map(str, rotor3)))
        refl.delete("1.0",END)
        refl.insert("1.0", "".join(map(str, ref)))
        
#REDEFINE LETTERCOUNT
        
    lettercount = len(uinput)
    window.update()
