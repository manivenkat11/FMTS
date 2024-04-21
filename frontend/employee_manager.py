import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from backend.db import read_query, execute_query  # Assuming functions for database operations
from datetime import datetime  # To handle dates 

class EmployeeManagerInterface(tk.Toplevel):
    def __init__(self, parent, first_name, last_name, emp_id, fm_id):
        super().__init__(parent)
        self.title("Employee Manager Dashboard")
        self.geometry("1200x600")
        self.parent = parent
        self.first_name = first_name
        self.last_name = last_name
        self.emp_id = emp_id
        self.fm_id = fm_id

        # Configure styles
        self.style = ttk.Style(self)
        self.style.configure('Header.TFrame', background='#003366')  # A nice shade of blue
        self.style.configure('Header.TLabel', background='#003366', foreground='white', font=('Arial', 12))
        
        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
       # Header Frame with styled background
        self.header_frame = ttk.Frame(self, style='Header.TFrame')
        self.header_frame.pack(fill='x', padx=10, pady=10)

        # Logged-in User Label with styled font and background
        self.logged_in_label = ttk.Label(self.header_frame, text=f"Logged in as Employee Manager: {self.first_name} {self.last_name}", style='Header.TLabel')
        self.logged_in_label.pack(side='left')

        # Logout Button
        self.logout_button = ttk.Button(self.header_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side='right', pady=10)

        # Tab Control
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(fill='both', expand=True)

        # Task Management Tab
        self.tasks_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tasks_tab, text='Tasks')
        self.create_task_tab()

        # Employee Management Tab
        self.employee_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.employee_tab, text='Manage Employee')
        self.create_employee_tab()

    def create_task_tab(self):
        # Frame for Treeview
        self.tree_frame = ttk.Frame(self.tasks_tab)
        self.tree_frame.pack(fill='both', expand=True)

        # Define Treeview columns
        columns = ('task_id', 'request_id', 'description', 'assigned_to', 'status')
        self.treeview = ttk.Treeview(self.tree_frame, columns=columns, show='headings')
        self.treeview.pack(fill='both', expand=True)

        # Define headings
        self.treeview.heading('task_id', text='Task ID')
        self.treeview.heading('request_id', text='Request ID')
        self.treeview.heading('description', text='Description')
        self.treeview.heading('assigned_to', text='Assigned To')
        self.treeview.heading('status', text='Status')

        # Assign button
        self.assign_button = ttk.Button(self.tasks_tab, text="Assign to Employee", command=self.assign_task)
        self.assign_button.pack(side='left', padx=10, pady=10)

        # Combobox for Employee selection
        self.employee_var = tk.StringVar()
        self.employee_combobox = ttk.Combobox(self.tasks_tab, textvariable=self.employee_var, state='readonly')
        self.employee_combobox.pack(side='left', padx=10, pady=10)
        self.load_employees()

        # Update Status button
        self.update_button = ttk.Button(self.tasks_tab, text="Update Status", command=self.update_status)
        self.update_button.pack(side='left', padx=10, pady=10)

        # Combobox for Status selection
        self.status_var = tk.StringVar()
        self.status_combobox = ttk.Combobox(self.tasks_tab, textvariable=self.status_var, state='readonly')
        self.status_combobox['values'] = ['Open', 'In Progress', 'Resolved']
        self.status_combobox.pack(side='left', padx=10, pady=10)

    def create_employee_tab(self):
        # Frame for Employee management
        self.manage_employee_frame = ttk.Frame(self.employee_tab)
        self.manage_employee_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Employee Listbox with Scrollbar
        self.employee_listbox = tk.Listbox(self.manage_employee_frame, width=50, height=15)
        self.employee_scroll = ttk.Scrollbar(self.manage_employee_frame, orient='vertical', command=self.employee_listbox.yview)
        self.employee_listbox.configure(yscrollcommand=self.employee_scroll.set)
        self.employee_listbox.pack(side='left', fill='y', pady=10)
        self.employee_scroll.pack(side='left', fill='y')

        # Button Frame for Add, Update, Delete
        self.button_frame = ttk.Frame(self.manage_employee_frame)
        self.button_frame.pack(side='right', fill='both', expand=True, padx=20)

        self.add_button = ttk.Button(self.button_frame, text="Add New Employee", command=self.add_employee)
        self.add_button.pack(fill='x', pady=10) 
        self.delete_button = ttk.Button(self.button_frame, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack(fill='x', pady=10)

        self.load_employees_list()

    def load_employees_list(self):
        # Load only active employees into the listbox
        query = "SELECT EMP_ID, EMP_FNAME, EMP_LNAME FROM employee WHERE IsActive = TRUE"
        results = read_query(self.parent.db_connection, query)
        self.employee_listbox.delete(0, tk.END)  # Clear existing entries before reloading
        for result in results:
            employee_entry = f"{result['EMP_ID']} - {result['EMP_FNAME']} {result['EMP_LNAME']}"
            self.employee_listbox.insert('end', employee_entry)


    def add_employee(self):
        AddEmployeeDialog(self, title="Add New Employee")
 

    def delete_employee(self):
        selected = self.employee_listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "No employee selected")
            return
        selected_id = self.employee_listbox.get(selected[0]).split(' - ')[0]

        try:
            archive_query = "UPDATE employee SET IsActive = FALSE WHERE EMP_ID = %s"
            execute_query(self.parent.db_connection, archive_query, (selected_id,))
            messagebox.showinfo("Success", "Employee has been archived and is no longer active.")
            self.load_employees_list()  # Reload the list after archiving
        except Exception as e:
            messagebox.showerror("Error", f"Failed to archive employee: {str(e)}")
 

    def load_tasks(self):
        print(self.fm_id)
        # Placeholder function to load tasks assigned to the department
        query = "SELECT TASK_ID, REQ_ID, TASK_DESC, ASSGND_TO_EMP_ID, TASK_STATUS FROM task WHERE FM_ID = %s"
        results = read_query(self.parent.db_connection, query, (self.fm_id,))
        
        self.treeview.delete(*self.treeview.get_children())
        for result in results:
            assigned_to = self.get_employee_name(result['ASSGND_TO_EMP_ID']) if result['ASSGND_TO_EMP_ID'] else ""
            self.treeview.insert('', 'end', values=(result['TASK_ID'], result['REQ_ID'], result['TASK_DESC'], assigned_to, result['TASK_STATUS']))

    def load_employees(self):
        # Placeholder function to load employees with skills
        query = """
        SELECT e.EMP_ID, e.EMP_FNAME, e.EMP_LNAME, GROUP_CONCAT(s.SKILL_NAME) AS SKILLS
        FROM employee e
        LEFT JOIN employee_skill es ON e.EMP_ID = es.EMP_ID
        LEFT JOIN skill s ON es.SKILL_ID = s.SKILL_ID
        GROUP BY e.EMP_ID
        """
        results = read_query(self.parent.db_connection, query)
        employees = [(result['EMP_ID'], f"{result['EMP_FNAME']} {result['EMP_LNAME']} ({result['SKILLS']})") for result in results]
        self.employee_combobox['values'] = employees
    
    def assign_task(self):
        # Get the selected item in the Treeview
        selected_item = self.treeview.selection()[0]
        if not selected_item:
            messagebox.showerror("Error", "Please select a task to assign.")
            return

        task_id = self.treeview.item(selected_item, 'values')[0]
        employee_info = self.employee_var.get()
        if not employee_info:
            messagebox.showerror("Error", "Please select an employee to assign the task.")
            return

        employee_id, _ = employee_info.split(maxsplit=1)  # Extracting emp_id from the selected employee info

        # SQL to update task with assigned employee
        query = "UPDATE task SET ASSGND_TO_EMP_ID = %s WHERE TASK_ID = %s"
        try:
            execute_query(self.parent.db_connection, query, (employee_id, task_id))
            messagebox.showinfo("Success", "Task assigned to employee successfully")
            self.load_tasks()  # Reload tasks after assignment
        except Exception as e:
            messagebox.showerror("Error", "Failed to assign task: " + str(e))
        
    def update_status(self):
        # Get the selected item in the Treeview
        selected_item = self.treeview.selection()[0]
        if not selected_item:
            messagebox.showerror("Error", "Please select a task to update.")
            return

        task_id = self.treeview.item(selected_item, 'values')[0]
        new_status = self.status_var.get()

        if not new_status:
            messagebox.showerror("Error", "Please select a new status for the task.")
            return

        # SQL to update task status
        query = "UPDATE task SET TASK_STATUS = %s WHERE TASK_ID = %s"
        try:
            execute_query(self.parent.db_connection, query, (new_status, task_id))
            messagebox.showinfo("Success", "Task status updated successfully")
            self.load_tasks()  # Reload tasks after status update
        except Exception as e:
            messagebox.showerror("Error", "Failed to update task status: " + str(e))

    def get_category_id(self, department_name):
        query = "SELECT CAT_ID FROM category WHERE CAT_NAME = %s"
        results = read_query(self.parent.db_connection, query, (department_name,))
        return results[0]['CAT_ID'] if results else None

    def get_employee_name(self, emp_id):
        query = "SELECT EMP_FNAME, EMP_LNAME FROM employee WHERE EMP_ID = %s"
        result = read_query(self.parent.db_connection, query, (emp_id,))
        return f"{result[0]['EMP_FNAME']} {result[0]['EMP_LNAME']}" if result else ""

    def logout(self):
        # Add logout functionality here
        self.destroy()  # Close the dashboard window
        # You can add code here to handle the logout action
if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Optionally hide the root window
    app = EmployeeManagerInterface(root)
    app.mainloop()

        
class AddEmployeeDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title=title)

    def body(self, frame):
        # Define labels and entry widgets for each field
        labels = ['Global ID', 'Password', 'First Name', 'Last Name', 'Email', 'Contact', 'Role', 'Date of Joining', 'Address', 'Street', 'City', 'State', 'Zipcode']
        self.entries = {}
        for i, label in enumerate(labels):
            ttk.Label(frame, text=f"{label}:").grid(row=i, column=0, sticky='w')
            entry = ttk.Entry(frame)
            entry.grid(row=i, column=1, padx=10, pady=2)
            self.entries[label.lower().replace(' ', '_')] = entry
        return self.entries['global_id']  # initial focus on the global ID field

    def apply(self):
        entry_values = {key: entry.get() for key, entry in self.entries.items()}
        # SQL to insert new employee
        columns = ', '.join(entry_values.keys())
        placeholders = ', '.join(['%s'] * len(entry_values))
        query = f"INSERT INTO employee ({columns}) VALUES ({placeholders})"
        execute_query(self.parent.db_connection, query, tuple(entry_values.values()))
        self.parent.load_employees_list()
 
 
