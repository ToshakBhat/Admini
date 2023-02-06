import csv
from tkinter import *
from tkinter import messagebox as msg
from testingListbox import final_list
import string
from section import gettingSession
import Search
bg = "#ffff80"


def Alter(list1, window, name_of_class):
    def back():
        Search.SearchStudent(root, name_of_class)

    def getting():
        new_data = []
        for i in list_of_vars:
            new_data.append(i.get())
        main_data = []
        with open("files/classes data/{}/".format(name_of_class.upper())+name_of_class.upper()+list1[-1]+gettingSession()
                  +".csv", mode="r") as my_file:
            reader = csv.reader(my_file)
            for rec in reader:
                main_data.append(rec)
        for list2 in main_data:
            if list2[0] == list1[0]:
                for x in range(1, 14):
                    list2[x] = new_data[x]
                with open("files/classes data/{}/".format(name_of_class.upper()) + name_of_class.upper() + list1[
                    -1] + gettingSession()
                          + ".csv", mode="w", newline='') as my_file2:
                    writer = csv.writer(my_file2)
                    writer.writerows(main_data)

        res = msg.showinfo("SUCCESS", "Student Profile updated Successfully.")
        if res == "ok":
            back()
    window.destroy()
    root = Tk()
    root.geometry("700x555")
    root.config(bg="red")
    frame = Frame(root, width=700, height=550, bg=bg).grid(row=0, column=0, rowspan=14, columnspan=3)
    Label(frame, text=name_of_class+" "+list1[-1], fg="green", font=("verdana", 12, ("bold", "underline")), bg=bg
          , borderwidth=2, relief="groove").grid(row=0, column=0, sticky="nw")
    Label(frame, text="ADMISSION NO. " + list1[0], font=("Times New Roman", 14, "bold"), bg=bg, fg="blue").grid(row=0, column=0,
                                                                                              columnspan=3)
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
    Final_list = final_list()
    # closed
    list_of_vars = [AdmissionNumber, NameOfStudent, DateOfBirth, AadharCard, Address, PhoneNumber, WhatsappNumber,
                    FatherName, FatherQualification, FatherProfession, MotherName, MotherQualification, MotherProfession
        , SocialStatus]
    for var in range(0, 14):
        list_of_vars[var].set(string.capwords(list1[var]))
    row = 1
    for i in range(1, 14):
        Label(frame, text=Final_list[i].upper(), bg="sky blue", fg="green", font=("Times New Roman", 12, "bold"), borderwidth=2
              , relief="groove").grid(row=row, column=0, sticky="nsew", padx=3)
        if list1[i] == "":
            Label(frame, text="<Not Provided>", bg=bg,fg="green", font=("Times New Roman", 12), borderwidth=2
                  ,relief="groove").grid(row=row, column=1, sticky="nsew")
        else:
            Label(frame, text=string.capwords(list1[i]), bg=bg,fg="green", font=("Times New Roman", 12), borderwidth=2
              , relief="groove").grid(row=row, column=1, sticky="nsew")
        Entry(frame, text=list_of_vars[i], borderwidth=2, relief="groove").grid(row=row, column=2)
        row += 1

    Button(frame, text="SAVE", command=getting, bg="sky blue").grid(row=0, column=2)
    Menubar = Menu(root)
    #Menubar.add_command(label="Reload", command=reload)
    Menubar.add_command(label="Back", command=back)
    root.config(menu=Menubar)
    root.mainloop()
"""
lst = ["A","B","C"]
Alter(lst)"""