from customtkinter import *
from PIL import Image
from tkinter import messagebox

set_appearance_mode("light")

# ---------------- LOGIN FUNCTION ----------------
def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror("ERROR", "All fields are required.")
    elif usernameEntry.get() == "Kavya Sharma" and passwordEntry.get() == "1234":
        messagebox.showinfo("Success", "Login is successful.")
        root.destroy()
        import ems
    else:
        messagebox.showerror("ERROR", "Wrong credentials.")


# ---------------- MAIN WINDOW ----------------
root = CTk()
root.title("Login Page")
root.geometry("930x478")
root.state("zoomed")   # start maximized (Windows)

# ---------------- BACKGROUND IMAGE ----------------
original_image = Image.open("cover.jpg")

bg_image = CTkImage(original_image, size=(930, 478))

imglabel = CTkLabel(root, image=bg_image, text="")
imglabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Resize background dynamically
def resize_bg(event):
    resized_image = CTkImage(
        original_image,
        size=(event.width, event.height)
    )
    imglabel.configure(image=resized_image)
    imglabel.image = resized_image

root.bind("<Configure>", resize_bg)


# ---------------- USERNAME ----------------
usernameEntry = CTkEntry(
    root,
    placeholder_text="Username",
    width=280,
    height=42,
    fg_color="white",
    text_color="black",
    placeholder_text_color="gray",
    border_color="#c0c0c0",
    border_width=1,
    corner_radius=8
)
usernameEntry.place(relx=0.5, rely=0.45, anchor="center")

# ---------------- PASSWORD ----------------
passwordEntry = CTkEntry(
    root,
    placeholder_text="Password",
    width=280,
    height=42,
    show="*",
    fg_color="white",
    text_color="black",
    placeholder_text_color="gray",
    border_color="#c0c0c0",
    border_width=1,
    corner_radius=8
)
passwordEntry.place(relx=0.5, rely=0.55, anchor="center")

# ---------------- LOGIN BUTTON ----------------
loginButton = CTkButton(
    root,
    text="Login",
    width=220,
    height=42,
    cursor="hand2",
    command=login,
    fg_color="#1f6aa5",
    hover_color="#165a8a",
    corner_radius=8
)
loginButton.place(relx=0.5, rely=0.68, anchor="center")

root.mainloop()
