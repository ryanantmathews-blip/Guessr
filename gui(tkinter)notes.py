import tkinter as tk
from tkinter import *

#correct_words = ['SIGMA', 'PLACE', 'SHINE', 'IDEAS']
z = 12
#textinput = input("what do you want to say")

screen = Tk() # makes window

#screentext = tk.Label(
    #text = "ohio", #str(textinput)
    #background = "white",
    ##foreground = "black",
   # width = 25,
    #height = 20
               #)
#screentext.pack() #these two lines allow text/colors to be shown on screen

# f1 = tk.Button(
   # text = "click ",
 #   fg = "Black",
#  bg = "white",
  #  height = 10,
  #  width = 25,
 #            )
#f1.pack()
#
#button

#labelq = tk.Label(text = "Put ur goon documents here lmao", height= z, width= 40)
#labelq.pack() #makes the question seen above
#entry = tk.Entry() #creates entry field
#entry.pack() # entry is great for getting small amount of texts (1 line)
#responseq = entry.get()
#entry.insert(0, "hello user")

bt1 = tk.Text(master=screen, height = 12, width = 12)
bt1.pack(side=tk.BOTTOM, expand=True) # pack expresses configuration
#t = bt1.get("1.0", "4.9")
block = tk.Label(height = 12, width = 12,  bg = "light gray")
block.pack(side = tk.RIGHT, expand = True)




screen.mainloop() # allows for window to stay up and get updated