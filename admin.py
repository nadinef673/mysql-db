import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoices',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
def verify():
    users = admin_ent1.get()
    passs = admin_ent2.get()
    sql = "select * from admin where username = %s and password = %s"
    mycursor.execute(sql, [(users), (passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()
def logged():
    messagebox.showinfo("You have successfully logged")
    import admin_perm
    admin_perm.mainloop()

#if login details are incorrect
def failed():
    messagebox.showinfo("Error, try again")
    admin_ent1.delete(0, END)
    admin_ent2.delete(0, END)

window = Tk()
window.geometry("350x350")
window.title("Admin Login")
window.configure(background = "magenta")

admin_name = Label(window, text="User Name", bg='magenta')
admin_name.place(x=10, y=10)

admin_ent1 = Entry(window)
admin_ent1.place(x=140, y=10)

admin_pass = Label(window, text="Password", bg='magenta')
admin_pass.place(x=10, y=40)

admin_ent2 = Entry(window)
admin_ent2.place(x=140, y=40)
admin_ent2.config(show="*")

admin_btn = Button(window, text="Login", command=verify, height = 3, width = 13)
admin_btn.place(x=10, y=100)


window.mainloop()