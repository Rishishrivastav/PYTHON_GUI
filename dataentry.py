
from tkinter import *
# from tkinter import messagebox
from tkinter.ttk import Combobox
# import pathlib
import os
import openpyxl


# window=root.Tk()

root = Tk()
root.title("Date Entry")
root.geometry('700x400+300+200')
root.resizable(False, False)
root.configure(bg="#326273")

file = 'F:\PYTHON GUI PROGRAM\data.xlsx'
    


def submit():
    name = nameValue.get()
    contact = contactValue.get()
    age = ageValue.get()
    gender = gender_combobox.get()
    address = addressEntry.get(1.0, END)

    if not os.path.exists(file):
        workbook=openpyxl.workbook()
        sheet=workbook.active
        heading=['Name','Contact','Age','Gender','Address']
        sheet.append(heading)
        workbook.save(file)

    workbook= openpyxl.load_workbook(file)
    sheet= workbook.active
    sheet.append([name,contact,age,gender,address])
    workbook.save(file)

    print(name)
    print(contact)
    print(age)
    print(gender)
    print(address)

def clear():
    nameValue.set('')
    contactValue.set('')
    ageValue.set('')
    addressEntry.delete(1.0, END)

def exit():
    root.destroy()

# Heading
Label(root, text="Please fill out this entry form:", font="arial 13", bg="#326273", fg="#fff").place(x=20, y=20)

# Labels
Label(root, text="Name", font=("Arial", 12), bg="#326273", fg="#fff").place(x=50, y=100)
Label(root, text="Contact No", font=("Arial", 12), bg="#326273", fg="#fff").place(x=50, y=150)
Label(root, text="Age", font=("Arial", 12), bg="#326273", fg="#fff").place(x=50, y=200)
Label(root, text="Gender", font=("Arial", 12), bg="#326273", fg="#fff").place(x=370, y=200)
Label(root, text="Address", font=("Arial", 12), bg="#326273", fg="#fff").place(x=50, y=250)

# Entry Fields
nameValue = StringVar()
contactValue = StringVar()
ageValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=45, bd=2, font=("Arial", 12))
contactEntry = Entry(root, textvariable=contactValue, width=45, bd=2, font=("Arial", 12))
ageEntry = Entry(root, textvariable=ageValue, width=15, bd=2, font=("Arial", 12))

# Gender
gender_combobox = Combobox(root, value=['Male', 'Female'], font='Arial 14', state='readonly', width=14)
gender_combobox.place(x=440, y=200)
gender_combobox.set('Male')

addressEntry = Text(root, width=50, height=4, bd=2)

nameEntry.place(x=200, y=100)
contactEntry.place(x=200, y=150)
ageEntry.place(x=200, y=200)

Button(root, text="submit", bg="#326273",fg="white",width=15,height=2, command=submit).place(x=200,y=350)
Button(root, text="Clear", bg="#326273",fg="white",width=15,height=2 ,command=clear).place(x=340,y=350)
Button(root, text="Exit", bg="#326273",fg="white",width=15,height=2,command=exit).place(x=480,y=350)

root.mainloop()





