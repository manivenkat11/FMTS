import tkinter as tk
from tkinter import ttk, messagebox
from backend.db import read_query, create_db_connection, execute_query  # Import database functions
import re  # Import regular expressions for validation 
from datetime import datetime  # To handle dates

class RequestForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#f0f0f0')  # Light gray background
        # Initialize the database connection
        self.db_connection = create_db_connection()
        print("Database connection established successfully!")
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self, text="Submit a New Request", font=("Helvetica", 16), bg='#f0f0f0')
        title.grid(row=0, column=0, columnspan=2, pady=20)

        # Room ID Dropdown
        self.room_id_var = tk.StringVar(self)
        room_id_label = tk.Label(self, text="Room ID:", bg='#f0f0f0', anchor='w', width=20)
        room_id_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.room_id_dropdown = ttk.Combobox(self, textvariable=self.room_id_var, state='readonly', width=47)
        self.room_id_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
        self.fetch_room_ids()

        # Form fields
        fields = ['Global ID', 'First Name', 'Last Name', 'Email', 'Phone']
        self.entries = {}
        self.entries["Room ID"] = self.room_id_var
        # Adjust the starting row index for fields to avoid overlap with Room ID Dropdown
        start_row_index = 2
        for idx, field in enumerate(fields):
            label = tk.Label(self, text=f"{field}:", bg='#f0f0f0', anchor='w', width=20)
            label.grid(row=idx + start_row_index, column=0, padx=10, pady=5, sticky='w')
            entry = tk.Entry(self, width=50, relief='ridge', bd=2)  # Slightly rounded and increased width
            entry.grid(row=idx + start_row_index, column=1, padx=10, pady=5, sticky='ew')
            self.entries[field] = entry

        # Description field as a Text widget
        desc_label = tk.Label(self, text="Description:", bg='#f0f0f0', anchor='w', width=20)
        desc_label.grid(row=len(fields) + start_row_index, column=0, padx=10, pady=5, sticky='w')
        self.desc_text = tk.Text(self, height=5, width=50, relief='ridge', bd=2)  # Slightly rounded and increased width
        self.desc_text.grid(row=len(fields) + start_row_index, column=1, padx=10, pady=5, sticky='ew')

        # Create Request Button with style
        submit_button = ttk.Button(self, text="Create Request", command=self.create_request, style='Primary.TButton')
        submit_button.grid(row=len(fields) + start_row_index + 1, column=0, padx=5, pady=20)
        
        # Clear Form Button
        clear_button = ttk.Button(self, text="Clear Form", command=self.clear_form, style='Secondary.TButton')
        clear_button.grid(row=len(fields) + start_row_index + 1, column=1, padx=5, pady=20)

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
        self.room_id_dropdown['values'] = list(self.room_details.keys())
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
        self.geometry('800x600')
        # Create database connection
        self.db_connection = create_db_connection()

        # Create Tab Control with custom style
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12))  # Custom button style
        style.map('TButton',
                  foreground=[('pressed', 'black'), ('active', 'black')],
                  background=[('pressed', '!disabled', 'gray'), ('active', 'gray')])

        style.configure('Primary.TButton', foreground='black', background='sky blue', font=('Helvetica', 12))
        style.configure('Secondary.TButton', foreground='black', background='gray', font=('Helvetica', 12))

        tab_control = ttk.Notebook(self, style='TButton.TNotebook')

        # Tab 1: Requests (Using the RequestForm class)
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Request Form', padding=(10, 5))
        self.request_form = RequestForm(tab1)
        self.request_form.pack(expand=True, fill='both', padx=20, pady=20)

        # Tab 2: Employee Login
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Employee Login', padding=(10, 5))
        self.login_form = self.create_login_form(tab2)
        self.login_form.pack(expand=True, fill='both')

        # Pack the tab control to the main window
        tab_control.pack(expand=1, fill="both")

    def create_login_form(self, parent):
        frame = tk.Frame(parent, bg='#f0f0f0')  # Light gray background
        title = tk.Label(frame, text="Employee Login", font=("Helvetica", 16), bg='#f0f0f0')
        title.pack(pady=20)

        # Username
        username_label = tk.Label(frame, text="Username:", bg='#f0f0f0')
        username_label.pack()
        username_entry = tk.Entry(frame, relief='ridge', bd=2, width=40)  # Slightly rounded and increased width
        username_entry.pack()

        # Password
        password_label = tk.Label(frame, text="Password:", bg='#f0f0f0')
        password_label.pack()
        password_entry = tk.Entry(frame, show="*", relief='ridge', bd=2, width=40)  # Slightly rounded and increased width
        password_entry.pack()

        # Login Button with style
        login_button = ttk.Button(frame, text="Login", style='Secondary.TButton', cursor='hand2')
        login_button.pack(pady=20)

        return frame

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
    # Close the database connection after the main loop ends
    app.db_connection.close()
