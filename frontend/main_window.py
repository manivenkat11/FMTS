import tkinter as tk
from tkinter import ttk, messagebox
from backend.db import read_query, create_db_connection, execute_query  # Import database functions
import re  # Import regular expressions for validation 
from datetime import datetime  # To handle dates
from frontend.facility_manager import FacilityManagerInterface
from frontend.employee_manager import EmployeeManagerInterface
from frontend.employee import EmployeeTaskInterface

class RequestForm(tk.Frame):
     
    def __init__(self, parent):
        super().__init__(parent, bg='#f0f0f0')
        self.db_connection = create_db_connection()
        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self, text="CMU Facilities Management", bg='#003366', fg='white', font=("Helvetica", 18))
        header.pack(fill='x')

        title = tk.Label(self, text="Submit a New Request", font=("Helvetica", 16), bg='#f0f0f0')
        title.pack(pady=(20, 10))

        self.room_id_var = tk.StringVar(self)
        ttk.Label(self, text="Room ID:").pack()
        self.room_id_dropdown = ttk.Combobox(self, textvariable=self.room_id_var, state='readonly')
        self.room_id_dropdown.pack(fill='x', padx=20, pady=(10, 5))
        # Set the default value for the Combobox
        self.fetch_room_ids()

        fields = ['Global ID', 'First Name', 'Last Name', 'Email', 'Phone']
        self.entries = {field: ttk.Entry(self, font=('Helvetica', 14)) for field in fields}
        for field, entry in self.entries.items():
            ttk.Label(self, text=f"{field}:").pack()
            entry.pack(fill='x', padx=20, pady=(10, 5))  

        ttk.Label(self, text="Description:").pack()
        self.desc_text = tk.Text(self, height=5)
        self.desc_text.pack(fill='x', padx=20, pady=5)

        button_frame = tk.Frame(self, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=20)
        ttk.Button(button_frame, text="Create Request", command=self.create_request).pack(side='left', padx=10, expand=True)
        ttk.Button(button_frame, text="Clear Form", command=self.clear_form).pack(side='right', padx=10, expand=True)

    def create_request(self):
        if self.validate_form():
            room_display = self.room_id_var.get()
            room_id, build_id, floor_id, build_name, floor_no, room_no = self.room_details[room_display]
            data = {field: entry.get() for field, entry in self.entries.items()}
            data.update({
                'Description': self.desc_text.get("1.0", "end-1c"),
                'Room ID': room_id,
                'BUILD_ID': build_id,
                'FLOOR_ID': floor_id,
                'BUILD_NAME': build_name,
                'FLOOR_NO': floor_no,
                'ROOM_NO': room_no
            })
            self.submit_request_to_db(data)
            messagebox.showinfo("Request Created", "The request has been created successfully!")
            self.clear_form()
            
    def clear_form(self):
        # Reset all entry fields
        for entry in self.entries.values():
            if isinstance(entry, tk.StringVar):  # This is for the combobox
                if self.room_id_dropdown['values']:
                    entry.set(self.room_id_dropdown['values'][0])  # Reset to first room display
            elif isinstance(entry, tk.Entry):  # Standard entry fields
                entry.delete(0, tk.END)

        # Reset the description text area
        self.desc_text.delete('1.0', tk.END)

    def fetch_room_ids(self):
        # Fetching room, floor, and building IDs along with their descriptive names
        query = """
        SELECT r.ROOM_ID, CONCAT(b.BUILD_NAME, '/', f.FLOOR_NO, '/', r.ROOM_NO) AS ROOM_DISPLAY,
            b.BUILD_ID, b.BUILD_NAME, f.FLOOR_ID, f.FLOOR_NO, r.ROOM_NO
        FROM room r
        JOIN floor f ON r.FLOOR_ID = f.FLOOR_ID
        JOIN building b ON f.BUILD_ID = b.BUILD_ID
        """
        result = read_query(self.db_connection, query)
        self.room_details = {room['ROOM_DISPLAY']: (room['ROOM_ID'], room['BUILD_ID'], room['FLOOR_ID'], room['BUILD_NAME'], room['FLOOR_NO'], room['ROOM_NO']) for room in result}
        dropdown_values = ["Select Room"] + list(self.room_details.keys())
        self.room_id_dropdown['values'] = dropdown_values
        self.room_id_var.set("Select Room")
        if self.room_id_dropdown['values']:
            self.room_id_var.set(self.room_id_dropdown['values'][0])
            
    def submit_request_to_db(self, data):
        # SQL INSERT statement with BUILD_ID and FLOOR_ID
        query = """
        INSERT INTO requestor (ROOM_ID, REQ_GLOBALID, REQ_FNAME, REQ_LNAME, REQ_EMAIL, REQ_PHONE, REQ_DATE, REQ_DESCR, BUILD_ID, FLOOR_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        today_date = datetime.now().strftime('%Y-%m-%d')  # Formats today's date as YYYY-MM-DD
        values = (
            data['Room ID'], data['Global ID'], data['First Name'], data['Last Name'],
            data['Email'], data['Phone'], today_date, data['Description'],
            data['BUILD_ID'], data['FLOOR_ID']
        )
        execute_query(self.db_connection, query, values)  # Execute the SQL command
        print("Data inserted successfully into the database.")

    def validate_form(self):
        # Validation for each field
        global_id = self.entries['Global ID'].get()
        if not (re.match("^[a-zA-Z0-9]+$", global_id) or re.match("^\S+@\S+\.\S+$", global_id)):
            messagebox.showerror("Invalid Input", "Global ID must be either alphanumeric or a valid email.")
            return False
        if not re.match("^[a-zA-Z]+$", self.entries['First Name'].get()):
            messagebox.showerror("Invalid Input", "First Name must contain only letters.")
            return False
        if not re.match("^[a-zA-Z]+$", self.entries['Last Name'].get()):
            messagebox.showerror("Invalid Input", "Last Name must contain only letters.")
            return False
        if not re.match("^\S+@\S+\.\S+$", self.entries['Email'].get()):
            messagebox.showerror("Invalid Input", "Email format is invalid.")
            return False
        if not re.match("^\d{10}$", self.entries['Phone'].get()):
            messagebox.showerror("Invalid Input", "Phone number must be 10 digits.")
            return False
        if len(self.desc_text.get("1.0", "end-1c")) > 300:
            messagebox.showerror("Invalid Input", "Description must not exceed 300 characters.")
            return False
        return True
  
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CMU Facilities Management Task System')
        self.geometry('1024x720')
        self.configure(bg='#003366')  # Dark blue background

        self.db_connection = create_db_connection()

        tab_control = ttk.Notebook(self, style='TButton.TNotebook')
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Request Form')
        self.request_form = RequestForm(tab1)
        self.request_form.pack(expand=True, fill='both', padx=20, pady=20)

        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Employee Login')
        self.login_form = self.create_login_form(tab2)
        self.login_form.pack(expand=True, fill='both')

        tab_control.pack(expand=1, fill="both")

    def create_login_form(self, parent): 
        frame = tk.Frame(parent, bg='#003366')  # Updated to blue background
        frame.pack(fill='both', expand=True)  # Make the frame expand to fill the window

        # Header with application title, could be reused in other parts of the application
        header = tk.Label(frame, text="CMU Facilities Management Task System", bg='#003366', fg='white', font=("Helvetica", 18))
        header.pack(fill='x', pady=(10, 20))

        title = tk.Label(frame, text="Employee Login", font=("Helvetica", 16), bg='#003366', fg='white')
        title.pack(pady=10)

        # Centering frame for the form elements
        center_frame = tk.Frame(frame, bg='#003366')
        center_frame.pack()

        # Username Entry
        username_label = tk.Label(center_frame, text="Email:", bg='#003366', fg='white', font=("Helvetica", 12))
        username_label.pack(pady=(5, 2))
        self.username_entry = tk.Entry(center_frame, font=('Helvetica', 12), relief='ridge', bd=2, width=30)
        self.username_entry.pack()

        # Password Entry
        password_label = tk.Label(center_frame, text="Password:", bg='#003366', fg='white', font=("Helvetica", 12))
        password_label.pack(pady=(5, 2))
        self.password_entry = tk.Entry(center_frame, show="*", font=('Helvetica', 12), relief='ridge', bd=2, width=30)
        self.password_entry.pack()

        # Login Button
        login_button = ttk.Button(center_frame, text="Login", style='TButton', cursor='hand2', command=self.validate_login)
        login_button.pack(pady=20)

        return frame


    def validate_login(self):
        email = self.username_entry.get()
        password = self.password_entry.get()
        print("Email:", email, "Password:", password)
        query = "SELECT EMP_PASSWORD, EMP_ROLE FROM employee WHERE EMP_EMAIL = %s"
        result = read_query(self.db_connection, query, (email,))
        if result:
            print("Query successful, result:", result)
            if result[0]['EMP_PASSWORD'] == password:
                self.role = result[0]['EMP_ROLE']
                print("Password match, role:", self.role)
                self.login_success()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
                print("Password mismatch")
        else:
            messagebox.showerror("Login Failed", "User not found")
            print("Query returned no results")


    def login_success(self):
        print("Login success, opening window for role:", self.role)
        first_name, last_name = self.get_employee_name(self.username_entry.get())
        if self.role == 'Facilities Manager':
            # Assuming the first name and last name are retrieved from the database after successful login
            self.open_facility_manager_interface(first_name, last_name)
        elif self.role == 'Employee Manager':
            self.open_employee_manager_interface(first_name, last_name)
        elif self.role == 'Employee':
            self.open_employee_interface()
        else:
            print("Role not recognized:", self.role)

    def get_employee_name(self, email):
        query = "SELECT EMP_FNAME, EMP_LNAME FROM employee WHERE EMP_EMAIL = %s"
        result = read_query(self.db_connection, query, (email,))
        if result:
            return result[0]['EMP_FNAME'], result[0]['EMP_LNAME']
        else:
            return None, None

    def open_facility_manager_interface(self, first_name, last_name):
        fm_window = FacilityManagerInterface(self, first_name, last_name)
        fm_window.grab_set() 

    def open_employee_manager_interface(self, first_name, last_name):
        email = self.username_entry.get()
        print("Opening Employee Manager Interface for:", email)
        emp_id, fm_id = self.get_employee_manager_ids(email)
        print("Employee ID and FM ID:", emp_id, fm_id)
        em_window = EmployeeManagerInterface(self, first_name, last_name, emp_id, fm_id) 
        em_window.grab_set() 
        
    def get_employee_manager_ids(self, email):
        # Fetch EMP_ID and FM_ID for the logged-in Employee Manager
        query = """
        SELECT e.EMP_ID, ed.FM_ID
        FROM employee e
        JOIN emp_department ed ON e.EMP_ID = ed.EMP_ID
        WHERE e.EMP_EMAIL = %s
        """
        result = read_query(self.db_connection, query, (email,))  # Ensure email is passed as a tuple
        print("Query result:", result)
        if result and len(result) > 0:
            return result[0]['EMP_ID'], result[0]['FM_ID']
        else:
            return None, None
 
    def open_employee_interface(self):
        email = self.username_entry.get()
        print("Opening Employee Task Interface for:", email)
        emp_id = self.get_employee_id(email)
        print("Employee ID:", emp_id)
        emp_window = EmployeeTaskInterface(self, emp_id)
        emp_window.grab_set()

    def get_employee_id(self, email):
        """
        Fetches the employee ID for a given email.

        Args:
        email (str): The email of the employee.

        Returns:
        int: The employee ID, or None if not found.
        """
        query = "SELECT EMP_ID FROM employee WHERE EMP_EMAIL = %s"
        result = read_query(self.db_connection, query, (email,))
        if result:
            return result[0]['EMP_ID']  # Assuming EMP_ID is the first column in the result
        else:
            return None
    
if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
    # Close the database connection after the main loop ends
    app.db_connection.close()
