from customtkinter import *
from tkinter import ttk, messagebox
import database

def open_salary_window(refresh_main_tree):

    win = CTkToplevel()
    win.title("SQL Query Window")
    win.geometry("950x550")
    win.configure(fg_color="#161C30")
    win.grab_set()

    win.grid_rowconfigure(0, weight=1)
    win.grid_rowconfigure(1, weight=0)
    win.grid_columnconfigure(0, weight=1)

    # ====== TREE CONTAINER ======
    treeFrame = CTkFrame(win)
    treeFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    treeFrame.grid_rowconfigure(0, weight=1)
    treeFrame.grid_columnconfigure(0, weight=1)

    tree = ttk.Treeview(treeFrame, show='headings')
    tree.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(treeFrame, orient=VERTICAL, command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    tree.configure(yscrollcommand=scrollbar.set)

    style = ttk.Style()
    style.configure(
        'Treeview',
        background='#161C30',
        foreground='white',
        rowheight=30,
        font=('arial', 14)
    )
    style.configure(
        'Treeview.Heading',
        font=('arial', 16, 'bold')
    )

    # ===== LOAD DEFAULT DATA =====
    def load_all():
        tree.delete(*tree.get_children())
        tree["columns"] = ('ID', 'Name', 'Contact', 'Gender', 'Role', 'Salary')
        for col in tree["columns"]:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        for emp in database.fetch_employees():
            tree.insert('', END, values=emp)

    load_all()

    # ===== QUERY INPUT BAR =====
    bottomFrame = CTkFrame(win, fg_color="#161C30")
    bottomFrame.grid(row=1, column=0, pady=10, sticky="ew")
    bottomFrame.grid_columnconfigure(0, weight=1)

    queryEntry = CTkEntry(
        bottomFrame,
        placeholder_text="Type your query here.....",
        height=40,
        font=('arial', 14)
    )
    queryEntry.grid(row=0, column=0, padx=10, sticky="ew")

    # ===== RUN QUERY (DYNAMIC TREEVIEW) =====
    def run_query():
        query = queryEntry.get().strip()
        if not query:
            messagebox.showerror('Error', 'Please enter an SQL query.')
            return
        try:
            columns, rows = database.run_custom_query_with_columns(query)

            tree.delete(*tree.get_children())
            tree["columns"] = columns

            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=170)

            for row in rows:
                tree.insert('', END, values=row)

        except Exception as e:
            messagebox.showerror('Query Error', str(e))

    CTkButton(
        bottomFrame,
        text="Run",
        width=120,
        command=run_query
    ).grid(row=0, column=1, padx=5)

    CTkButton(
        bottomFrame,
        text="OK",
        width=120,
        command=lambda: (refresh_main_tree(), win.destroy())
    ).grid(row=0, column=2, padx=5)
