from tkinter import *
from tkinter import messagebox as msg
from tkinter import ttk
import csv
import folder as fl
import Backbone


def CreateNewWindow(window1):
    def done(l2):
        with open("files/Intro content/Section.txt", mode="w") as my_file:
            list1 = []
            c2 = l2.curselection()
            for item in c2:
                x = l2.get(item)
                list1.append(x)
            my_file.writelines(list1)

    def section():
        root21 = Tk()
        root21.geometry("300x200")
        fn = Frame(root21, width=300, height=200).grid(row=0, column=0, columnspan=1, rowspan=5)

        Section_list = ["A", "B", "C", "D", "E", "F", "G"]
        Label(root21, text="SECTIONS", font=("Times New Roman", 10), bg="yellow").grid(row=0, column=0, columnspan=2, sticky="nsew", pady=5)
        l2 = Listbox(root21,  height=7, width=20, selectmode="multiple", borderwidth=4, relief="groove")
        for j in range(0, len(Section_list)):
            l2.insert(j, Section_list[j])
        l2.grid(row=1, column=0)
        Button(root21, text="DONE", font=("verdana", 12, "bold"), command=lambda: done(l2)).grid(row=2, column=0)
        root21.mainloop()

    def save():
        with open("files/Intro content/IntroNew.csv", "w+", newline='') as myfile:
            filewriter = csv.writer(myfile)
            BasicDetails = [(institution_name.get()).upper(), (user_name.get()).upper(),  (password.get()).upper()]
            Classes_Selected = list()
            c = l.curselection()
            for item in c:
                x = l.get(item)
                Classes_Selected.append(x)
            res = msg.askyesno("IMPORTANT", f"Institution Name : {institution_name.get()} , User Name : {user_name.get()},"
                                      f" Password : {password.get()}, Classes Selected : {Classes_Selected}")
            if res:
                filewriter.writerow(BasicDetails)
                filewriter.writerow(Classes_Selected)
                msg.showinfo("SUCCESS", "Details saved successfully")
                with open("files/Intro content/NewUser.txt", mode="w") as file:
                    file.write("Disabled")
                fl.MakeFolder(folder.get())
                root2.destroy()
            else:
                institution_name.set("")
                user_name.set("")
                password.set("")

    def verify():
        if folder.get() == "" or institution_name.get() == "" or password.get() == "" or user_name.get() == "":
            msg.showerror("Error", "Fill up the credentials.")
        else:
            save()
    window1.destroy()
    root2 = Tk()
    root2.geometry("950x550")
    #root2.minsize(750, 500)
    #root2.maxsize(750, 500)
    #var declaration
    institution_name = StringVar()
    user_name = StringVar()
    password = StringVar()
    folder = StringVar()
    num_of_sections = StringVar()
    font=("Times New Roman", 12, "bold")
    f1 = Frame(root2, width=950, height=550, bg="yellow").grid(row=0, column=0, columnspan=4, rowspan=10)
    Label(root2, text="ADMINISTRATION SETUP", bg="black", fg="white", font=font).grid(row=0, column=0, columnspan=4, sticky="nsew", pady=10)
    Label(root2, text="INSTITUTION NAME", font=font, bg="yellow").grid(row=1, column=0, sticky="nsew")
    #Label(root2, text="(should not be soo long)").grid(row=1, column=0, sticky="s")
    Entry(root2, textvariable=institution_name, width=40).grid(row=1, column=1, sticky="w")
    Label(root2, text="ADMINISTRATOR NAME", font=font, bg="yellow").grid(row=2, column=0, sticky="nsew")
    Entry(root2, textvariable=user_name, width=33).grid(row=2, column=1, sticky="w")
    Label(root2, text="PASSWORD", font=font, bg="yellow").grid(row=3, column=0, sticky="nsew")
    Entry(root2, textvariable=password).grid(row=3, column=1, sticky="w")

    Label(root2, text="CLASSES", font=font, bg="yellow").grid(row=1, column=2, rowspan=2, sticky="nsew")
    #Label(root2, text="*Minimum 6 classes should be selected", bg="yellow").grid(row=1, column=2, rowspan=2, sticky="n")
    Class_list = ["PRE-NURSERY", "NURSERY", "LKG", "UKG", "1ST", "2ND", "3RD", "4TH", "5TH", "6TH", "7TH", "8TH",
                  "9TH", "10TH", "11TH", "12TH"]
    l = Listbox(f1, height=10, width=30, selectmode="multiple", borderwidth=6, relief="groove")
    for i in range(0, len(Class_list)):
        l.insert(i, Class_list[i])
    l.grid(row=1, column=3, rowspan=2)
    scroll = Scrollbar(f1, command=l.yview)
    l.configure(yscrollcommand=scroll.set)
    l.grid(row=1, column=3, sticky='nsew')
    scroll.grid(row=1, column=3, sticky="e")

    Label(root2, text="Personalised FOLDER NAME :", font=font, bg="yellow").grid(row=4, column=0)
    Entry(root2, textvariable=folder, width=30).grid(row=4, column=1, sticky="w")
    #Label(root2, text="*You can make changes in Profile in future also.", font=font, bg="yellow").grid(row=5, column=0, sticky="nsew", columnspan=2)
    Button(root2, text="SAVE", bg="black", fg="white", font=font, command=verify).grid(row=6, column=0, columnspan=4)
    #menu
    menubar = Menu(root2)
    #menubar.add_command(label="EXIT", command=exit)
    menubar.add_command(label="SECTIONS", command=section)
    root2.config(menu=menubar)
    mainloop()