import csv
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as msg
import section
import string
import Backbone
import folder


def View(root_window, class_name):
    def Print():
        lst = []
        lst2 = ["Adm No.","Student Name", "DOB", "Aadhar", "Address", "Phone No.","Whatsapp No.","Father Name"
                ,"Father Qual.", "Father Prof.","Mother Name","Mother Qual.","Mother Prof.","Social Stat."]
        try:
            with open("files/classes data/{}/{}.csv".format(class_name, class_name+sec.get()+section.gettingSession()), mode="r") as my_file2:
                reader2 = csv.reader(my_file2)
                for rec in reader2:
                    lst.append(rec)
            for i in lst:
                i = i[0:12]
            lst.insert(0, lst2)
            folder.Write(lst, class_name + sec.get())
        except FileNotFoundError:
            msg.showerror("Error", "Can't open a file that haven't yet created")

    def back():
        Backbone.CreateNewWindow2(root6)

    def reload():
        View(root6, class_name)

    def more(Student_names, index, Student_dictionary):
        root6.destroy()
        root7 = Tk()
        root7.geometry("1050x560")
        f2 = Frame(root7, width=1050, height=560, bg=bg).grid(row=0, column=0, columnspan=9, rowspan=20)
        row = 1
        column = 1
        Student_names2 = Student_names[index+1:len(Student_names)]
        for name in Student_names2:
            Label(f2, text=index+2, bg=bg, fg="green", font=("verdana", 10,"bold"), borderwidth=2, relief="groove").grid(row=row, column=0, sticky="nsew")
            index += 1

            required_data = [Student_dictionary[name][0], Student_dictionary[name][1], Student_dictionary[name][2], Student_dictionary[name][7],
                             Student_dictionary[name][10], Student_dictionary[name][5], Student_dictionary[name][6],
                             Student_dictionary[name][4]]
            for x in required_data:
                if x == "":
                    Label(f2, text="-", bg=bg, font=("verdana", 10), fg="blue", borderwidth=2, relief="groove").grid(row=row, column=column, sticky="nsew")
                else:
                    Label(f2, text=string.capwords(x), bg=bg, font=("verdana", 10), fg="blue", borderwidth=2, relief="groove").grid(row=row, column=column, sticky="nsew")
                column += 1
                if column == 9:
                    row = row + 1
                    column = 1
        Button(f2, text="BACK", command=lambda: View(root7, class_name), bg="sky blue").grid(row=0, column=0)

    def Operation(event):
        if sec.get() == "":
            msg.showinfo("IMPORTANT", "Please select a section to proceed")
        else:
            Menubar.add_command(label="Print", command=Print)
            try:
                with open("files/classes data/{}/".format(class_name) + class_name + sec.get() + Session+".csv", mode="r", newline="") as file:
                    filereader = csv.reader(file)
                    row = 2
                    column = 1
                    count = 0
                    Student_dict = dict()
                    Student_Names = []
                    total_Entries = []
                    for rec2 in filereader:
                        total_Entries.append(rec2)

                    #integrating with dictionary

                    for list1 in total_Entries:
                        Student_dict[list1[1]+str(list1[0])] = list1

                    for item in Student_dict:
                        Student_Names.append(item)

                    Student_Names.sort()
                    Label(f, text="Strength of Class : {}".format(len(Student_Names)), bg=bg, font=("verdana", 10, ("bold","italic"))
                          ,borderwidth=4, relief="groove", fg="green").grid(row=0, column=5, columnspan=2)

                    breaking = False
                    for name in Student_Names:
                        Label(f, text=Student_Names.index(name)+1, fg="green", bg=bg, font=("verdana", 10,"bold"), borderwidth=2, relief="groove").grid(row=row, column=0, sticky="nsew")

                        required_data = [Student_dict[name][0], Student_dict[name][1], Student_dict[name][2], Student_dict[name][7],
                                         Student_dict[name][10], Student_dict[name][5], Student_dict[name][6], Student_dict[name][4]]
                        for x in required_data:
                            if x == "":
                                Label(f, text="-", bg=bg, font=("verdana", 10), fg="blue", borderwidth=2, relief="groove").grid(row=row, column=column, sticky="nsew")
                            else:
                                Label(f, text=string.capwords(x), bg=bg, font=("verdana", 10), fg="blue", borderwidth=2, relief="groove").grid(row=row, column=column, sticky="nsew")
                            column += 1
                            if column == 9:
                                row = row+1
                                column = 1
                            if row == 20:
                                index = Student_Names.index(name)
                                Button(f, text="MORE", command=lambda: more(Student_Names, index, Student_dict), bg="sky blue").grid(row=0, column=8)
                                breaking = True
                                break
                        if breaking is True:
                            break
            except FileNotFoundError:
                res = msg.askokcancel("IMPORTANT", "{} {} haven't yet created. Want to Check status".format(class_name, sec.get()))
                if res is True:
                    Backbone.CreateNewWindow2(root6)
    bg = "#ffff80"
    root_window.destroy()
    root6 = Tk()
    root6.geometry("1050x560")
    root6.configure(bg="red")
    root6.title(class_name)
    f = Frame(root6, width=1050, height=560, bg=bg).grid(row=0, column=0, columnspan=9, rowspan=22)
    sec = StringVar()
    sec.set("")
    Label(f, text=class_name, bg="sky blue", fg="green", font=("verdana", 10, "bold")).grid(row=0, column=0, sticky="nsew")
    Label(f, text="SECTION :", bg=bg, font=("verdana", 10, "bold"), fg="red").grid(row=0, column=2, sticky="e")
    l = ttk.Combobox(f, width=10, textvariable=sec)
    l['values'] = section.gettingSections()
    l.grid(row=0, column=3)
    b = Button(f, text="OK", bg="sky blue")
    b.bind("<Button-1>", Operation)
    b.grid(row=0, column=4, sticky="w")
    #Label(f, text="Before working on a new section, please reload the window", bg=bg).grid(row=0, column=5, columnspan=6)

    data = []
    main_data = []
    with open("files/Intro content/data.csv", mode="r", newline="") as my_file:
        reader = csv.reader(my_file)
        for rec in reader:
            data.append(rec)
        main_data = data[0]
    col = 0
    for i in main_data:
        Label(f, text=i, bg=bg, fg="green", font=("verdana", 8, ("bold", "underline"))).grid(row=1, column=col)
        col += 1
    with open("files/Intro content/Session.txt", mode="r") as i_file:
        Session = i_file.readline()
    Menubar = Menu(root6)
    Menubar.add_command(label="Reload", command=reload)
    Menubar.add_command(label="Back", command=back)
    root6.config(menu=Menubar)
    root6.mainloop()