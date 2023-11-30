import tkinter as tk

window = tk.Tk()

def decrease():
    result = int(lblCounter["text"])
    result -= 1
    lblCounter.configure(text = result) #dont need to cast result as a string
def increase():
    result = int(lblCounter["text"])
    result += 1
    lblCounter.configure(text = result)
    #lblCounter["text"] = result    #another way of doing it

window.title("Counter")
window.geometry('300x200')

btnDecrease = tk.Button(window, text = "-", command = decrease)
lblCounter = tk.Label(window, text = "0")
btnIncrease = tk.Button(window, text = "+", command = increase)

btnDecrease.grid(column = 0, row = 0)
lblCounter.grid(column = 1, row = 0)
btnIncrease.grid(column = 2, row = 0)

window.mainloop()