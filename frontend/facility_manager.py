import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from backend.db import read_query, execute_query  # Assuming functions for database operations
from datetime import datetime  # To handle dates 

class FacilityManagerInterface(tk.Tk):
    def __init__(self, parent, first_name, last_name):
        super().__init__()
        self.title("Facility Manager Dashboard")
        self.geometry("1200x600")
        self.parent = parent
        self.first_name = first_name
        self.last_name = last_name

        self.create_widgets()
        self.load_requests()

    def create_widgets(self):
        # Header Frame
        self.header_frame = ttk.Frame(self)
        self.header_frame.pack(fill='x', padx=10, pady=10)

        # Logged-in User Label
        self.logged_in_label = ttk.Label(self.header_frame, text=f"Logged in as: {self.first_name} {self.last_name}", font=('Arial', 12))
        self.logged_in_label.pack(side='left')

        # Logout Button
        self.logout_button = ttk.Button(self.header_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side='right', pady=10)

        # Tab Control
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(fill='both', expand=True)

        # Request Management Tab
        self.requests_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.requests_tab, text='Requests')
        self.create_requests_tab()

        # Employee Management Tab
        self.employee_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.employee_tab, text='Manage Employee')
        self.create_employee_tab()

    def create_requests_tab(self):
        # Main Content Frame for Requests tab
        self.requests_main_frame = ttk.Frame(self.requests_tab)
        self.requests_main_frame.pack(fill='both', expand=True)

        # Frame for Treeview
        self.tree_frame = ttk.Frame(self.requests_main_frame)
        self.tree_frame.pack(fill='both', expand=True)

        # Define Treeview columns
        columns = ('req_id', 'room_id', 'description', 'assigned_to')
        self.treeview = ttk.Treeview(self.tree_frame, columns=columns, show='headings')
        self.treeview.pack(fill='both', expand=True)

        # Define headings
        self.treeview.heading('req_id', text='Request ID')
        self.treeview.heading('room_id', text='Room ID')
        self.treeview.heading('description', text='Description')
        self.treeview.heading('assigned_to', text='Assigned To')

        # Assign button
        self.assign_button = ttk.Button(self.requests_main_frame, text="Assign to Department", command=self.assign_request)
        self.assign_button.pack(pady=10)

        # Combobox for Department selection
        self.department_var = tk.StringVar()
        self.department_combobox = ttk.Combobox(self.requests_main_frame, textvariable=self.department_var, state='readonly')
        self.department_combobox.pack(pady=5)
        self.load_departments()

    def create_employee_tab(self):
        # Main Content Frame for Manage Employee tab
        self.employee_main_frame = ttk.Frame(self.employee_tab)
        self.employee_main_frame.pack(fill='both', expand=True)

        # Employee Listbox with Scrollbar
        self.employee_listbox = tk.Listbox(self.employee_main_frame, width=50, height=15)
        self.employee_scroll = ttk.Scrollbar(self.employee_main_frame, orient='vertical', command=self.employee_listbox.yview)
        self.employee_listbox.configure(yscrollcommand=self.employee_scroll.set)
        self.employee_listbox.pack(side='left', fill='y', pady=10)
        self.employee_scroll.pack(side='left', fill='y')

        # Button Frame for Add, Update, Delete
        self.button_frame = ttk.Frame(self.employee_main_frame)
        self.button_frame.pack(side='right', fill='both', expand=True, padx=20)

        self.add_button = ttk.Button(self.button_frame, text="Add New Employee", command=self.add_employee)
        self.add_button.pack(fill='x', pady=10) 
        self.delete_button = ttk.Button(self.button_frame, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack(fill='x', pady=10)

        self.load_employees_list()

    def load_requests(self):
        # Placeholder function to load requests
        query = "SELECT REQ_ID, ROOM_ID, REQ_DESCR FROM requestor"
        results = read_query(self.parent.db_connection, query)
        for result in results:
            self.treeview.insert('', 'end', values=(result['REQ_ID'], result['ROOM_ID'], result['REQ_DESCR'], ""))
            
    def load_departments(self):
        query = "SELECT FM_DEPTNAME FROM fm_department"
        results = read_query(self.parent.db_connection, query)
        departments = [result['FM_DEPTNAME'] for result in results]
        self.department_combobox['values'] = departments

    def assign_request(self):

        selected_item = self.treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a request to assign.")
            return

        selected_item = selected_item[0]  # Get the first selected item
        request_id = self.treeview.item(selected_item, 'values')[0]
        fm_department_name = self.department_combobox.get()
        if not fm_department_name:
            messagebox.showerror("Error", "Please select a department to assign.")
            return

        # Assuming function get_fm_department_id(fm_department_name) that fetches FM_ID based on the FM Department name
        fm_department_id = self.get_fm_department_id(fm_department_name)
        if fm_department_id is None:
            messagebox.showerror("Error", "Selected department is invalid.")
            return

        # Assuming current_user_id holds the ID of the logged-in facility manager
        current_user_id = self.get_current_user_id()  

        # SQL to insert a new task
        query = """
        INSERT INTO task (REQ_ID, ASSGND_BY_EMP_ID, FM_ID, TASK_DESC, TASK_SEVERITY, TASK_STATUS, TASK_STARTDT)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        task_description = "Assigned task based on facility manager's decision."
        task_severity = "Normal"  # Example severity
        task_status = "Open"
        task_start_date = datetime.now().strftime('%Y-%m-%d')

        try:
            execute_query(self.parent.db_connection, query, (request_id, current_user_id, fm_department_id, task_description, task_severity, task_status, task_start_date))
            messagebox.showinfo("Success", "Task assigned to department successfully")
            self.treeview.set(selected_item, column='assigned_to', value=fm_department_name)
        except Exception as e:
            messagebox.showerror("Error", "Failed to assign task: " + str(e))

    def get_fm_department_id(self, fm_department_name):
        query = "SELECT FM_ID FROM fm_department WHERE FM_DEPTNAME = %s"
        results = read_query(self.parent.db_connection, query, (fm_department_name,))
        return results[0]['FM_ID'] if results else None
    
    def get_current_user_id(self):
        # This function should return the current logged-in user's EMP_ID
        # Placeholder return value
        return 1  # Assuming 1 is the EMP_ID of the logged-in Facility Manager
    
    def logout(self):
        # Add logout functionality here
        self.destroy()  # Close the dashboard window
        # You can add code here to handle the logout action, such as returning to the login screen
    
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

    def load_employees_list(self):
        # Placeholder function to load active employees into the listbox
        query = "SELECT EMP_ID, EMP_FNAME, EMP_LNAME FROM employee WHERE IsActive = TRUE"
        results = read_query(self.parent.db_connection, query)
        self.employee_listbox.delete(0, tk.END)  # Clear existing entries before reloading
        for result in results:
            employee_entry = f"{result['EMP_ID']} - {result['EMP_FNAME']} {result['EMP_LNAME']}"
            self.employee_listbox.insert('end', employee_entry)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()  # Optionally hide the root window
    app = FacilityManagerInterface(root)
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
        return self.entries['global_id']  # initial focus on the Global ID field

    def apply(self):
        entry_values = {key: entry.get() for key, entry in self.entries.items()}
        # SQL to insert new employee
        columns = ', '.join(entry_values.keys())
        placeholders = ', '.join(['%s'] * len(entry_values))
        query = f"INSERT INTO employee ({columns}) VALUES ({placeholders})"
        execute_query(self.parent.parent.db_connection, query, tuple(entry_values.values()))
        self.parent.load_employees_list()
        