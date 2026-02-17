import tkinter as tk
from tkinter import *
screen = tk.Tk()
ftop = tk.Frame()
title = tk.Label(
    master=ftop,
    text = "Burdle",
    bg = "green",
    fg = "white",
    height=32,
    width=64,
                )
title.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
ftop.pack()
screen.mainloop()

