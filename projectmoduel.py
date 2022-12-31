import re



def firstpage():
    firstinput = input("1-Login\n2-signup\n")
    if int(firstinput)==1:
        login()
    elif int(firstinput)==2:
        signup()


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
    fname = e_mail()
    password = input("Enter your password\n")

    fileobj = open("usrinformation/signup.txt", "r")
    users = fileobj.readlines()

    for u in users:
        usrinfo = u.strip("\n")
        userinfo = usrinfo.split(":")
        if userinfo[2]==fname and userinfo[3]==password:
            print("login successfully")
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


