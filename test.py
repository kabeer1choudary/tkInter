from tkinter import *

root = Tk()

e = Entry(root, width=60, borderwidth=10) # text box
e.pack() # we can use e.grid(row=, column=)
e.insert(0, 'enter some text')

def click():
    if e.get()=="quit":
        root.quit()
    else:
        hello = "Hello "+e.get()
        myLabel = Label(root, text=hello)
        myLabel.pack()
    
myButton = Button(root, text='OK', command=click)
myButton.pack()

root.mainloop()