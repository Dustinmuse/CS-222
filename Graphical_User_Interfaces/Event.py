import tkinter as tk

window = tk.Tk()

window.title("Second Python GUI")
window.geometry('500x300')  #width x height   |    makes the size of the window
lbl = tk.Label(window, text = "Ok")  #specifies lbl to the variable window incase there are multiple windows
txt = tk.Entry(window, width = 10)   #makes a text entry box for only 10 characters

def clicked(): # must be defined before line 14 (when it is used)
    result = "Welcome " + txt.get()  # get you the text from the text box (what is entered by user)
    lbl.configure(text = result)     # overrides the Ok and makes it say Welcome + whatever was entered in text box

btn = tk.Button(window, text = "Welcome", command = clicked)



lbl.grid(column = 0, row = 0)   #similar to pack() but able to choose where you want the variable lbl to be in the window
txt.grid(column = 1, row = 0)
btn.grid(column = 2, row = 0)

window.mainloop()