from tkinter import *
root = Tk()

root.title("simple window") # application title
root.iconbitmap('icon.ico') # to add icon

#defining frame
new_frame = LabelFrame(root, text="frame 1", padx=20, pady=20) #here padx and pady refers frame inside
new_frame.pack(padx=50, pady=50) #here padx and pady refers frame outside

#assigning buttons, we can use grid inside of the frame. when packing the frame by outside
button1 = Button(new_frame, text="click here").grid(row=0, column=0)
button2 = Button(new_frame, text="or...click here").grid(row=0, column=1)

#defining frame2
new_frame2 = LabelFrame(root, text="frame 2", padx=20, pady=20) #here padx and pady refers frame inside
new_frame2.pack(padx=50, pady=50) #here padx and pady refers frame outside

#defining the click value
def click(value):
    int_label = Label(new_frame2, text=value).pack()

#setting up radio buttons with integer values
r = IntVar()
r.set(2)

Radiobutton(new_frame2, text="op1", variable=r, value=1, command=lambda:click(r.get())).pack()
Radiobutton(new_frame2, text="op2", variable=r, value=2, command=lambda:click(r.get())).pack()

int_label = Label(new_frame2, text=r.get()).pack()

#defining frame3
new_frame3 = LabelFrame(root, text="frame 3", padx=20, pady=20) #here padx and pady refers frame inside
new_frame3.pack(padx=50, pady=50) #here padx and pady refers frame outside

#a list to iterate
lst = [
    ("milk", "milk"),
    ("bread", "bread"),
    ("eggs", "eggs"),
    ("juice", "juice")
]

def clicked(value):
    lst_label = Label(new_frame3, text=value).pack()
#setting up radio buttons with string values
s = StringVar()
s.set("milk")
for item, ingredient in lst:
    Radiobutton(new_frame3, text=item, variable=s, value=ingredient).pack()

lst_label = Label(new_frame3, text=s.get()).pack()
button = Button(new_frame3, text="ok", command=lambda:clicked(s.get())).pack()
root.mainloop()