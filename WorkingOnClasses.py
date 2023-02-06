from tkinter import *
import newSession as NEW_SESSION
import View_Classes
import Search


def gettingWindowAndClass(window, class_name, color):
    def search():
        Search.SearchStudent(window, class_name)

    def view(event):
        View_Classes.View(window, class_name)

    def click(event):
        NEW_SESSION.New_Window(window, class_name)
    frame = Frame(window, bg="grey", width=450, height=370, borderwidth=6, relief="groove").grid(row=3, column=0, rowspan=8, columnspan=3, pady=4)
    Label(frame, text=class_name, font=("verdana", 14, "bold"), relief="groove", borderwidth=6, bg=color, fg="green").grid(row=3, column=1, sticky="n", pady=2)
    b1 = Button(frame, text="NEW ADMISSION", font=("verdana", 14, "bold"), width=20, bg="green", fg=color)
    b1.bind("<Button-1>", click)
    b1.grid(row=4, column=1)
    #b2 = Button(frame, text="MODIFY", font=("verdana", 14, "bold"), width=20, bg="green", fg=color).grid(row=5, column=1)

    b3 = Button(frame, text="VIEW CLASS", font=("verdana", 14, "bold"), width=20, bg="green", fg=color)
    b3.bind("<Button-1>", view)
    b3.grid(row=5, column=1)

    b4 = Button(frame, text="SEARCH / MODIFY", command=search, font=("verdana", 14, "bold"), width=20, bg="green", fg=color).grid(row=6, column=1)