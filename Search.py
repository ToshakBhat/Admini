import csv
from tkinter import *
from tkinter import messagebox as msg
import string
import Backbone
from section import gettingSession,gettingPassword
from ViewStatus import SpecificClass as get_Sections
from testingListbox import final_list
import Format
from conform import conformation
bg = "#ffff80"


def SearchStudent(previous_window, class_name):
    def back():
        Backbone.CreateNewWindow2(root8)

    def demo(event, lst1):
        res = msg.askokcancel("IMPORTANT", "Use this feature to edit wrong details or add new details.")
        if res is True:
            conformation(root8, lst1, class_name)
        else:
            pass

    def fetch():
        info = final_list()
        row = 2
        column = 0
        for i in range(1, 14):
            Label(SubFrame, text=info[i], font=("verdana", 10, "bold"), bg=bg, fg="green").grid(row=row, column=column, pady=5)
            row += 1
            if row == 9:
                column += 2
                row = 2
        number_searched = admission_number.get()
        admission_list = []
        for x in admission_dict:
            admission_list.append(x)
        admission_list.sort()
        beg = 0
        last = len(admission_list)
        try:
            while beg <= last:
                mid = (beg+last)/2
                mid = int(mid)
                if admission_list[mid] == number_searched:
                    row = 2
                    column = 1
                    lst1 = admission_dict[number_searched]
                    for item in range(1, 14):
                        label = Label(SubFrame, text=string.capwords(lst1[item]), font=("verdana", 10, "bold"), bg="sky blue")
                        label.grid(row=row, column=column, sticky="nsew", pady=5)
                        Label(frame, text=class_name + " " + lst1[14], fg="green", bg="sky blue",
                              font=("verdana", 18, "bold")).grid(row=0, column=0, columnspan=5, sticky="nsew")
                        b = Button(SubFrame, text="ALTER", bg="black", fg="white")
                        b.bind("<Button-1>", lambda event: demo(event, lst1))
                        b.grid(row=1, column=3, sticky="e", padx=3)
                        row += 1
                        if row == 9:
                            column = 3
                            row = 2
                    break
                elif admission_list[mid] < number_searched:
                    beg = mid+1
                elif admission_list[mid] > number_searched:
                    last = mid-1
                else:
                    print("Value not in list")
                    break
        except IndexError:
            msg.showerror("ERROR", "This admission number doesn't exist")
    previous_window.destroy()
    root8 = Tk()
    root8.geometry("1000x520")
    root8.title("Search")
    root8.configure(bg="red")
    #declaration
    admission_number = StringVar()
    session = gettingSession()
    Sections_list = get_Sections(class_name)

    frame = Frame(root8, width=1000, height=520, bg="#ffff80").grid(row=0, column=0, columnspan=5, rowspan=10)
    Label(frame, text="SEARCH STUDENT ("+class_name + ")", fg="green", bg="sky blue", font=("verdana", 18, "bold")).grid(row=0, column=0, columnspan=5, sticky="nsew")
    Label(frame, text="ADMISSION NUMBER :", font=("verdana", 12, "bold"), bg=bg).grid(row=1, column=0, sticky="nsew")
    Entry(frame, textvariable=admission_number).grid(row=1, column=1, sticky="w")
    Button(frame, text="SEARCH", command=fetch, bg="black", fg="white").grid(row=1, column=2, sticky="w")

    #New Frame
    SubFrame = Frame(frame, width=300, height=80, bg=bg).grid(row=2, column=0, rowspan=8, columnspan=5, sticky="nsew", pady=10, padx=10)

    file_data = []
    admission_dict = {}
    for sec in Sections_list:
        with open("files/classes data/{}/".format(class_name.upper()) + class_name.upper() + sec + session+".csv", mode="r"
                  ) as my_file:
            reader = csv.reader(my_file)
            for rec in reader:
                file_data.append(rec)
            for i in file_data:
                admission_dict[i[0]] = i


    #Menu bar
    Menubar = Menu(root8)
    #Menubar.add_command(label="Update Details", command=fetch)
    Menubar.add_command(label="Back", command=back)
    root8.config(menu=Menubar)
    root8.mainloop()