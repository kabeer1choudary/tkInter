from tkinter import *

root = Tk()

root.title("simple window") # application title
root.iconbitmap('icon.ico') # to add icon
root.geometry("400x400") # setting the geometry for our window


vertical = Scale(root, from_=0, to=400) # setting a vertical slider
vertical.pack()

def click():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(vertical.get())+"x"+str(horizontal.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL) # setting a horizontal slider
horizontal.pack()


button = Button(root, text="click here", command=click).pack() #button to display the slider position

root.mainloop()