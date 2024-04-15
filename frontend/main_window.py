import tkinter as tk
from tkinter import ttk, messagebox
from backend.db import read_query, create_db_connection

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
        
        # Submit Button with style
        submit_button = ttk.Button(self, text="Create Request", command=self.create_request, style='Primary.TButton')
        submit_button.grid(row=len(fields) + start_row_index + 1, column=0, columnspan=2, pady=20)
        
    def create_request(self):
        # Here you would collect all the data from the entries and create the request
        # For now, let's just print the entries and show a confirmation dialog
        data = {field: entry.get() for field, entry in self.entries.items()}
        data['Description'] = self.desc_text.get("1.0", "end-1c")  # Get text from Text widget
        print(data)
        messagebox.showinfo("Request Created", "The request has been created successfully!")

    def fetch_room_ids(self):
        query = "SELECT ROOM_ID FROM room"
        result = read_query(self.db_connection, query)
        room_ids = [str(room['ROOM_ID']) for room in result]
        self.room_id_dropdown['values'] = room_ids
        print(f"Fetched {len(room_ids)} room IDs")
        if room_ids:
            self.room_id_var.set(room_ids[0])
            
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
