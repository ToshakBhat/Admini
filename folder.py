import csv
import os
from tkinter import messagebox as msg
main_dir = os.getcwd()


def MakeFolder(folderName):
    with open("files/Intro content/folder.txt", mode="w+") as file:
        file.write(folderName)
    prof = os.environ['USERPROFILE']
    desktop = os.path.join(prof, 'Desktop')
    try:
        os.chdir(desktop)
        os.mkdir(folderName)
        os.chdir(main_dir)
    except FileExistsError:
        os.chdir(main_dir)
        msg.showerror("Error", "Folder already exists by the provided name.")
        with open("files/Intro content/folder.txt", mode="w+") as file:
            file.write("Admini-School")
        os.chdir(desktop)
        os.mkdir("Admini-School")
        os.chdir(main_dir)


def Write(list1, class_):
    prof = os.environ['USERPROFILE']
    desktop = os.path.join(prof, 'Desktop')

    with open("files/Intro content/folder.txt", mode="r") as file:
        name = file.readline()

    os.chdir(desktop)
    with open(desktop+"/{}/{}.csv".format(name, class_), mode="w+", newline="") as my_file:
        writer = csv.writer(my_file)
        writer.writerows(list1)
    os.startfile(desktop+"/{}/{}.csv".format(name, class_))
    os.chdir(main_dir)
