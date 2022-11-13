import time
import math
import os
import sys
import webbrowser
import pwinput
#Variables section
forever = 1 #forever loop
global userdict
userdict = {
    "admin":".admin",
}
global user
user = "admin"
global sys_base
sys_base = os.name
global sb_trans
if (sys_base == "nt"):
    sb_trans = "Windows"
    print("PynaryOs based on Windows")
elif (sys_base == "posix"):
    sb_trans =  "MacOs/Linux/UNIX"
    print("PynaryOs based on MacOs/Linux/UNIX")
global userkey
userkey = ""
global uservalue
uservalue = ""
global filenow_name
filenow_name = ""
global filenow
filenow = ""
global pwd
pwd = "user"
global pwdcon
pwdcon = "null"
global lockstatus
lockstatus = 0
global lockpwd
lockpwd = "null"
global timerv
timerv = 0
global timerc
timerc = 0
global log
global calaction
calaction = 0
global createfile
global temps
temps = ""
global userc 
userc = ""
global ini_log
ini_log = "Activate Os on " + str(sb_trans)
log = [ini_log]
logtxt = open("PynaryLog.txt", "w")
#functions selection
def cal(): #calculator
    inp1 = ""
    inp2 = ""
#input2
    outp = ""
#output
    ans = ""
#action
    lst = ""
#show list or not
    time.sleep(1)
    print("Welcome to calculator!")
    lst = str(input("Do you need calculator command list? y/n "))
    if (lst == "y"):
        print('''
    sum: sum up
    sub: substract 
    times: multiply
    div: division
    remain: get the remainder of the division
    power: get a specific power of a number
    sqrt: get the square root of a number
    sq: get the square of a number
    cube: get the cube of a number
    ''')
    elif (lst == "n"):
        print("Skipping to enter input...")
        time.sleep(1)
    else:
        print("Input is unidentified")
    ans = str(input("Select action from the list "))
    if (ans == "sum" or ans == "sub" or ans == "times" or ans == "div" or ans =="remain") or ans == "power":
        if (ans == "sum"):
            inp1 = float(input("Enter the 1st number "))
            inp2 = float(input("Enter the 2nd number "))
            calaction = 1
            outp = int(inp1) + int(inp2)
            print(outp)
        elif (ans == "sub"):
            inp1 = float(input("Enter the 1st number "))
            inp2 = float(input("Enter the 2nd number "))
            outp = int(inp1) - int(inp2)
            print(outp)
            calaction = 1
        elif (ans == "times"):
            inp1 = float(input("Enter the 1st number "))
            inp2 = float(input("Enter the 2nd number "))
            outp = int(inp1) * int(inp2)
            print(outp)
            calaction = 1
        elif (ans == "div"):
            inp1 = float(input("Enter the 1st number "))
            inp2 = float(input("Enter the 2nd number "))
            outp = int(inp1) / int(inp2)
            print(outp)
            calaction = 1
        elif (ans == "remain"):
            inp1 = float(input("Enter the 1st number "))
            inp2 = float(input("Enter the 2nd number "))
            outp = int(inp1) % int(inp2)
            print(outp)
            calaction = 1
        elif (ans == "power"):
            inp1 = float(input("Enter the number "))
            inp2 = int(input("Enter the power (Must be an integer) " ))
            outp = float(inp1) ** float(inp2)
            print(outp)
            calaction = 1
        else:
            print("Unknown command")
    elif (ans == "sqrt" or ans == "sq" or ans == "cube"):
        if (ans == "sqrt"):
            inp1 = float(input("Enter the number"))
            outp = math.sqrt(inp1)
            print(outp)
            calaction = 2
        elif (ans == "sq"):
            inp1 = float(input("Enter the number"))
            outp = inp1 ** 2
            print(outp)
            calaction = 2
        elif (ans == "cube"):
            inp1 = float(input("Enter the number"))
            outp = inp1 ** 3
            print(outp)
            calaction = 2
    else:
        print("Unidentified action")
    #calculator logging
    if (calaction == 1): #calculator action type
        log.append(str(inp1) + str(" ") + str(inp2) + str(" = ") + str (outp) + str(".") + str(ans))
    elif (calaction == 2): #calculator action type
        log.append(str(inp1) + str(" = ") + str(outp) + str(".") + str(ans))
    else:
        print("Unexpected error")
    outp = ""
def changepw(): 
    global pwd
    pwd = pwinput.pwinput(prompt="Enter new password: ")
    global pwdcon
    pwdcon = pwinput.pwinput("Enter new password again: ")
    if (pwdcon == pwd):
        userdict[userc] = str(pwd)
        print("Password changed sucessfully")
    else:
        print("Password unmatch. Try again.")
def exportlog_f():
    for content in log:
        logtxt.write(str(content) + "\n")
    print("Exported. It can be found in your folder.")
    closelogtxt()
def lock():
    global lockstatus
    lockstatus = 1
    print("locked")
    lockpwd = ""
def timer():
    global timerv
    timerv = float(input("Start timer for _____ second(s) "))
    global timerc
    timerc = float(0)
    log.append(str("Timer: ") + str(timerv))
    while (timerc < timerv):
        timerc += 0.1
        time.sleep(0.1)
    print("Time's up!")
def showlog():
    log.append("Show log")
    for content in log:
        print(content)
    exportlog = str(input("Export log as a .txt file? y/n "))
    if (exportlog == "y"):
        exportlog_f()
    else:
        print("action skipped")
def closelogtxt():
    logtxt.close()
def filecreate():
    global filename_create
    filename_create = str(input("Enter file name (add .txt at the end) "))
    createfile = open(filename_create, "w")
    log.append(str("Create file: ") + str(filename_create))
    global filecontent
    filecontent = ""
    filecontent = str(input("Enter the content to be written in the file. "))
    createfile.write(filecontent)
    log.append(str("File content = ") + str(filecontent))
    print("File has been created and filled with content.")
    filecontent = ""
    filename_create = ""
    createfile.close()
def deletefile(): #delete file
    global deletefile_name
    deletefile_name = str(input("Enter the file name to be deleted. (Add .txt at the end) "))
    os.remove(str(deletefile_name))
    log.append(str("Delete file: ") + str(deletefile_name))
    print("File has been put into your recycle bin.")
    deletefile_name = ""
def readfile(): #Open a file (readonly)
    filenow_name = str(input("Enter file name: "))
    filenow = open(filenow_name, "r")
    filenow_content = filenow.read()
    print(filenow_content)
    filenow_content = ""
    filenow_name = ""
    filenow.close()
def website_o():
    global url
    url = str(input("Enter website: " + "\n"))
    webbrowser.open(url)
    log.append("Open wensite url: " + url)
def adminm():
    cont = 1
    print("Loading admin mode...")
    time.sleep(1.5)
    print('Welcome to admin mode.')
    print('''
add - Add user
del - Delete user
view - view user list and password
quit - Quit admin mode
''')
    while (cont == 1):
        actiona = str(input("Select action: "))
        if (actiona == "add"):
            temps = str(input("Username: "))
            userkey = temps
            temps = str(pwinput.pwinput("Password: "))
            uservalue = temps
            temps = ""
            userdict[userkey] = uservalue
            userkey = ""
            uservalue = ""
        elif (actiona == "del"):
            temps = str(input("Username" + "\n"))
            userkey = temps
            if (userkey != "admin"):
                temps = str(pwinput.pwinput("Enter Admin Password: "))
                adminpwd = userdict.get("admin")
                if (temps == adminpwd):
                    print("Deleting...")
                    time.sleep(1)
                    del userdict[userkey]
                    userkey = ""
                    temps = ""
                    adminpwd = ""
                else:
                    print("Incorrect pwd")
            else:
                print("You can't delete admin!")
        elif (actiona == "view"):
            print(userdict)
        elif (actiona == "quit"):
            cont = 0
            continue
        cont_r = str(input("Exit admin mode? (y/n)"))
        if (cont_r == "y"):
            cont = 0
            continue
        elif (cont_r == "n"):
            cont = 1
            continue
        else:
            print("?_?")
print("Welcome to PynaryOs. Type help.cmdlist to get command list. ")
while (forever <= 10):
    if (lockstatus == 0):
        action = input("Enter a command: ")
        if (action == "calculator"): #selected calculator
            cal()
            continue #log in def cal()
        elif (action == "changepwd"): #change pwd
            changepw()
            log.append("Change password")
            continue
        elif (action == "showpwd"): #show pwd
            print (pwd)
            log.append("Show password")
            continue
        elif (action == "about"): #about
            print ("Pynary means of Python and Binary (Means machine code)  :)")
            log.append("Get name_info")
            continue
        elif (action == "lock"): #lock
            lock()
            log.append("Lock acc")
            continue
        elif (action == "website"):
            website_o()
            continue
        elif (action == "projweb"):
            log.append("Go to Github/thisproject")
            webbrowser.open("https://www.github.com/lpkpaco/PynaryOs")
            continue
        elif (action == "help.cmdlist"): #command list
            print('''
            calculator - use calculator
            lock - lock the system
            showpwd - show system password (to be used to unlock system)
            changepwd - change the system password
            timer - start timer
            about - get for info
            help.cmdlist - get command list
            file.create - create a txt file
            file.delete - delete an existing file in the same folder (or add a path)
            file.read - read a existing file (read only)
            exit - exit PynaryOs
            showlog - show or export log
            dev.process - show the current development process
            projweb - go to the project page
            website - access the internet ''')
            log.append("help.cmdlist")
            continue
        elif (action == "admin"):
            if (user == "admin"):
                adminm()
            else:
                print("You are not admin")
            continue #log in def adminm()
        elif (action == "timer"): #timer
            timer()
            continue #log in def timer()
        elif (action == "showlog"): #showlog
            showlog() #log in def showlog()
            continue
        elif (action == "file.create"): #create a file
            filecreate()
            continue #log in def filecreate()
        elif (action == "file.delete"): #log in def deletefile
            deletefile()
            continue
        elif (action == "file.read"): #log in def readfile()
            readfile()
            continue
        elif (action == "exit"): #exit PynaryOs
            print("Exiting PynaryOs")
            time.sleep(2)
            log.append("Exit PynaryOs")
            exit()
        elif (action == "dev.process"):
            print('''
            Current process:
            Security: yes
            Control over system performance: no
            Job account: half
            error detecting aids: no
            coordination between other software and users: no
            memory management: no
            processor management: no
            device management: N/A
            file management: half
            ''')
            continue
        else:
            print("Unknown command")
            log.append("Unknown command")
    elif (lockstatus == 1):
        userl = str(input("Username: "))
        if userl in userdict:
            if (userl == "admin"):
                user = "admin"
            else:
                user = "user"
            userc = str(userl)
            userpwd = str(pwinput.pwinput(prompt="Password: "))
            temps = str(userdict[userl])
            if (userpwd == temps):
                lockstatus = 0
                continue
            else:
                print("Wrong pwd")
                continue
        else:
            print("User not found")       
    else:
        print("Unknown error occurred")
        log.append("Unknown error_login")
