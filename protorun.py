import random
import tkinter as tk
from tkinter import *

wbankE = ["WEARY", "AUDIO", "CHAMP", "REGAL", "JUICE"]
wbankH = ["EPOXY", "TOXIN", "SWOON", "FRITZ", "NICHE"]

difficulty = True

#D = str(input("hard or easy:"))
#d = D.lower()
#while difficulty == True:
    #*if d == "easy" or d == "hard":
        #print(f"difficulty set to {d}")
        #break
    #else:
        #d = str(input("please re-enter difficulty:"))

def bankselector(dih):
    if dih == "easy":
        bank = wbankE
        wordC = random.choice(wbankE)
    elif dih== "hard":
        bank = wbankH
        wordC = random.choice(wbankH)
    print(wordC)

#bankselector(d)

def Attempt(guess):
    if guess == wordC:
        print("correct")
    else:
        print("incorrect")

# a = input("guess")
# a = a.upper()
# Attempt(a)

#window/gui

def difficultyscreen():
   Dscreen = tk.Toplevel(window)
   Dscreen.title("Difficulty")
   Dscreen.grid()



window = tk.Tk()
window.title("BURDLE")
window.rowconfigure(0, weight=2)
window.rowconfigure(2)
window.rowconfigure(3)
window.columnconfigure(0, weight=2)
titlescreen = tk.Label(
    text = "Burdle \n [not wordle;)]",
    bg = "green",
    fg = "white",
    height=16,
    width=48,
    font=("Helvetica", 14, 'bold')
                      )
titlescreen.grid(row= 0, column = 0, sticky = "NEWS")
#entryfield
guiguess=tk.StringVar()
Wentry1 = tk.Entry( textvariable = guiguess)
Wentry1.grid(row = 1, column= 0, sticky="NEWS")
#button to check answer
submisionguess = tk.Button(window,text = "Submit")
submisionguess.grid(row= 2, column= 0, sticky= "NEWS")

difficultyscreen()

#loop runner
window.mainloop()
