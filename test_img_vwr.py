from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("simple image viewer") # application title
root.iconbitmap('icon.ico') # to add icon

#stating the images
my_img1 = ImageTk.PhotoImage(Image.open("1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("4.png"))
#image list for reference
img_lst = [my_img1, my_img2, my_img3, my_img4]

mylabel = Label(image=my_img1)
mylabel.grid(row=0, column=0, columnspan=3)

#back function
def back(img_num):
    global mylabel
    global button_forward
    global button_back

    mylabel.grid_forget()

    mylabel=Label(image=img_lst[img_num-1])
    mylabel.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda:forward(img_num+1)).grid(row=1, column=2)
    button_back = Button(root, text="<<", command=lambda:back(img_num-1)).grid(row=1, column=0)

    if img_num == 1:
        button_back = Button(root, text="<<", state=DISABLED).grid(row=1, column=0)

    # updating status bar
    status_label = Label(root, text="Image " + str(img_num) + " of "+ str(len(img_lst)), width = 50, bd=2, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3)

# forward function
def forward(img_num):
    global mylabel
    global button_forward
    global button_back
    
    mylabel.grid_forget()

    mylabel=Label(image=img_lst[img_num-1])
    mylabel.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda:forward(img_num+1)).grid(row=1, column=2)
    button_back = Button(root, text="<<", command=lambda:back(img_num-1)).grid(row=1, column=0)

    if img_num == 4:
        button_forward = Button(root, text=">>", state=DISABLED).grid(row=1, column=2)
    # updating status bar
    status_label = Label(root, text="Image " + str(img_num) + " of "+ str(len(img_lst)), width = 50, bd=2, relief=SUNKEN, anchor=E)
    status_label.grid(row=2, column=0, columnspan=3)

#setting a status bar
status_label = Label(root, text="Image 1 of "+ str(len(img_lst)), width = 50, bd=2, relief=SUNKEN, anchor=E)
status_label.grid(row=2, column=0, columnspan=3)

#initial button assignments
button1 = Button(root, text="exit", command=root.quit).grid(row=1, column=1)
button_back = Button(root, text="<<", command=back, state=DISABLED).grid(row=1, column=0)
button_forward = Button(root, text=">>", command=lambda:forward(2)).grid(row=1, column=2)

root.mainloop()