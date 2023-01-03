import re

from datetime import date, time, datetime

def firstpage():
    while True:
        firstinput = input("1-Login\n2-signup\n")
        if int(firstinput)==1:
            login()
            break
        elif int(firstinput)==2:
            signup()
            break
        else:
            print("try again")

def secondpage(em):
    while True:
        firstinput = input("1-Create project\n2-List projects\n3-List own projects\n4-Delete own project\n")
        if int(firstinput)==1:
            projects(em)
            break
        elif int(firstinput)==2:
            lst(em)
            break
        elif int(firstinput) == 3:
            user_list(em)
            break
        elif int(firstinput) == 4:
            deleteproject(em)
            break
        else:
            print("try again")


def e_mail():
    while True:
        email = input("Please enter your mail: ")
        pat = r"^\D[\w\.]+@([\w-]+\.)+[\w-]{2,4}$"
        if re.match(pat, email):
            return email
            break
        else:
            print("not valid")





def check(name):
    while True:
        nm = input(f"Enter your {name} name: ")
        if not nm.isalpha():
            print("Invalid name")
        else:
            return nm
            break


def phnum():
    while True:
        pat = r"^01[0125][0-9]{8}$"
        phone = input("Enter your number: ")
        if re.match(pat, phone):
            return phone
            break
        else:
            print("phone number not valid!!")

def signup():
    firstname= check("First")
    lastname = check("Last")
    email = e_mail()
    p1 = password()
    phone = phnum()
    userinfo = f"{firstname}:{lastname}:{email}:{p1}:{phone}\n"
    append(userinfo)



def append(uinfo):
    try:
        fileobject = open("usrinformation/signup.txt", "a")
    except Exception as e:
        print(e)
    else:
        fileobject.write(uinfo)
        firstpage()



def login():
    email = e_mail()
    password = input("Enter your password\n")

    fileobj = open("usrinformation/signup.txt", "r")
    users = fileobj.readlines()

    for u in users:
        usrinfo = u.strip("\n")
        userinfo = usrinfo.split(":")
        if userinfo[2]==email and userinfo[3]==password:
            print("login successfully")
            secondpage(email)
            break
    else:
        print("user not found")
        firstpage()


def password():
    while True:
        p1 = input("Please Enter your password: ")
        p2 = input("Please Rewrite your password: ")
        if p1 != p2:
            print("Password can't be the same")
        else:
            return p1
            break


def projects(e):
    project = check("project")
    details = input("Enter project details: ")
    sdate = date.today()
    days = dte("Day")
    month = dte("Month")
    year = dte("Year")
    total = 250000
    enddate = f"{days}-{month}-{year}"
    projectInfo = f"{e}:{project}:{details}:{sdate}:{enddate}:{total}\n"
    try:
        fileobject = open("projectsinfo/project.txt", "a")
    except Exception as e:
        print(e)
    else:
        fileobject.write(projectInfo)
        secondpage(e)



def dte(t):
    while True:
        d = input(f"Enter your {t} end : ")
        if d.isdigit():
            return d
            break
        else:
            print("Inavlid")


def lst(em):
    fileobj = open("projectsinfo/project.txt", "r")
    users = fileobj.readlines()

    for u in users:
        usrinfo = u.strip("\n")
        print(usrinfo)

    secondpage(em)



def deleteproject(em):
    project_name = check("Project")
    fileobj = open("projectsinfo/project.txt", "r")
    users = fileobj.readlines()

    with open("projectsinfo/project.txt", "w") as f:
        for u in users:
            usrinfo = u.strip("\n")
            userinfo = usrinfo.split(":")
            if userinfo[0] == em and userinfo[1] == project_name in u:
                f.write(" \n")
            else:
                f.write(u)

        secondpage(em)





def user_list(em):
    fileobj = open("projectsinfo/project.txt", "r")
    users = fileobj.readlines()

    for u in users:
        usrinfo = u.strip("\n")
        userinfo = usrinfo.split(":")
        if userinfo[0] == em:
            print(usrinfo)

