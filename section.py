import csv

def gettingSections():
    with open("files/Intro content/Section.txt", mode="r") as file:
        list1 = []
        sec = file.readline()
        for i in sec:
            list1.append(i)
        return list1


def gettingSession():
    with open("files/Intro content/Session.txt", mode="r") as i_file:
        session = i_file.readline()
        return session


def gettingPassword():
    with open("files/Intro content/IntroNew.csv", mode="r") as p_file:
        reader = csv.reader(p_file)
        main = []
        for rec in reader:
           main.append(rec)
        return main[0][2]

