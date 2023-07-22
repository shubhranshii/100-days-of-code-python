from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list=[]
    password_letters= [random.choice(letters) for n in range(0,nr_letters)]
    password_symbols=[random.choice(symbols)  for n in range(0,nr_symbols)]
    password_numbers=[random.choice(numbers)  for n in range(0,nr_numbers)]
    password_list= password_numbers+password_letters+password_symbols


    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Incomplete Information", message="Please do not leave any fields empty.")

    else:
        if messagebox.askokcancel(title=website, message=f"Details entered are:\nEmail/Username:"
                                                         f"{username}\nPassword:{password}\nClick OK to continue."):
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

website_var = StringVar()
website_label = Label(text="Website:", font=('calibre', 10, 'normal'))
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

user_label = Label(text="Email/Username:", font=('calibre', 10, 'normal'))
user_label.grid(row=2, column=0)
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0, "shubhranshiagarwal@gmail.com")

password_label = Label(text="Password:", font=('calibre', 10, 'normal'))
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=2, sticky="EW")

generate_button = Button(text="Generate Password", padx=1, relief="groove", command=create_password)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", padx=1, relief="groove", command=add_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
