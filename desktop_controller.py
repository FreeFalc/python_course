# coding=utf-8
from Tkinter import *
import tkMessageBox

from configurer import contacts


root = Tk()
tl = None

l_name = Label(root, text="Name")
l_name.grid(row=0, column=0)
e_name = Entry(root)
e_name.grid(row=0, column=1)
l_phone = Label(root, text="Phone")
l_phone.grid(row=1, column=0)
e_phone = Entry(root)
e_phone.grid(row=1, column=1)


def clear_entries():
    e_name.delete(0, END)
    e_phone.delete(0, END)


def ask_create_contact():
    try:
        contacts.create_contact(e_name.get(), e_phone.get())
        clear_entries()
        tkMessageBox.showinfo("Success", "Contact added")
    except ValueError as e:
        tkMessageBox.showerror("Error", e)


def ask_find_contact():
    try:
        phone = contacts.find_contact(e_name.get())
        e_phone.delete(0, END)
        e_phone.insert(0, phone)
    except ValueError as e:
        tkMessageBox.showerror("Error", e)


def ask_update_contact():
    try:
        contacts.update_contact(e_name.get(), e_phone.get())
        clear_entries()
        tkMessageBox.showinfo("Success", "Contact updated")
    except ValueError as e:
        tkMessageBox.showerror("Error", e)


def ask_delete_contact():
    try:
        contacts.delete_contact(e_name.get())
        clear_entries()
        tkMessageBox.showinfo("Success", "Contact deleted")
    except ValueError as e:
        tkMessageBox.showerror("Error", e)


def ask_list_contacts():
    global tl
    b_l.config(text="Close List", command=on_tl_exit)
    tl = Toplevel(root)
    tl.bind('<Destroy>', on_tl_exit)
    scrollbar = Scrollbar(tl)
    scrollbar.pack(side=RIGHT, fill=Y)
    lb = Listbox(tl)
    lb.pack()
    lb.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lb.yview)
    for name, phone in contacts.list_contacts():
        lb.insert(0, "{}:{}".format(name, phone))


def on_tl_exit(_=None):
    b_l.config(text="Show All", command=ask_list_contacts)
    tl.destroy()


def on_exit():
    contacts.save_contacts()
    root.quit()

Button(root, text="Add", width=10, command=ask_create_contact).grid(row=0, column=2)
Button(root, text="Find", width=10, command=ask_find_contact).grid(row=1, column=2)
Button(root, text="Update", width=10, command=ask_update_contact).grid(row=2, column=2)
Button(root, text="Delete", width=10, command=ask_delete_contact).grid(row=3, column=2)
b_l = Button(root, text="Show All", width=10, command=ask_list_contacts)
b_l.grid(row=3, column=0)

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
