import tkinter as tk
import random as rnd
from itertools import cycle
import os as os
import sys as sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# HEY! THATS CHEATING! PRESS RUN ABOVE ^^^^^^
wbankE = ["DRIFT", "AUDIO", "CHAMP", "FRITZ", "JUICE", "APPLE", "BRICK", "CLOUD", "FLAME", "GHOST", "HEART", "LIGHT", "MAGIC", "NIGHT", "PLANT","SHINE",]
wbankH = ["EPOXY", "TOXIN", "SWOON", "REGAL", "NICHE", "RIVER", "STONE", "TABLE", "UNITY", "VOICE", "WATER", "WORLD", "YOUTH", "ZEBRA","BLADE", "WEARY",]
wbankc = wbankH + wbankE

# window stuff and r/c weights 
window = tk.Tk()
window.title("Guessr")
icon_path = os.path.join('assets', "guessr_window_icon_192.png")
icon = tk.PhotoImage(file=icon_path)
window.wm_iconphoto(False, icon)
window.geometry("960x540")
window.rowconfigure(0, weight=2)
window.rowconfigure(1, weight=1)
window.rowconfigure(2)
window.rowconfigure(3)
window.columnconfigure(0, weight=2)
window.columnconfigure(1)
window.columnconfigure(2)
window.columnconfigure(3)
window.resizable(True, True)


# functions for i/o

def dele():
    Wentry1.delete(0, 190)

def gettext():
    guiin = str(Wentry1.get()).upper()
    Attempt(guiin)

def selector():
    z = rnd.randint(0, 31)
    wordTsolve = wbankc[z]
    wts = list(wordTsolve)
    return wts

wtslst = selector()

def Attempt(guess):
    global a
    if list(guess) == wtslst:
        a = 0
    else:
        a = 1
    if a == 0:
        print("correct")
        Wentry1.delete(0, 150)
        Wentry1.insert(10,
"correct                                                                                                                                             ")

    else:
        print("incorrect")
        Wentry1.delete(0, 150)
        Wentry1.insert(10, "incorrect")

def cor_status():
    if str(Wentry1.get()).upper() == \
"CORRECT                                                                                                                                             ":
        cor = True
        print(str(Wentry1.get()).upper(), 'is true: user can go to next page')
        return cor
    else:
        cor = False
        print(str(Wentry1.get()).upper(), "user cant go to next page")
        return cor

def Reset():
    python = sys.executable
    os.execv(python, [python] + sys.argv)

        # page3 (reset)

blank = tk.Label(window, text = "Congrats!""\n""\n""\n"
                                "If you would like to play another round""\n""\n"
                                "press the New Game button!   ➜""\n""\n",

                                fg= "white", bg= "grey", font=("Helvetica", 25, 'bold'))
blank.grid(row= 0, column= 0, rowspan= 4,  columnspan= 2, sticky= "NEWS")

reset = tk.Button(window, text= 'N'"\n""e""\n""w""\n""\n""G""\n""a""\n""m""\n""e""\n""\n""?",
                          command= Reset,font=("Helvetica", 20, 'bold'))
reset.grid(row= 0, column= 1, rowspan= 4, sticky= "NEWS")
# ^^^^^^
page3 = [blank, reset]

def GTpage3():
    cor = cor_status()
    if cor == True:
        for j in page3:
            j.lift()

        # actual game play (page 2)

# entryfield
Wentry1 = tk.Entry( font=("Helvetica", 17,))
Wentry1.grid(row=2, column=0, sticky="NEWS")

# button to check answer
submit = tk.Button(window, text="Submit", command=gettext, font=("Arial", 17, "italic"))
submit.grid(row=3, column=0, sticky="NEWS", columnspan=1)

# button to clear text
clear = tk.Button(window, text="Clear", command=dele, font=("Arial", 16, "bold"))
clear.grid(row=2, column=1, sticky="NEWS")

# filler
f_img_path = os.path.join("assets", "otherguessr_icon@136px.png")
f_img = tk.PhotoImage(file=f_img_path)
filler = tk.Label(window, image=f_img)
filler.grid(row=1, column=1, sticky="NS")

# Title screen stuff
titlescreen = tk.Label(
    text="Guessr""\n""(╯°o°）╯︵ ┻━┻",
    bg="#00cc7a",
    fg="white",
    font=("Helvetica", 25, 'bold')
                      )
titlescreen.grid(row=0, column=0, sticky="NEWS", )


# hint function and dependencies
def pds1():
    pdisp.configure(text=f"{wtslst[0]} _ {wtslst[2]} _ {wtslst[4]}")


def pds2():
    pdisp.configure(text=f"{wtslst[0]} _ {wtslst[2]}  {wtslst[3]} {wtslst[4]}")


def pds3():
    pdisp.configure(
        text=f"You lost!""\n""The word was:""\n"f"{wtslst[0]} {wtslst[1]} {wtslst[2]} {wtslst[3]} {wtslst[4]}")


pdsC = cycle([pds1, pds2, pds3])


def hint():
    next(pdsC)()  # <- do not delete this


# hints button
hints = tk.Button(window, text='H'"\n""I""\n""N""\n""T""\n""?", command=hint, font=("Arial", 16))
hints.grid(row=0, column=1, sticky="NEWS", )

# play display
pdisp = tk.Label(text=f"{wtslst[0]} _ _ _ {wtslst[4]}", bg="#00cc7a", fg="white", font=("Arial", 30))
pdisp.grid(row=1, column=0, sticky="NEWS")

# next button func
page2 = [Wentry1, submit, clear, titlescreen, hints, filler, pdisp]


def GTpage2():  # should go between pages
    for i in page2:
        i.lift()
        pageturner.configure(command= GTpage3)


    # rules (page 1)

rules = tk.Label(
    master = window,
    text="                    Welcome To Guessr!""\n""\n""\n"
         "                    RULES:""\n""\n"
         "                    1. Guess a 5 letter word""\n""\n"
         "                    2. Stuck? Use hints! ""\n""\n"
         "                    3. If you use all 3 hints you lose!""\n""\n"""
         "                    4. Once you guess is correct""\n"
         "                    press the Next button!",
    bg="#4d4d4d",
    fg="white",
    font=("Helvetica", 25, 'bold')
)
rules.grid(row=0, column=0, sticky="NEWS", rowspan=4)
tk.Label(bg="#4d4d4d").grid(row=0, column=1, sticky="NEWS", rowspan=4)

# page turn button/next
pageturner = tk.Button(window, text="Next", command=GTpage2, font=("Arial", 12, "bold"))
pageturner.grid(row=3, column=1, sticky="NEWS")

# loop runner
window.mainloop()
