import mysql.connector

# Establish a database connection
def create_db_connection():
    return mysql.connector.connect(
        host="141.209.241.91",
        user="sp2024bis698g1",  # MySQL username
        passwd="warm",  # MySQL password
        database="sp2024bis698g1s"  # database name
    )   

# Function to execute a query (CREATE, UPDATE, DELETE)
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        cursor.close()
        return False

# Function to fetch data from the database (SELECT)
def read_query(connection, query, data=None):
    cursor = connection.cursor(dictionary=True)
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        cursor.close()
        return []

# Function to create a request
def create_request(room_id, global_id, first_name, last_name, email, phone, description):
    db = create_db_connection()
    query = """
        INSERT INTO REQUESTOR (ROOM_ID, REQ_GLOBALID, REQ_FNAME, REQ_LNAME, REQ_EMAIL, REQ_PHONE, REQ_DESCR, REQ_DATE) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())
    """
    data = (room_id, global_id, first_name, last_name, email, phone, description)
    success = execute_query(db, query, data)
    db.close()
    return success

# Function to list all requests
def list_all_requests():
    db = create_db_connection()
    query = "SELECT * FROM REQUESTOR"
    requests = read_query(db, query)
    db.close()
    return requests

# Function to create a task
def create_task(req_id, assigned_by_emp_id, assigned_to_emp_id, cat_id, description, severity):
    db = create_db_connection()
    query = """
        INSERT INTO TASK (REQ_ID, ASSGND_BY_EMP_ID, ASSGND_TO_EMP_ID, CAT_ID, TASK_DESC, TASK_SEVERITY, TASK_STATUS, TASK_STARTDT) 
        VALUES (%s, %s, %s, %s, %s, %s, 'Open', CURDATE())
    """
    data = (req_id, assigned_by_emp_id, assigned_to_emp_id, cat_id, description, severity)
    success = execute_query(db, query, data)
    db.close()
    return success

# Function to list all tasks
def list_all_tasks():
    db = create_db_connection()
    query = "SELECT * FROM TASK"
    tasks = read_query(db, query)
    db.close()
    return tasks

# Function to update a task
def update_task(task_id, update_info):
    
    db = create_db_connection()
    query = """
        UPDATE TASK SET TASK_STATUS = %s, TASK_ENDDT = CURDATE() 
        WHERE TASK_ID = %s
    """
    data = (update_info, task_id)
    success = execute_query(db, query, data)
    db.close()
    return success
