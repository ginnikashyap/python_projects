from tkinter import *

# All the code for wideget  goes here inside this block of window and window.mainloop,Else we may not  be able to see anything
# Button action is to convert given km to miles.
window = Tk()
def km_to_miles():
    e2_value=e1_value.get()
    print(type(e2_value))
    miles=float(e2_value)/1.609
    t1.insert(END,miles)

#Adding button widget
b1 = Button(window,text="Execute",command=km_to_miles)
#Sepecifying the position of the button like where to apply
b1.grid(row=0,column=0)

# Creating a variable of type StringVar,Since it will be linked to entry widget.And it is dynamic.
e1_value = StringVar()
# Adiing entry widget
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

# Adiing text widget,
t1= Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()



