import pymysql
from tkinter import messagebox

def connect_db():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root',password='enter your password ')
        mycursor = conn.cursor()
        
    except:
        messagebox.showerror('Error','Something went wrong.')
        # open command line client -> enter password ->rerun the code 
        return
    
    
    # create db 
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_db')
    mycursor.execute('USE employee_db')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data(ID VARCHAR(30) PRIMARY KEY, Name VARCHAR(50), Contact VARCHAR(20),Gender VARCHAR(20), Role VARCHAR(50),Salary VARCHAR(70))')
    conn.commit()

# fnx to add employee in db 
def insert(id,name,contact,gender,role,salary):
    mycursor.execute('INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s)',(id,name,contact,gender,role,salary))
    # commit changes
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE ID = %s',(id,))
    result = mycursor.fetchone()
    return result[0] > 0

def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result 

def update(id,new_name,new_phone,new_gender,new_role,new_salary):
    mycursor.execute('UPDATE data SET Name =%s,Contact=%s,Gender =%s,Role =%s,Salary = %s WHERE ID = %s',(new_name,new_phone,new_gender,new_role,new_salary,id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM data WHERE ID = %s', id)
    conn.commit()

def search(option, value):
    mycursor.execute(f'SELECT * FROM data Where {option} = %s',value)
    result = mycursor.fetchall()
    return result 

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data') # truncate command is used 
    conn.commit() # whenever modifications are done in db we have to commit the data 


connect_db()