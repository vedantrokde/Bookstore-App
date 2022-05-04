# importing libraries
from tkinter import *

# defining main object for window
root = Tk()

# util functions
def convert():
    t1.delete("1.0", END)
    t1.insert(END, float(e2_value.get()) * 1000)
    t2.delete("1.0", END)
    t2.insert(END, float(e2_value.get()) * 2.20462)
    t3.delete("1.0", END)
    t3.insert(END, float(e2_value.get()) * 35.274)

    t1.insert(END, float(e2_value.get()) * 1.6)


# adding row 1 with label, input field and button
e1 = Label(root, text="Enter quatity (in kg):")
e1.grid(row=0, column=0)

e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value)
e2.grid(row=0, column=1)

b1 = Button(root, text="Convert", command=convert)
b1.grid(row=0, column=2)

# adding row 2 with 3 output fields
t1 = Text(root, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(root, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(root, height=1, width=20)
t3.grid(row=1, column=2)

# rendering the root
root.mainloop()