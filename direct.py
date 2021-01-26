import tkinter as tk
master = tk.Tk()
whatever_you_do = "Thank You! You have logged in successfully"
msg = tk.Message(master, text=whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

logout_btn = Button(master, text="Logout")
logout_btn.pack()
tk.mainloop()