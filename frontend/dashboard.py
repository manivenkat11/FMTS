import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Task Dashboard 1").pack()
        self.task_list = tk.Listbox(self)
        self.task_list.pack()

        self.refresh_button = tk.Button(self, text="Refresh Tasks", command=self.refresh_tasks)
        self.refresh_button.pack()

    def refresh_tasks(self):
        # This function would fetch task data from an API
        self.task_list.delete(0, tk.END)
        self.task_list.insert(tk.END, "Task 1 - Pending")
        self.task_list.insert(tk.END, "Task 2 - Completed")
