from tkinter import *
from tkinter import messagebox
import json


def searching():
    website = website_input.get()
    try:
        with open("info.json") as data:
            read = json.load(data)

    except FileNotFoundError:
        messagebox.showinfo("Error", "not found")
    else:
        if website in read:
            email = read[website]["email"]
            password = read[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showwarning("Oops", f"No details exist for {website}")


def getting_info():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    information = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning("warning", "please don't empty any field")
    else:
        try:
            with open("info.json", "r") as data:
                reading_json = json.load(data)
        except FileNotFoundError:
            with open("info.json", "w") as data:
                json.dump(information, data, indent=4)
        else:
            reading_json.update(information)
            with open("info.json", "w") as data:
                json.dump(reading_json, data, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
# Buttons
search_button = Button(text="Search", command=searching)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=getting_info)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
