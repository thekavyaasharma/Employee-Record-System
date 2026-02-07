from customtkinter import *
from tkinter import ttk, messagebox
import database
import run_sql

set_appearance_mode("light")      

# functions 



def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error', 'Enter value to the Search bar.')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please select an option.')
    else:
        searched_data = database.search(searchBox.get(), searchEntry.get())
        tree.delete(*tree.get_children()) #delete previous data 
        employees = database.fetch_employees()
        for employee in searched_data:
            tree.insert('', END,values=employee)
        

# before delete ask for confirmation
def delete_all():
    result = messagebox.askyesno('Confirm','Do you want to delete all the records permanently?')
    if result:
        database.deleteall_records() 
        tree.delete(*tree.get_children()) #delete previous data 
    else :
        pass 


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete.')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error','Data is deleted.')

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update.')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),genderBox.get(),roleBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('SUCCESS','Data is updated.')

def selection(event):
    selected_item = tree.selection() # return a tuple
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        genderBox.set(row[3])
        roleBox.set(row[4])
        salaryEntry.insert(0,row[5])

def clear(value = False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    genderBox.set('Female')
    roleBox.set('Web Developer')
    salaryEntry.delete(0,END)

def treeview_data():
    tree.delete(*tree.get_children()) 
    employees = database.fetch_employees()
    for employee in employees:
        tree.insert('', END,values=employee)



def add_employee():

    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required.')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','ID already exists.')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error',"Invalid ID format. Use 'EMP-' followed by a number(e.g., 'EMP-101')")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),genderBox.get(),roleBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employee added successfully.')


# ===================== MAIN WINDOW =====================
window = CTk()
window.title('Employee Management System')
window.minsize(930, 580)
window.configure(fg_color="#161C30")
# window.state('zoomed')   # uncomment if you want it maximized on start

# Grid configuration for responsiveness
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=0)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)

# ===================== LEFT FRAME =====================
leftFrame = CTkFrame(window, fg_color="#161C30")
leftFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
leftFrame.grid_columnconfigure(1, weight=1)

# ID
CTkLabel(leftFrame, text='ID', font=('arial', 18, 'bold'), text_color='white')\
    .grid(row=0, column=0, padx=20, pady=25, sticky='w')
idEntry = CTkEntry(leftFrame, font=('arial', 15))
idEntry.grid(row=0, column=1, sticky="ew")

# Name
CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'), text_color='white')\
    .grid(row=1, column=0, padx=20, pady=25, sticky='w')
nameEntry = CTkEntry(leftFrame, font=('arial', 15))
nameEntry.grid(row=1, column=1, sticky="ew")

# Contact
CTkLabel(leftFrame, text='Contact', font=('arial', 18, 'bold'), text_color='white')\
    .grid(row=2, column=0, padx=20, pady=25, sticky='w')
phoneEntry = CTkEntry(leftFrame, font=('arial', 15))
phoneEntry.grid(row=2, column=1, sticky="ew")

# Gender
CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'), text_color='white')\
    .grid(row=3, column=0, padx=20, pady=25, sticky='w')
genderBox = CTkComboBox(
    leftFrame,
    values=['Female', 'Male'],
    state='readonly'
)
genderBox.set('Female')
genderBox.grid(row=3, column=1, sticky="ew")

# Role
CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'), text_color='white')\
    .grid(row=4, column=0, padx=20, pady=25, sticky='w')
roleBox = CTkComboBox(
    leftFrame,
    values=[
        'Web Developer', 'UX/UI Designer', 'Cloud Architect',
        'HR Manager', 'Network Engineer', 'IT Consultant',
        'Business Analyst', 'Data Scientist',
        'Technical Writer', 'DevOps Engineer'
    ],
    state='readonly'
)
roleBox.set('Web Developer')
roleBox.grid(row=4, column=1, sticky="ew")

# Salary
CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'), text_color='white')\
    .grid(row=5, column=0, padx=20, pady=25, sticky='w')
salaryEntry = CTkEntry(leftFrame, font=('arial', 15))
salaryEntry.grid(row=5, column=1, sticky="ew")

CTkButton(
    leftFrame,
    text="SQL Operations",
    width=180,
    command=lambda: run_sql.open_salary_window(treeview_data)
).grid(row=6, column=1, pady=15, sticky="w")


# ===================== RIGHT FRAME =====================
rightFrame = CTkFrame(window)
rightFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
rightFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_rowconfigure(1, weight=1)

# Search bar
searchBox = CTkComboBox(
    rightFrame,
    values=['ID', 'Name', 'Contact', 'Gender', 'Role', 'Salary'],
    state='readonly'
)
searchBox.set('Search by')
searchBox.grid(row=0, column=0)

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1, padx=5)

CTkButton(rightFrame, text='Search', width=100,command = search_employee)\
    .grid(row=0, column=2, padx=5)

CTkButton(rightFrame, text='Show all', width=100, command = show_all)\
    .grid(row=0, column=3, padx=5)

# ===================== TREEVIEW =====================
tree = ttk.Treeview(
    rightFrame,
    columns=('ID', 'Name', 'Contact', 'Gender', 'Role', 'Salary'),
    show='headings'
)
tree.grid(row=1, column=0, columnspan=4, sticky="nsew")

for col, w in zip(
    ('ID', 'Name', 'Contact', 'Gender', 'Role', 'Salary'),
    (100, 160, 160, 100, 200, 140)
):
    tree.heading(col, text=col)
    tree.column(col, width=w)

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 18, 'bold'), rowheight=40)
style.configure('Treeview',font=('arial', 15),rowheight = 30, background ='#161C30', foreground = 'white')

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns')
tree.configure(yscrollcommand=scrollbar.set)

# ===================== BUTTON FRAME =====================
buttonFrame = CTkFrame(window, fg_color="#161C30")
buttonFrame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
buttonFrame.grid_columnconfigure((0,1,2,3,4), weight=1)

CTkButton(buttonFrame, text='New Employee', width=160,command=lambda: clear(True))\
    .grid(row=0, column=0, padx=5)

CTkButton(buttonFrame, text='Add Employee', width=160, command=add_employee)\
    .grid(row=0, column=1, padx=5)

CTkButton(buttonFrame, text='Update Employee', width=160, command = update_employee)\
    .grid(row=0, column=2, padx=5)

CTkButton(buttonFrame, text='Delete Employee', width=160, command = delete_employee)\
    .grid(row=0, column=3, padx=5)

CTkButton(buttonFrame, text='Delete All', width=160, command = delete_all)\
    .grid(row=0, column=4, padx=5)

# ===================== START APP =====================
treeview_data()
window.bind('<ButtonRelease>', selection)
window.mainloop()