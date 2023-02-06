import csv


def final_list():
    with open("files/Intro content/Final_list.csv", mode="r") as file2:
        reader = csv.reader(file2)
        lst1 = []
        for i in reader:
            lst1.append(i)
        x = lst1[0]
        return x


def SessionChoice():
    with open("files/Intro content/SessionChoices.csv", mode="r") as file:
        #s = ["2021-22", "2022-23", "2023-24"]
        reader = csv.reader(file)
        lst = []
        for i in reader:
            lst.append(i)
        return lst[0]
