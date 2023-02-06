from tkinter import *
import csv
from tkinter import messagebox as msg


def SpecificClass(class_name):
    with open("files/Intro content/Session.txt", mode="r") as session:
        sessionName = session.read()
    with open("files/Intro content/Section.txt", mode="r") as section:
        sections = section.readline()
    wcount = 0
    wlist = []
    slist = []
    for sec in range(0, len(sections)):
        try:
            with open(
                    "files/classes data/{}/".format(class_name.upper()) + class_name.upper() + sections[sec] + sessionName + ".csv",
                    mode="r",
                    newline="") as my_file:
                slist.append(sections[sec])

        except FileNotFoundError:
            wcount += 1
            wlist.append(sections[sec])
    return slist


def Status(classes):
    root31 = Tk()
    root31.geometry("400x400")
    bg = "#ffff80"
    with open("files/Intro content/Session.txt", mode="r") as session:
        sessionName = session.read()

    with open("files/Intro content/Section.txt", mode="r") as section:
        sections = section.readline()
    list1 = []
    count = 0
    for i in range(3, len(classes)):
        count += 1
        list1.append(classes[i])
    f = Frame(root31, width=400, height=400, bg=bg).grid(row=0, column=0, columnspan=3, rowspan=count+1)
    Label(root31, text="CLASS", fg=bg, bg="green", font=("verdana", 9, "bold")).grid(row=0, column=0, sticky="nsew")
    Label(root31, text="EMPTY SECTIONS", fg=bg, bg="green", font=("verdana", 9, "bold")).grid(row=0, column=1, sticky="nsew")
    Label(root31, text="SECTIONS CREATED", fg=bg, bg="green", font=("verdana", 9, "bold")).grid(row=0, column=2, sticky="nsew")
    row = 1
    for name in list1:
        Label(root31, text=name, fg="yellow", bg="green", font=("verdana", 9, "bold")).grid(row=row, column=0,
                                                                                   sticky="nsew")
        wcount = 0
        wlist = []
        slist=[]
        for sec in range(0, len(sections)):
            try:
                with open("files/classes data/{}/".format(name.upper())+name.upper()+sections[sec]+sessionName+".csv" ,mode="r",
                            newline="") as my_file:
                    slist.append(sections[sec] + ",")
            except FileNotFoundError:
                wcount += 1
                wlist.append(sections[sec] + ",")
            else:
                pass
        if wlist == []:
            Label(root31, text="Nil", font=("Bookman Old Style", 10, "italic"), bg=bg).grid(row=row, column=1, padx=2)
        else:
            Label(root31, text=wlist, font=("Bookman Old Style", 10, "italic"), bg=bg).grid(row=row, column=1, padx=2)
        if slist == []:
            Label(root31, text="Nil", font=("Bookman Old Style", 10, "italic"), bg=bg).grid(row=row, column=2)
        else:
            Label(root31, text=slist, font=("Bookman Old Style", 10, "italic"), bg=bg).grid(row=row, column=2)
        row += 1
    root31.mainloop()