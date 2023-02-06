from tkinter import *
import csv
from tkinter import messagebox as msg
import string
import WorkingOnClasses as WOC
from tkinter import colorchooser as color
import ViewStatus
import promote


def Credit():
    root = Tk()
    root.geometry("400x300")
    Frame(root, width=400, height=300).grid(row=0, column=0, columnspan=2,rowspan=5, sticky="nsew")

    Label(root, text="CREDITS", fg="tomato").grid(row=0, column=0, columnspan=2, sticky="nsew")
    Label(root, text="IDEA :").grid(row=1, column=0, sticky="nsew")
    Label(root, text="CODER :").grid(row=2, column=0, sticky="nsew")
    Label(root, text="DISTRIBUTOR :").grid(row=3, column=0, sticky="nsew")
    Label(root, text="MANAGER :").grid(row=4, column=0, sticky="nsew")
    Label(root, text="GOD", font=("verdana", 14, ("bold", "underline"))).grid(row=1, column=1, sticky="w")
    Label(root, text="GOD", font=("verdana", 14, ("bold", "underline"))).grid(row=3, column=1, sticky="w")
    Label(root, text="GOD", font=("verdana", 14, ("bold", "underline"))).grid(row=4, column=1, sticky="w")
    Label(root, text="Toshak Bhat").grid(row=2, column=1, sticky="w")
    root.mainloop()


def contact():
    msg.showinfo("Contact", "You can contact us to share your experience through the gmail address:"
                            "asatdreamz@gmail.com ")


def CreateNewWindow2(window2):

    def workingOnClass(event):
        text = event.widget.cget("text")
        WOC.gettingWindowAndClass(root3, text, colour)

    def Continuity():
        row = 3
        column= 0
        sticky = "nw"
        padding_x = 10
        for i in range(3, len(From_file)):
            b1 = Button(root3, text=From_file[i], width=12, bg="tomato", activebackground="sky blue", font=("verdana",10,"bold"), pady=5)
            b1.bind("<Button-1>", workingOnClass)
            b1.grid(row=row, column=column, sticky=sticky, padx=padding_x, pady=5)
            row += 1
            if row == 11:
                row = 3
                column = 2
                sticky = "ne"

    """def PasswordCheck():
        if (password.get()).upper() == From_file[2]:
            password.set("")
            Continuity()
        else:
            res = msg.showerror("ERROR", "Incorrect Password")
            if res == "ok":
                root3.destroy()
    """
    window2.destroy()
    root3 = Tk()
    root3.geometry("1000x500")
    root3.minsize(950, 400)
    root3.maxsize(1050, 500)
    file = open("files/Intro content/color.txt")
    colour = file.readline()
    file.close()
    root3.configure(bg=colour)
    #menubar

    def status():
        ViewStatus.Status(From_file)

    def color_picker():
        res = msg.askyesno("Color", "Want to change Background colour ?")
        if res is True:
            x = color.askcolor()
            color_file = open("files/Intro content/color.txt", mode="w")
            color_file.write(x[1])
            color_file.close()
    MenuBar = Menu(root3)
    FileMenuBar = Menu(MenuBar)
    FileMenuBar.add_command(label="Bg Color", command=color_picker)
    FileMenuBar.add_command(label="Contact", command=contact)
    FileMenuBar.add_command(label="Credits", command=Credit)
    #FileMenuBar.add_command(label="Exit", command=exit)
    MenuBar.add_cascade(label="File", menu=FileMenuBar)
    MenuBar.add_command(label="View Status", command=status)
    #MenuBar.add_command(label="Promote", command=lambda: promote.message())
    root3.config(menu=MenuBar)

    with open('files/Intro content/IntroNew.csv', 'r') as my_file:
        From_file = list()
        my_reader = csv.reader(my_file)
        for data in my_reader:
            if data == []:
                msg.showerror("ERROR", "Your Profile Doesn't Exist. Please create a one")
                root3.destroy()
            else:
                From_file.extend(data)
    root3.title(From_file[0])
    f = Frame(root3, width=1000, height=100, bg="green").grid(row=0, column=0, rowspan=3, columnspan=3)
    Label(f, text=From_file[0], font=("verdana", 14, ("bold", "underline")),bg="green", fg="yellow").grid(row=0, column=0, columnspan=3, sticky="nsew")
    Label(f, text=f"Hi {string.capwords(From_file[1])}", font=("Times New Roman", 10, "bold"), width=22, bg="green", fg="yellow").grid(row=1, column=0, sticky="nw")
    Label(f, text="Let's get started", font=("verdana", 9), bg="green", fg="yellow").grid(row=2, column=0, sticky="ne")
    Label(f, text="Powered by <ASAT DreamZ>", font=("verdana", 9), fg="yellow", bg="green").grid(row=1, column=2, sticky="ne")
    with open("files/Intro content/Session.txt", mode="r") as sfile:
        txt = sfile.readline()
        x = "Current Session: "+txt
    Label(f, text=x, bg="green", fg="yellow").grid(row=2, column=2, sticky="ne")
    Continuity()

    root3.mainloop()