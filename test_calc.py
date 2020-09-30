from tkinter import *

root = Tk()
root.title("Calc")
input_box = Entry(root, text="", width=50, borderwidth=5)
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(num): # defining the click function to return entered numbers
    current = input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, str(current) + str(num))

def click_clr(): # defining clear button
    input_box.delete(0, END)

# defining basic functions by getting an input
def click_add():
    add = input_box.get()
    global f1
    global math
    f1 = int(add)
    math = "addition"
    input_box.delete(0, END)

def click_sub():
    sub = input_box.get()
    global f1
    global math
    f1 = int(sub)
    math = "subtraction"
    input_box.delete(0, END)

def click_mul():
    mul = input_box.get()
    global f1
    global math
    f1 = int(mul)
    math = "multiplication"
    input_box.delete(0, END)

def click_div():
    div = input_box.get()
    global f1
    global math
    f1 = int(div)
    math = "division"
    input_box.delete(0, END)

# defining equal to button, based on the operation we choose
def click_cmd():
    num = input_box.get()
    f2 = int(num)
    input_box.delete(0, END)
    if math == "addition":
        input_box.insert(0, f1 + f2)
    if math == "subtraction":
        input_box.insert(0, f1 - f2)
    if math == "multiplication":
        input_box.insert(0, f1 * f2)
    if math == "division":
        input_box.insert(0, f1 / f2)

# defining buttons and allocating them in a grid
button_1 = Button(root, text="1", height=1, width=10, command=lambda:click(1)).grid(row=1,column=0)
button_2 = Button(root, text="2", height=1, width=10, command=lambda:click(2)).grid(row=1,column=1)
button_3 = Button(root, text="3", height=1, width=10, command=lambda:click(3)).grid(row=1,column=2)
button_4 = Button(root, text="4", height=1, width=10, command=lambda:click(4)).grid(row=2,column=0)
button_5 = Button(root, text="5", height=1, width=10, command=lambda:click(5)).grid(row=2,column=1)
button_6 = Button(root, text="6", height=1, width=10, command=lambda:click(6)).grid(row=2,column=2)
button_7 = Button(root, text="7", height=1, width=10, command=lambda:click(7)).grid(row=3,column=0)
button_8 = Button(root, text="8", height=1, width=10, command=lambda:click(8)).grid(row=3,column=1)
button_9 = Button(root, text="9", height=1, width=10, command=lambda:click(9)).grid(row=3,column=2)
button_0 = Button(root, text="0", height=1, width=10, command=lambda:click(0)).grid(row=4,column=0)

button_clear = Button(root, text="CLR", height=1, width=10, command=click_clr).grid(row=4,column=1)
button_equal = Button(root, text="=", height=1, width=10, command=click_cmd).grid(row=4,column=2)
button_add = Button(root, text="+", height=1, width=10, command=click_add).grid(row=1,column=3)
button_sub = Button(root, text="-", height=1, width=10, command=click_sub).grid(row=2,column=3)
button_mul = Button(root, text="*", height=1, width=10, command=click_mul).grid(row=3,column=3)
button_div = Button(root, text="/", height=1, width=10, command=click_div).grid(row=4,column=3)

root.mainloop()