#graphical user interface

import tkinter as tk   #package apart of python

window = tk.Tk()  #makes a window

hello = tk.Label(text = "Hello World")   #makes a label saying Hello World
welcome = tk.Label(text = "Welcome to CS 222", foreground = "white", background = "black") #makes letters white and background black
#clickMe = tk.Button(text = "Ok", width = 25, height = 7, fg = "blue", bg = "yellow") #fg = foreground | bg = background
clickMe = tk.Button(text = "Ok", width = 10, height = 3)
hello.pack()  #adds hello to the window
welcome.pack()
clickMe.pack()

window.mainloop()   #runs the window