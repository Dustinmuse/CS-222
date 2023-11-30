import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.geometry('500x300')
window.title("Third Python GUI")
combo = Combobox(window)
combo['values'] = ("IN", "CA", "MA") # all items in drop down box
combo.current(1) #sets a default option from the list of 'values'

combo.grid(column = 0, row = 0)

window.mainloop()