import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoices',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

def register():
    sql="INSERT into register values (%s,%s,%s,%s)"
    val=('0',str(reg_ent1.get()),str(reg_ent2.get()),str(password_ent.get()))
    mycursor.execute(sql,val)
    mydb.commit()

    import register_page
    register_page.mainloop()

window = Tk()
window.geometry("500x500")
window.title("Register")
window.configure(background = "magenta")

reg_name = Label(window, text="Please enter your name", bg='magenta')
reg_name.grid(row=1, column=1)

reg_ent1 = Entry(window)
reg_ent1.grid(row=1, column=3)

reg_username = Label(window, text="Please Select username", bg='magenta')
reg_username.grid(row=2, column=1)

reg_ent2 = Entry(window)
reg_ent2.grid(row=2, column=3)

password=Label(window, text="Please select password", bg='magenta')
password.grid(row=3, column=1)

password_ent = Entry(window)
password_ent.grid(row=3, column=3)
password_ent.config(show="*")

reg_btn = Button(window, text="Register", command=register, height = 1, width = 8)
reg_btn.grid(row=5, column=2)


window.mainloop()