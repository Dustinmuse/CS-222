import tkinter as tk

class Todo:
    #root = window
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List")
        self.tasks = []
        #Entry = textbox
        self.taskEntry = tk.Entry(root, width = 50)
        self.addButton = tk.Button(root, text = "Add Task", command = self.addTask)
        self.taskList = tk.Listbox(root, selectmode = tk.SINGLE, width = 50)
        self.deleteButton = tk.Button(root, text = "Delete Task", command = self.deleteTask)

        self.taskEntry.pack()
        self.addButton.pack()
        self.taskList.pack()
        self.deleteButton.pack()

    def addTask(self):
        task = self.taskEntry.get()
        #if task has a value
        if task:
            self.tasks.append(task)
            self.UpdateTaskList()
            #deletes previous added tasks, so they are not multiplying
            self.taskEntry.delete(0, tk.END)

    def deleteTask(self):
        #only able to select 1 item
        selectedIndex = self.taskList.curselection()
        #if there is a value selected
        if selectedIndex:
            self.tasks.pop(selectedIndex[0])
            self.UpdateTaskList()

    def UpdateTaskList(self):
        #clears the textbox out after adding
        self.taskList.delete(0, tk.END)
        for task in self.tasks:
            self.taskList.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = Todo(root)
    root.mainloop()