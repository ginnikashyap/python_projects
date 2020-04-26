from tkinter import *
from backend import Database

database=Database("books.db")

window = Tk()

window.wm_title("BookStore")

# Wrapper functions for each database function
def get_selected_row(event):
    global selected_row
    index=list1.curselection()[0]
    selected_row=list1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selected_row[1])

    entry2.delete(0, END)
    entry2.insert(END, selected_row[2])

    entry3.delete(0, END)
    entry3.insert(END, selected_row[3])

    entry4.delete(0, END)
    entry4.insert(END, selected_row[4])


def view_command():
    list1.delete(0,END)
    for row in database.view_data():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def insert_command():
    database.insert_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0, END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

# def update_command():
#     list_id=list1.s
#     backend.update_data(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),list_id)
#
def delete_command():
    id=selected_row[0]
    database.delete_data(id)

def update_command():
    id=selected_row[0]
    database.update_data(id,entry1.get(),entry2.get(),entry3.get(),entry4.get())





label1 = Label(window,text="Title")
label1.grid(row=0,column=0)

title_text=StringVar()
entry1 = Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)


label2 = Label(window,text="Author")
label2.grid(row=0,column=2)

author_text=StringVar()
entry2 = Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)

label3 = Label(window,text="Year")
label3.grid(row=1,column=0)

year_text=StringVar()
entry3 = Entry(window,textvariable=year_text)
entry3.grid(row=1,column=1)


label4 = Label(window,text="ISBN")
label4.grid(row=1,column=2)

isbn_text=StringVar()
entry4 = Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

list1 = Listbox(window,height=6,width=45)
list1.grid(row=3,column=0,rowspan=6,columnspan=2)


sb1=Scrollbar(window)
sb1.grid(row=4,column=2,rowspan=6)

# link the scrollbar to list
# And link list to scrollbar
# Configure method is used to access an object's attributes after its initialisation.
#here changing list1's by adding scrollbar to it
list1.configure(yscrollcommand=sb1.set)
list1.bind('<<ListboxSelect>>',get_selected_row)

#here changing Scrollbar's by adding scrollbar to it
sb1.configure(command=list1.yview())

button1= Button(window, width=12,text="View All",command=view_command)
button1.grid(row=2,column=3)

button1= Button(window,text="Search an Entry",width=12,command=search_command)
button1.grid(row=3,column=3)

button1= Button(window,text="Add a entry",width=12,command=insert_command)
button1.grid(row=4,column=3)

button1= Button(window,text="Update",width=12,command=update_command)
button1.grid(row=5,column=3)

button1= Button(window,text="Delete",width=12,command=delete_command)
button1.grid(row=6,column=3)

button1= Button(window,text="Close",width=12,command=window.destroy)
button1.grid(row=7,column=3)


window.mainloop()