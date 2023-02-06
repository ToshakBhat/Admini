from tkinter import *
from tkinter import messagebox as msg
import csv
from section import gettingPassword
import Format
bg = "#ffff80"


def conformation(wind, lst1, class_name):
    def passwords():
        x = password.get()
        if x.upper() == gettingPassword():
            Format.Alter(lst1, root12, class_name)
        else:
            msg.showerror("ERROR", "Wrong Password")

    wind.destroy()
    root12 = Tk()
    root12.geometry("400x300")
    password = StringVar()
    Frame(root12, width=400, height=300, bg=bg).grid(row=0, column=0, columnspan=1, rowspan=4)
    Label(root12, text="PASSWORD CONFORMATION", font=("verdana", 12, "bold"), fg="green").grid(row=0, column=0,
                                                                                            sticky="nsew")
    Entry(root12, textvariable=password).grid(row=1, column=0, rowspan=2)
    Button(root12, text="OK", bg="black", fg="white", command=passwords).grid(row=2, column=0, pady=5)
    root12.mainloop()