from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as msg
import csv
from testingListbox import SessionChoice
import Backbone
bg = "#ffff80"


def message():
    res = msg.showinfo("NOTICE", "This feature will be made available in next update.STAY TUNED")


def upgradingClass2(class1, sec1, class2, sec2, pre_session, new_session, window):
    window.destroy()
    root51 = Tk()
    root51.geometry("1000x535")
    main_data_list = []
    try:
        with open("files/classes data/{}/".format(class1.upper()) + class1.upper() + sec1+pre_session+".csv", mode="r"
                  ) as my_file:
            reader = csv.reader(my_file)
            for rec in reader:
                main_data_list.append(rec)
    except FileNotFoundError:
        msg.showerror("ERROR", class1+sec1+"haven't yet created")
        upgradingClass()
        root51.destroy()
    n = len(main_data_list)
    f = Frame(root51, width=1000, height=535, bg=bg).grid(row=0, column=0, columnspan=6, rowspan=n + 2,
                                                              sticky="nsew")
    Label(root51, text=class1 + " " + sec1 + "-->" + " " + class2 + sec2, fg="green", bg="sky blue").grid(row=0, column=0, sticky="nsew"
                                                                               , columnspan=2)
    Label(root51, text="Admission No", font=("verdana", 10, "bold"),bg=bg).grid(row=1, column=0, sticky="nsew")
    Label(root51, text="Student Name", font=("verdana", 10, "bold"),bg=bg).grid(row=1, column=1, sticky="nsew")
    Label(root51, text="Father Name", font=("verdana", 10, "bold"),bg=bg).grid(row=1, column=2, sticky="nsew")
    row = 2
    for i in main_data_list:
        Label(root51, text=i[0], borderwidth=2, relief="groove", font=("verdana", 10,"bold"),bg=bg).grid(row=row, column=0
                                                                                                   ,sticky="nsew")
        Label(root51, text=i[1], borderwidth=2, relief="groove", font=("verdana", 10,"bold"),bg=bg).grid(row=row, column=1,
                                                                                                   sticky="nsew")
        #Label(root51, text=i[2], borderwidth=2, relief="groove", font=("verdana", 10,"bold")).grid(row=row, column=2)
        Label(root51, text=i[7], borderwidth=2, relief="groove", font=("verdana", 10,"bold"),bg=bg).grid(row=row, column=2,
                                                                                                   sticky="nsew")
        Button(root51, text="Promote", bg="green").grid(row=row, column=3)
        Button(root51, text="Demote", bg="tomato").grid(row=row, column=4)
        Button(root51, text="Delete", bg="grey").grid(row=row, column=5)
        row += 1

    root51.mainloop()


def upgradingClass():
    def Done():
        with open("files/Intro content/Session.txt") as i_file:
            read = i_file.readline()
        sessions = SessionChoice()
        index = sessions.index(read)
        res = msg.askokcancel("IMPORTANT", "Exporting Data from {} to {}".format(c1.get() + " " + c2.get() + "("+read+")",
                                                                           c3.get() + " " + c4.get() + "("+sessions[index+1]
                                                                           +")"))
        if not res:
            pass
        else:
             upgradingClass2(c1.get(), c2.get(), c3.get(), c4.get(), read, sessions[index+1], root5)

    root5 = Tk()
    root5.geometry("300x300")
    Frame(root5, width=300, height=300, bg="green").grid(row=0, column=0, rowspan=5, columnspan=1)
    Label(root5, text="PROMOTE FROM", fg="yellow", font=("verdana", 12, "bold"), bg="green").grid(row=0, column=0)

    with open("files/Intro content/IntroNew.csv", mode="r") as my_file:
        reader = csv.reader(my_file)
        l = []
        for rec in reader:
            l.extend(rec)
    with open("files/Intro content/Section.txt", mode="r") as file:
        reader2 = file.readline()
        l2 = []
        for rec in reader2:
            l2.append(rec)

    #Class box
    Class_ = StringVar()
    c1 = ttk.Combobox(root5, width=15, textvariable=Class_)
    c1['values'] = l[3:len(l)]
    c1.grid(row=1, column=0, sticky="nw", padx=5)

    #SectionBox
    sec = StringVar()
    c2 = ttk.Combobox(root5, width=15, textvariable=sec)
    c2['values'] = l2
    c2.grid(row=1, column=0, sticky="ne", padx=5)
    Label(root5, text="TO", fg="yellow", font=("verdana", 12, "bold"), bg="green").grid(row=2, column=0)

    #Class Box2
    Class_2 = StringVar()
    c3 = ttk.Combobox(root5, width=15, textvariable=Class_2)
    c3['values'] = l[3:len(l)]
    c3.grid(row=3, column=0, sticky="nw", padx=5)

    #SectionBox2
    sec2 = StringVar()
    c4 = ttk.Combobox(root5, width=15, textvariable=sec2)
    c4['values'] = l2
    c4.grid(row=3, column=0, sticky="ne", padx=5)

    Button(root5, text="DONE", fg="white", bg="black", font=("verdana", 12, "bold"), command=Done).grid(row=4, column=0)
    root5.mainloop()