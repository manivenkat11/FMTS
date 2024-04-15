import tkinter as tk

class TaskForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Submit a New Task").pack()

        self.title_entry = tk.Entry(self)
        self.title_entry.pack()
        self.description_entry = tk.Entry(self)
        self.description_entry.pack()
        self.status_entry = tk.Entry(self)
        self.status_entry.pack()
        self.assigned_to_entry = tk.Entry(self)
        self.assigned_to_entry.pack()

        self.submit_button = tk.Button(self, text="Submit Task", command=self.submit_task)
        self.submit_button.pack()

    def submit_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        status = self.status_entry.get()
        assigned_to = self.assigned_to_entry.get()
        # Here we would call an API to submit this data
        print("Task Submitted:", title, description, status, assigned_to)
