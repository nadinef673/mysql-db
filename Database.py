from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Life Choices Database")
window.configure(background = "magenta")

def stud():
    import students
    students.mainloop()

def admin():
    import admin
    admin.mainloop()

def staff():
    import staff
    staff.mainloop()

def register():
    import register
    register.mainloop()

wel_lbl = Label(window, text="Welcome to Lifechoices Login Page", bg="magenta")
wel_lbl.pack(side=TOP)

sel_lbl = Label(window, text="Please Select One Of The Options Below", bg="magenta")
sel_lbl.pack(side=TOP)


stud_btn = Button(window, text="Students", command=stud, bg='grey', fg='black')
stud_btn.pack(side=LEFT)


admin_btn = Button(window, text="Admin", command=admin, bg='grey', fg='black')
admin_btn.pack(side=LEFT)

staff_btn = Button(window, text="Staff", command=staff, bg='grey', fg='black')
staff_btn.pack(side=RIGHT)

reg_btn = Button(window, text="Register", command=register, bg='grey', fg='black')
reg_btn.pack(side=RIGHT)

window.mainloop()