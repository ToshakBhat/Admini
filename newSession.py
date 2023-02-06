from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as msg
import Backbone
import section
import csv


def FinalList(x, y):
    final = x + y
    with open("files/Intro content/Final_list.csv", mode="w+") as file:
        lst = []
        writer = csv.writer(file)
        for i in final:
            lst.append(i)
        writer.writerow(lst)


def New_Window(old_window, class_name):
    def back():
        Backbone.CreateNewWindow2(root4)

    def handleFile(Session, Section, class_data):
        with open("files/classes data/{}/".format(class_name)+class_name + Section + Session+".csv", newline='', mode="a+") as my_file:
            writer = csv.writer(my_file)
            writer.writerow(class_data)
            with open("files/Intro content/Session.txt", "w", newline="") as ifile:
                ifile.write(Session)

    def More_Entries(event):
        def tryExcept():
            try:
                x = int(list_of_vars[0].get())
            except ValueError:
                msg.showerror("Error", "All values are empty! Please fill the empty fields")
            else:
                class_data = [list_of_vars[0].get()]
                for j in range(1, 14):
                    class_data.append(list_of_vars[j].get())
                    list_of_vars[j].set("")
                class_data.append(list_of_vars[14].get())
                x = int(list_of_vars[0].get())
                x += 1
                list_of_vars[0].set(x)
                handleFile(Session, Section, class_data)
        Session = SessionName.get()
        Section = SectionName.get()
        if Session == "":
            msg.showerror("Error", "Please specify the Session to proceed")
        elif Section == "":
            msg.showerror("Error", "Please specify the Section to proceed")
        else:
            tryExcept()

    def Done(event):
        More_Entries(event)
        list_of_vars[0].set("")
        SectionName.set("")
        Button(root4, text="GO BACK", command=back, bg="sky blue").grid(row=9, column=3)

    old_window.destroy()
    root4 = Tk()
    root4.geometry("1000x530")
    root4.title("NEW SESSION")
    with open("files/Intro content/Session.txt", "r", newline="") as file:
        l = file.readline()

    f2 = Frame(root4, width=1000, height=530, bg="grey").grid(row=0, column=0, columnspan=4, rowspan=15)
    Label(f2, text=class_name, font=("verdana", 14, "bold"), bg="sky blue").grid(row=0, column=0, sticky="nsew")
    Label(f2, text="SESSION", font=("Bookman Old Style", 12), bg="yellow").grid(row=0, column=1, sticky="s")
    SessionName = StringVar()
    SectionName = StringVar()
    SessionName.set(l)
    #combobox for session
    box = ttk.Combobox(f2, textvariable=SessionName)
    box['values'] = ["2021-22", "2022-23", "2023-24"]
    box.grid(row=1, column=1, sticky="nn")
    Label(f2, text="SECTION", font=("Bookman Old Style", 12), bg="yellow").grid(row=0, column=2, sticky="s")
    #combobox for section
    with open("files/Intro content/Section.txt", mode="r") as file:
        list1 = []
        sec = file.readline()
        for i in sec:
            list1.append(i)
    box2 = ttk.Combobox(f2, textvariable=SectionName)
    box2['values'] = list1
    box2.grid(row=1, column=2, sticky="nn")

    f3 = Frame(f2, bg="tomato", height=400).grid(row=2, column=0, sticky="nsew", columnspan=2, rowspan=7, padx=10)
    f4 = Frame(f2, bg="tomato").grid(row=2, column=2, columnspan=2, rowspan=7, sticky="nsew", padx=10)
    #variable declaration
    AdmissionNumber = StringVar()
    NameOfStudent = StringVar()
    DateOfBirth = StringVar()
    AadharCard = StringVar()
    Address = StringVar()
    PhoneNumber = StringVar()
    WhatsappNumber = StringVar()
    FatherName = StringVar()
    MotherName = StringVar()
    FatherQualification = StringVar()
    FatherProfession = StringVar()
    MotherQualification = StringVar()
    MotherProfession = StringVar()
    SocialStatus = StringVar()
    #closed
    list_of_vars = [AdmissionNumber, NameOfStudent, DateOfBirth, AadharCard, Address, PhoneNumber, WhatsappNumber,
                    FatherName, FatherQualification, FatherProfession, MotherName, MotherQualification, MotherProfession
                    , SocialStatus, SectionName]
    list1 = ["Admission Number", "Name Of Student", "Date Of Birth", "Aadhar Card", "Address", "Phone Number", "Whatsapp Number"]
    list2 = ["Father Name", "Father Qualification", "Father Profession", "Mother Name", "Mother Qualification", "Mother Profession", "Social Status"]
    row = 2
    for i in range(0, 7):
        Label(f3, text=list1[i], width=20, font=("verdana", 10, "bold"), height=2, bg="yellow").grid(row=row, column=0, sticky="e")
        Label(f4, text=list2[i], width=20, font=("verdana", 10, "bold"), height=2, bg="yellow").grid(row=row, column=2, sticky="e")
        Entry(f3, width=20, font=("verdana", 12), textvariable=list_of_vars[i]).grid(row=row, column=1)
        row += 1
    Entry(f4, width=20, font=("verdana", 12), textvariable=list_of_vars[7]).grid(row=2, column=3)
    Entry(f4, width=20, font=("verdana", 12), textvariable=list_of_vars[10]).grid(row=5, column=3)
    #comboboxes
    new_box1 = ttk.Combobox(f4, width=20, textvariable=list_of_vars[8])
    new_box1['values'] = ["8TH PASS", "10TH PASS", "12TH PASS", "GRADUATE"]
    new_box1.grid(row=3, column=3)

    new_box2 = ttk.Combobox(f4, width=20, textvariable=list_of_vars[11])
    new_box2['values'] = ["8TH PASS", "10TH PASS", "12TH PASS", "GRADUATE"]
    new_box2.grid(row=6, column=3)

    new_box3 = ttk.Combobox(f4, width=20, textvariable=list_of_vars[9])
    new_box3['values'] = ["PRIVATE", "ARMY", "GOVERNMENT"]
    new_box3.grid(row=4, column=3)

    new_box4 = ttk.Combobox(f4, width=20, textvariable=list_of_vars[12])
    new_box4['values'] = ["HOUSEWIFE", "PRIVATE", "GOVERNMENT"]
    new_box4.grid(row=7, column=3)

    new_box5 = ttk.Combobox(f4, width=20, textvariable=list_of_vars[13])
    new_box5['values'] = ["GENERAL", "SC", "ST", "OBC"]
    new_box5.grid(row=8, column=3)
    #end of comboboxes
    b1 = Button(root4, text="MORE ENTRIES", width=15, font=("verdana", 9, "bold"), relief="groove", borderwidth=6,
                bg="sky blue")
    b1.bind("<Button-1>", More_Entries)
    b1.grid(row=9, column=1, sticky="s", pady=10)
    b2 = Button(root4, text="DONE", width=15, font=("verdana", 9, "bold"), relief="groove", borderwidth=6,
           bg="sky blue")
    b2.bind("<Button-1>", Done)
    b2.grid(row=9, column=2, sticky="s", pady=10)
    Menubar = Menu(root4)
    Menubar.add_command(label="Back", command=back)
    root4.config(menu=Menubar)
    root4.mainloop()
