# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:49:39 2022

@author: Swasti
"""

from tkinter import*
import random
root = Tk()
root.title("Colour Changer")
root.geometry("600x400")

colourArray = ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]

colourDictionary = {'colour': colourArray}

def bg():
    randomNo = random.randint(0, 7)
    randomColour = colourDictionary['colour'][randomNo]
    root.configure(background = randomColour)
    
button = Button(root, text = "Random Colour", command = bg)
button.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()