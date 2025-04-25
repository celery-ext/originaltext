# TODOapp
#----------------------
import tkinter as tk

# todoapp's class
class ToDoApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # label entry frame
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        tk.Label(self, text="Task: ").grid(row=0, column=0)
        task_entry = tk.Entry(self, width=30)
        task_entry.grid(row=0, column=1)

        # add button frame
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Add Task", command=self.add_task).pack(side="left")
        tk.Button(btn_frame, text="Delete Task", command=self.delete_task).pack(side="left")

        # tasklist box
        self.task_list = tk.Listbox(self, selectmode="multiple", bd=10)
        self.task_list.pack(fill="both", expand=True)

        # task list
        self.task = []
    
    # add task
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task.append(task)
            self.task_list.insert("end", task)
            self.task_entry.delete(0, "end")

    #delete task
    def delete_task(self):
        selected_indices = self.task_list.curselection()
        for index in selected_indices[::-1]:
            self.task_list.delete(index)
            self.task.pop(index)


# # boot todo app
# if __name__ =="__main__":
#     app = ToDoApp.__init__(mainframe)
#     app.mainloop()