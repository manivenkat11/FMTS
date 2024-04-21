import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from backend.db import read_query, execute_query  # Assuming functions for database operations
from datetime import datetime  # To handle dates 

class EmployeeTaskInterface(tk.Toplevel):
    def __init__(self, parent, emp_id):
        super().__init__(parent)
        self.parent = parent
        self.emp_id = emp_id
        self.title("Employee Task Dashboard")
        self.geometry("1000x600")

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        # Frame for Task Listing
        self.task_frame = ttk.Frame(self)
        self.task_frame.pack(fill='both', expand=True, pady=10)

        # Define Treeview for tasks
        self.treeview = ttk.Treeview(self.task_frame, columns=('task_id', 'description', 'status'), show='headings')
        self.treeview.heading('task_id', text='Task ID')
        self.treeview.heading('description', text='Description')
        self.treeview.heading('status', text='Status')
        self.treeview.pack(fill='both', expand=True)

        # Status update Combobox
        self.status_var = tk.StringVar()
        self.status_combobox = ttk.Combobox(self, textvariable=self.status_var, state='readonly', values=['Open', 'In Progress', 'Resolved'])
        self.status_combobox.pack(side='left', padx=10, pady=10)

        # Update Button
        self.update_button = ttk.Button(self, text="Update Status", command=self.update_status)
        self.update_button.pack(side='right', padx=10, pady=10)

    def load_tasks(self):
        query = "SELECT TASK_ID, TASK_DESC, TASK_STATUS FROM task WHERE ASSGND_TO_EMP_ID = %s"
        results = read_query(self.parent.db_connection, query, (self.emp_id,))
        self.treeview.delete(*self.treeview.get_children())
        for result in results:
            self.treeview.insert('', 'end', values=(result['TASK_ID'], result['TASK_DESC'], result['TASK_STATUS']))

    def update_status(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a task to update.")
            return
        task_id = self.treeview.item(selected_item, 'values')[0]
        new_status = self.status_var.get()
        if not new_status:
            messagebox.showerror("Error", "Please select a new status for the task.")
            return
        query = "UPDATE task SET TASK_STATUS = %s WHERE TASK_ID = %s"
        try:
            execute_query(self.parent.db_connection, query, (new_status, task_id))
            messagebox.showinfo("Success", "Task status updated successfully")
            self.load_tasks()  # Refresh the task list
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update task status: {str(e)}")


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Optionally hide the root window
    app = EmployeeTaskInterface(root)
    app.mainloop()

        
 
