'''
 _____ _   _ _____ _____  __  __   ___                
|  ___| \ | |_   _|  __ \|  \/  | / _ \               
| |__ |  \| | | | | |  \/| .  . |/ /_\ \  _ __  _   _ 
|  __|| . ` | | | | | __ | |\/| ||  _  | | '_ \| | | |
| |___| |\  |_| |_| |_\ \| |  | || | | |_| |_) | |_| |
\____/\_| \_/\___/ \____/\_|  |_/\_| |_(_) .__/ \__, |
                                         | |     __/ |
                                         |_|    |___/
Made by R.D. 2022
https://github.com/briocherockets/enigma.py
https://www.reddit.com/user/BriocheRockets

   _____ ______ _______ _    _ _____  
  / ____|  ____|__   __| |  | |  __ \ 
 | (___ | |__     | |  | |  | | |__) |
  \___ \|  __|    | |  | |  | |  ___/ 
  ____) | |____   | |  | |__| | |     
 |_____/|______|  |_|   \____/|_|     

'''

#LIBRARIES
import tkinter as tk
from tkinter import *

#WINDOW SETUP
window=tk.Tk()
window.title("Enigma")
window.geometry("700x550")
window.resizable(width=False, height=False)

'INPUT/OUTPUT BOXES'
outputbox = Text(window, height=6, width = 75, font=("Calibri",12))
inputbox = Text(window, height=6, width = 75, font=("Calibri",12))
outputbox.place(x= 50, y = 50)
inputbox.place(x=50, y=380)
lettercount = 0

'WIRING LABELS'
Label(window, text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", font=("Consolas",13)).place(x = 379,y = 180)
Label(window, text = "Rotor 1:", font=("Consolas",15)).place(x = 260,y = 210)
Label(window, text = "Rotor 2:", font=("Consolas",15)).place(x = 260,y = 240)
Label(window, text = "Rotor 3:", font=("Consolas",15)).place(x = 260,y = 270)
Label(window, text = "Reflector:", font=("Consolas",15)).place(x = 260,y = 300)

'EEEEEEEEE'
strip = ""
'^dont remove or else it breaks everything lol'

'ROTOR ROTATION DISPLAYS'
rotor1box = Text(window, height=1, width = 2, font=("Calibri",20))
rotor2box = Text(window, height=1, width = 2, font=("Calibri",20))
rotor3box = Text(window, height=1, width = 2, font=("Calibri",20))
rotor1box.place(x=80, y=255)
rotor2box.place(x=130, y=255)
rotor3box.place(x=180, y=255)

'WIRING TEXTBOXES'
rot1 = Text(window, height=1, width = 26, font=("Consolas",13))
rot2 = Text(window, height=1, width = 26, font=("Consolas",13))
rot3 = Text(window, height=1, width = 26, font=("Consolas",13))
refl = Text(window, height=1, width = 26, font=("Consolas",13))
rot1.place(x =380, y=210)
rot2.place(x =380, y=240)
rot3.place(x =380, y=270)
refl.place(x =380, y=300)

#ROTOR VARIABLES
'TEMPORARY ROTOR VARIABLES (FOR STORAGE BEFORE CONVERSION INTO LIST'
rotor1string = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ' 
rotor2string = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3string = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
reflectorstring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

'TICKS N TURNOVERS'
rotor1turnover = 17
rotor2turnover = 5
rotor3turnover = 22 
rotor1tick = 1
rotor2tick = 1
rotor3tick = 1

'ROTOR LISTS'
rotor1 = []
rotor2 = []
rotor3 = []
rotor1f = []
rotor2f = []
rotor3f = []
reflector = []
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
rotors = [rotor1,rotor2,rotor3,reflector,rotor1f, rotor2f,rotor3f]
rotorticks = [rotor1tick,rotor2tick,rotor3tick]

'TAKE STRINGS AND CONVERT TO LISTS'
for i in range(0, 26):
    rotor3.append(alpha.find(rotor3string[i])+1)
    rotor2.append(alpha.find(rotor2string[i])+1)
    rotor1.append(alpha.find(rotor1string[i])+1)
    reflector.append(alpha.find(reflectorstring[i])+1)
    rotor3f.append(alpha.find(rotor3string[i])-i)
    rotor2f.append(alpha.find(rotor2string[i])-i)
    rotor1f.append(alpha.find(rotor1string[i])-i)

'INSERT VALUES TO BOXES'
rot1.insert("1.0", "".join(map(str, rotor1string)))
rot2.insert("1.0", "".join(map(str, rotor2string)))
rot3.insert("1.0", "".join(map(str, rotor3string)))
refl.insert("1.0", "".join(map(str, reflectorstring)))
rotor3box.insert("1.0",rotorticks[2])
rotor2box.insert("1.0",rotorticks[1])
rotor1box.insert("1.0",rotorticks[0])

#DEFINE FUNCTIONS
def save():
    global rotors
    rotor1string = rot1.get("1.0","end")
    rotor2string = rot2.get("1.0","end")
    rotor3string = rot3.get("1.0","end")
    reflectorstring = refl.get("1.0","end")
    rotor1 = []
    rotor2 = []
    rotor3 = []
    reflector = []
    rotor1f = []
    rotor2f = []
    rotor3f = []
    for i in range(0, 26):
        rotor3.append(alpha.find(rotor3string[i])+1)
        rotor2.append(alpha.find(rotor2string[i])+1)
        rotor1.append(alpha.find(rotor1string[i])+1)
        reflector.append(alpha.find(reflectorstring[i])+1)
        rotor3f.append(alpha.find(rotor3string[i])-i)
        rotor2f.append(alpha.find(rotor2string[i])-i)
        rotor1f.append(alpha.find(rotor1string[i])-i)    
    rotors = [rotor1, rotor2, rotor3, reflector, rotor1f, rotor2f, rotor3f]
    
def change(rotor,reversebool):
    global active
    if rotor == 4:
        active = reflector[active-1]
    elif reversebool == True:
#        print(active+(rotors[rotor+3])[active-1])
        active = (active+(rotors[rotor+3])[active-1])
        if active > 26:
            active -= 26
        if active < 1:
            active += 26
    elif reversebool == False:
#        print(active-(rotors[rotor+3])[(rotors[rotor-1]).index(active)])
#        print(rotors[rotor-1])
        active = (active-(rotors[rotor+3])[(rotors[rotor-1]).index(active)])   
        if active > 26:
            active -= 26
        if active < 1:
            active += 26

def encrypt():    
    change(3, True)
    change(2, True)
    change(1, True)
    change(4, True)
    change(1, False)
    change(2, False)
    change(3, False)
    
def rotincrement(rotor,reversebool):
    if reversebool == False:
        temprot = (rotors[rotor+3])[0]
        del((rotors[rotor+3])[0])
        (rotors[rotor+3]).insert(25,temprot)
        if rotorticks[rotor-1] < 26:
            rotorticks[rotor-1] += 1
        else:
            rotorticks[rotor-1] = 1
        
    else:
        temprot = (rotors[rotor+3])[25]
        del((rotors[rotor+3])[25])
        (rotors[rotor+3]).insert(0,temprot)
        if rotorticks[rotor-1] > 1:
            rotorticks[rotor-1] -= 1
        else:
            rotorticks[rotor-1] = 26
    print(rotors[rotor-1])
    for i in range (0,26):
        
        (rotors[rotor-1])[i] = (rotors[rotor+3])[i]+i+1
        if (rotors[rotor-1])[i] > 26:
            (rotors[rotor-1])[i] -= 26
        elif (rotors[rotor-1])[i] < 1:
            (rotors[rotor-1])[i] += 26
    print(rotors[rotor-1])
    rotor3box.delete("1.0",END)
    rotor3box.insert("1.0",rotorticks[2])
    rotor2box.delete("1.0",END)
    rotor2box.insert("1.0",rotorticks[1])
    rotor1box.delete("1.0",END)
    rotor1box.insert("1.0",rotorticks[0])

def rotate(count,reversebool):
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
            if rotorticks[2] == rotor3turnover-1:
                rotincrement(2, True)
                if rotorticks[1] == rotor2turnover-1:
                    rotincrement(1, True)

def runencrypt(event):
    global lettercount
    global active
    #UPDATE UI ROTORTICKS/USER INPUT
    uinput = inputbox.get("1.0",END)
    #LETTER COUNT UPDATE DETECTION
    if lettercount != len(uinput):
        if lettercount < len(uinput)and len(uinput) > 1:
            if len(uinput)-lettercount > 1:
                for i in range (1, len(uinput)-lettercount+1):
                    active = alpha.find(uinput[i-1].upper())+1
                    rotate(1,False)
                    encrypt()
                    
                    outputbox.insert(END,alpha[active-1])
                
            else:
                active = alpha.find(uinput[len(uinput)-2].upper())+1
                rotate(1,False)
                encrypt()
                outputbox.insert(END,alpha[active-1])
                
        elif  lettercount > len(uinput):
            rotate(lettercount-len(uinput),True)
            uoutput = outputbox.get("1.0",END)
            strip = uoutput[:((lettercount-len(uinput))*-1)-1]
            outputbox.delete("1.0",END)
            outputbox.insert("1.0",strip)
    #REDEFINE LETTERCOUNT
    lettercount = len(uinput)

#DEFINE BUTTONS FOR ROTOR SETTING
tk.Button(window, text ="➕", font = ("Calibri",12),command = lambda:rotincrement(1,False), activebackground = "Grey", activeforeground = "Grey").place(x=80, y=200)
tk.Button(window, text ="➕", font = ("Calibri",12),command = lambda:rotincrement(2,False), activebackground = "Grey", activeforeground = "Grey").place(x=130, y=200)
tk.Button(window, text ="➕", font = ("Calibri",12),command = lambda:rotincrement(3,False), activebackground = "Grey", activeforeground = "Grey").place(x=180, y=200)
tk.Button(window, text ="➖", font = ("Calibri",12), command = lambda:rotincrement(1,True), activebackground = "Grey", activeforeground = "Grey").place(x=80, y=310)
tk.Button(window, text ="➖", font = ("Calibri",12),command = lambda:rotincrement(2,True), activebackground = "Grey", activeforeground = "Grey").place(x=130, y=310)
tk.Button(window, text ="➖", font = ("Calibri",12),command = lambda:rotincrement(3,True), activebackground = "Grey", activeforeground = "Grey").place(x=180, y=310)
tk.Button(window, text="Save Wiring", font = ("Calibri",13),command = save, activebackground = "Grey", activeforeground = "Grey").place(x=440, y=328)

#MAIN LOOP
window.bind("<Key>", runencrypt)
runencrypt("<Key>")
window.mainloop()

#JIONSSXVTSPO 3,2,1
