import random
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char



# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_butt():
    #delete()
    web=web_entry.get()
    mail=em_entry.get()
    passw=pass_entry.get()

    if len(web) == 0:
        messagebox.showinfo(title="Empty", message="Some fields are empty!")
    elif len(mail)==0:
        messagebox.showinfo(title="Empty", message="Some fields are empty!")
    elif len(passw)==0:
        messagebox.showinfo(title="Empty", message="Some fields are empty!")
    else:
        but_ans=messagebox.askokcancel(title=web,message=f"These are the details entered:\n Email:{mail}\n Password:{passw}\n"
                                                 f"Do you like to save?")


        if but_ans:
            datafile=open("data.txt","a")
            datafile.write(f"{web}  |  {mail}  |  {passw}\n")

            web_entry.delete(0,END)
            em_entry.delete(0,END)
            em_entry.insert(0,"hiruthick@gmail.com")
            pass_entry.delete(0,END)
            web_entry.focus()

def pass_gen():
    if len(pass_entry.get())==0:
        pass_entry.insert(0,password)
        pyperclip.copy(password)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
#LABELS
web_label=Label(text="Website Link:")
em_label=Label(text="Email/Username:")
pass_label=Label(text="Password:")

web_label.grid(row=1,column=0)
em_label.grid(row=2,column=0)
pass_label.grid(row=3,column=0)

web_entry=Entry(width=35)
web_entry.focus()
em_entry=Entry(width=35)
em_entry.insert(0,"hiruthick@gmail.com")
pass_entry=Entry(width=21)

web_entry.grid(row=1,column=1,columnspan=2)
em_entry.grid(row=2,column=1,columnspan=2)
pass_entry.grid(row=3,column=1)
name=web_entry.get()




gen_pass_but=Button(text="Generate Password",command=pass_gen)
add_but=Button(text="Add",width=36,command=add_butt)
gen_pass_but.grid(row=3,column=2)
add_but.grid(row=4,column=1,columnspan=2)



window.mainloop()