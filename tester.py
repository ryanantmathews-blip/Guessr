import tkinter as tk
from tkinter import *
import random

wbankE = ["WEARY", "AUDIO", "CHAMP", "FRITZ", "JUICE"]
wbankH = ["EPOXY", "TOXIN", "SWOON", "REGAL", "NICHE"]
wbankc = wbankH + wbankE

#functions for i/o
def Attempt(guess):
    for x in wbankc:
        if guess == x:
            Wentry1.delete(0, 15)
            Wentry1.insert(1, f" {guess} is correct")
            break
        else:
            Wentry1.delete(0,15)
            Wentry1.insert(1, f" {guess} is incorrect")

def gettext():
    guiin = str(Wentry1.get())
    ATI = guiin.upper()
    Attempt(ATI)

#make function to clear i/o from entry
#window/gui
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
submisionguess = tk.Button(window,text = "Submit", command= gettext)
submisionguess.grid(row= 2, column= 0, sticky= "NEWS")
#loop runner
window.mainloop()



