import pymysql
from tkinter import messagebox

def connect_db():
    global mycursor, conn
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='xxx' #insert your own mysql password 
        )
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Something went wrong.')
        return

    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_db')
    mycursor.execute('USE employee_db')
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS data(
            ID VARCHAR(30) PRIMARY KEY,
            Name VARCHAR(50),
            Contact VARCHAR(20),
            Gender VARCHAR(20),
            Role VARCHAR(50),
            Salary INT
        )
    ''')
    conn.commit()

def insert(id, name, contact, gender, role, salary):
    mycursor.execute(
        'INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s)',
        (id, name, contact, gender, role, salary)
    )
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE ID=%s', (id,))
    return mycursor.fetchone()[0] > 0

def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    return mycursor.fetchall()

def update(id, name, contact, gender, role, salary):
    mycursor.execute(
        '''UPDATE data 
           SET Name=%s, Contact=%s, Gender=%s, Role=%s, Salary=%s 
           WHERE ID=%s''',
        (name, contact, gender, role, salary, id)
    )
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM data WHERE ID=%s', (id,))
    conn.commit()

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()

#  NEW: run custom SQL query
def run_custom_query(query):
    mycursor.execute(query)
    return mycursor.fetchall()

def run_custom_query_with_columns(query):
    mycursor.execute(query)
    rows = mycursor.fetchall()
    columns = [desc[0] for desc in mycursor.description]
    return columns, rows


connect_db()