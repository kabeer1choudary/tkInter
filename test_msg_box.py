from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("simple window") # application title
root.iconbitmap('icon.ico') # to add icon

def msg_box():
    #messagebox.showinfo('Hello world', 'hi there..!')
    #messagebox.showerror('Hello world', 'hi there..!') #here 'Hello world' = title and 'hi there..!' = message
    #messagebox.showwarning
    #messagebox.askquestion
    msg = messagebox.askretrycancel('Hello world', 'hi there..!')
    #messagebox.askyesno
    #messagebox.askyesnocancel
    Label(root, text=msg).pack() # this label is to find out the response of yes/no | retry/cancel
    if msg == 1:
        Label(root, text="its a 1").pack()
    else:
        Label(root, text="its a 0").pack()

button = Button(root, text="click here", command=msg_box).pack()

root.mainloop()