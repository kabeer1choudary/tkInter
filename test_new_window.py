from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("simple window") # application title
root.iconbitmap('icon.ico') # to add icon

def open():
    global img # adding img variable as global, cause python doesn't allow to display the image
    top = Toplevel() # a new window like root
    top.title("new window")
    top.iconbitmap('icon.ico')
    lbl = Label(top, text='hi there !').pack()
    img = ImageTk.PhotoImage(Image.open("1.png"))
    lbl1 = Label(top, image=img).pack()
    btn1 = Button(top, text='click to close', command=top.destroy).pack() # to close the new window

btn = Button(root, text='click to open a new window', command=open).pack()

root.mainloop()