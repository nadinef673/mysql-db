from tkinter import *
import  mysql.connector
from tkinter import messagebox

add = Tk()
add.title("Add user by admin")
add.geometry("300x300")

# widgets
head_lbl = Label(add)
head_lbl.grid(row=1, column=1)
fname_lbl = Label(add, text="Full Name:")
fname_lbl.grid(row=2, column=1)
uname_lbl = Label(add, text="Username:")
uname_lbl.grid(row=3, column=1)
passw_lbl = Label(add, text="Password:")
passw_lbl.grid(row=4, column=1)
fname = Entry(add)
fname.grid(row=2, column=2)
uname = Entry(add)
uname.grid(row=3, column=2)
passw = Entry(add)
passw.grid(row=4, column=2)

def create():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
    host='localhost', database='Lifechoices')

    mycursor = mydb.cursor()

    x = fname.get()
    y = uname.get()
    z = passw.get()
    if x=='' or y=='' or z=='':
        messagebox.showerror("TRY AGAIN", "Please do not leave the fields empty")
        add.destroy()
        create()
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                       host='localhost', database='Lifechoices')
        try:
            mycursor = mydb.cursor()
            sql = "INSERT INTO register (full_name, username, password) VALUES(%s, %s, %s)"
            mycursor.execute(sql, [(x), (y), (z)])
            mydb.commit()
        except:
            messagebox.showerror("OOPS", "Error connecting to databases")
        messagebox.showinfo("SUCCESS " + x + " has been added to the server")
        add.destroy()

create_btn = Button(add, text="Add User", width=20, command=create)
create_btn.place(x=0, y=150)

add = Tk()
add.title("Delete user by admin")
add.geometry("300x300")

# widgets
head_lbl = Label(add)
head_lbl.grid(row=1, column=1)
del_fname_lbl = Label(add, text="Full Name:")
del_fname_lbl.grid(row=2, column=1)
del_uname_lbl = Label(add, text="Username:")
del_uname_lbl.grid(row=3, column=1)
del_passw_lbl = Label(add, text="Password:")
del_passw_lbl.grid(row=4, column=1)
del_fname = Entry(add)
del_fname.grid(row=2, column=2)
del_uname = Entry(add)
del_uname.grid(row=3, column=2)
del_passw = Entry(add)
del_passw.grid(row=4, column=2)

def delete():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
    host='localhost', database='Lifechoices')

    mycursor = mydb.cursor()

    x = del_fname.get()
    y = del_uname.get()
    z = del_passw.get()
    if x=='' or y=='' or z=='':
        messagebox.showerror("TRY AGAIN", "Please do not leave the fields empty")
        add.destroy()
        create()
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                                       host='localhost', database='Lifechoices')
        try:
            mycursor = mydb.cursor()
            sql = "DELETE from register (full_name, username, password) VALUES(%s, %s, %s)"
            mycursor.execute(sql, [(x), (y), (z)])
            mydb.commit()
        except:
            messagebox.showerror("OOPS", "Error connecting to databases")
        messagebox.showinfo("SUCCESS " + x + " has been added to the server")
        add.destroy()

delete_btn = Button(add, text="Delete User", width=20, command=delete)
delete_btn.place(x=0, y=150)

add.mainloop()