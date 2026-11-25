
import secrets
import string
import tkinter as tk
from tkinter import messagebox


# Characters used to generate passwords
character_string = (
    string.ascii_uppercase
    + string.ascii_lowercase
    + string.digits
    + "!@#$%^&*()=+_-"
)


def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())

        # Validate inputs
        if length <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Password length must be greater than zero."
            )
            return

        if repeat not in (1, 2):
            messagebox.showerror(
                "Invalid Input",
                "Enter 1 or 2 for repetition."
            )
            return

        if repeat == 1 and length > len(character_string):
            messagebox.showerror(
                "Invalid Input",
                "Length is too large for a password without repetition."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers in both fields."
        )
        return

    # Generate password
    if repeat == 1:
        password = ''.join(
            secrets.SystemRandom().sample(character_string, length)
        )
    else:
        password = ''.join(
            secrets.choice(character_string) for _ in range(length)
        )

    password_v.set("Created password: " + password)


# Define the user interface
password_gen = tk.Tk()
password_gen.geometry("450x300")
password_gen.title("Random Password Generator")
password_gen.resizable(False, False)

# Password output variable
password_v = tk.StringVar()

# Application title
title_label = tk.Label(
    password_gen,
    text="Random Password Generator",
    font=("Ubuntu Mono", 16, "bold")
)
title_label.pack(pady=10)

# Read password length
length_label = tk.Label(
    password_gen,
    text="Enter length of password:"
)
length_label.place(x=20, y=60)

length_entry = tk.Entry(password_gen, width=8)
length_entry.place(x=220, y=60)

# Read repetition preference
repeat_label = tk.Label(
    password_gen,
    text="Repetition? 1: No, 2: Yes:"
)
repeat_label.place(x=20, y=95)

repeat_entry = tk.Entry(password_gen, width=8)
repeat_entry.place(x=220, y=95)

# Generate password button
password_button = tk.Button(
    password_gen,
    text="Generate Password",
    command=generate_password
)
password_button.place(x=145, y=140)

# Display generated password
password_label = tk.Entry(
    password_gen,
    bd=2,
    bg="gray85",
    textvariable=password_v,
    state="readonly",
    readonlybackground="gray85",
    width=48
)
password_label.place(x=20, y=195, height=40)

# Exit button
exit_button = tk.Button(
    password_gen,
    text="Exit",
    command=password_gen.destroy
)
exit_button.place(x=190, y=250)

# Run application
password_gen.mainloop()
