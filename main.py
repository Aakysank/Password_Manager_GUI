import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(width= 200, height=200,padx = 20, pady = 20)

#canvas widget creation - embedding the image for GUI

password_canvas = tkinter.Canvas(width=200,height=200)
photo = tkinter.PhotoImage(file="logo.png")
password_canvas.create_image(100, 100,image=photo)
password_canvas.grid(column = 1, row = 0)

#GUI grid layout

website_label = tkinter.Label(text="Website:")
website_label.grid(column = 0, row= 1)

website_line_edit = tkinter.Entry(width=35)
website_line_edit.grid(column = 1, row= 1)

def search_website():
    try:
        website_name = website_line_edit.get()
        if len(website_name):
            with open("data.json",mode='r') as file:
                data = json.load(file)
            search_data = data[website_name]
        else:
            messagebox.showerror(title="Error", message=f"Please enter a website name")
            return
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"Data file not present. Please store your data")
    except KeyError:
        messagebox.showerror(title="Error", message=f"Website not found")
    else:
        
        email = search_data["email"]
        password = search_data["password"]

        messagebox.showinfo(title="Info", message = f"E-mail/Username: {email} \n Password: {password}")

website_search = tkinter.Button(text="Search", command=search_website)
website_search.grid(column=2, row=1)

email_un_label = tkinter.Label(text="E-mail/Username:")
email_un_label.grid(column = 0, row= 2)

email_un_line_edit = tkinter.Entry(width=35)
email_un_line_edit.grid(column = 1, row= 2, columnspan=2)

pwd_label = tkinter.Label(text="Password:")
pwd_label.grid(column = 0, row= 3)

pwd_line_edit = tkinter.Entry(width=21)
pwd_line_edit.grid(column = 1, row= 3)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #print("Welcome to the PyPassword Generator!")
    nr_letters= random.randint(2,4) 
    nr_symbols = random.randint(1,3) 
    nr_numbers = random.randint(1,3) 

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    password_list = []
    #for n in range(0,nr_letters):
    #  password_list += random.choice(letters)
    #
    #for n in range(0,nr_symbols):
    #  password_list += random.choice(symbols)
    #
    #for n in range(0,nr_numbers):
    #  password_list += random.choice(numbers)

    #print(password)
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    password_list = [random.choice(letters) for n in range(0,nr_letters)]
    password_list.extend([random.choice(symbols) for n in range(0,nr_symbols)])
    password_list.extend([random.choice(numbers) for n in range(0,nr_numbers)])

    random.shuffle(password_list)
    pwd_string = "".join(password_list)

    pwd_line_edit.delete(0,tkinter.END)
    pwd_line_edit.insert(tkinter.END,pwd_string)

    pyperclip.copy(pwd_string)
    
def save_to_file():
    website = website_line_edit.get()
    email = email_un_line_edit.get()
    pwd = pwd_line_edit.get()

    if len(website) <=0 or len(email) <=0 or len(pwd) <=0:
        if len(website) <=0:
            messagebox.showerror(title="Invalid data", message=f"Please enter valid website")
        elif len(email) <=0:
            messagebox.showerror(title="Invalid data", message=f"Please enter valid email")
        elif len(pwd) <=0:
            messagebox.showerror(title="Invalid data", message=f"Please enter valid password")
    else:
        new_dict = {
            website:
            {
                "email":email,
                "password":pwd
            }
            }

        try:
            with open("data.json",mode='r') as file:
                data = json.load(file)    
        except FileNotFoundError:
            data = new_dict
        else:
            data.update(new_dict)

        with open("data.json",mode='w') as file:
            json.dump(data,file,indent=4)
        
        website_line_edit.delete(0,tkinter.END)
        email_un_line_edit.delete(0,tkinter.END)
        pwd_line_edit.delete(0,tkinter.END)
        
        

# ---------------------------- UI SETUP ------------------------------- #

pwd_generate_pwd = tkinter.Button(text="Generate Password", command=generate_password)
pwd_generate_pwd.grid(column = 2, row= 3)

add_button = tkinter.Button(text="Add",width=36, command=save_to_file)
add_button.grid(column = 1, row= 4, columnspan=2)

window.mainloop()
