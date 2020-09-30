from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()

root.title("simple window") # application title
root.iconbitmap('icon.ico') # to add icon

def open():
    global img
    # to open location of a specified file, such as png and other files
    root.filename = filedialog.askopenfilename(initialdir="./", title="select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    img_label = Label(root, image=img).pack()

btn = Button(root, text="click to open a file", command=open).pack()
root.mainloop()