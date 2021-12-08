import time
import math
#Variables section
forever = 1 #forever loop
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
    ''')
    elif (lst == "n"):
        print("Skipping to enter input...")
        time.sleep(1)
    else:
        print("Input is unidentified")
    ans = str(input("Select action from the list "))
    if (ans == "sum" or ans == "sub" or ans == "times" or ans == "div" or ans =="remain"):
        inp1 = int(input("Enter the 1st integer"))
        inp2 = int(input("Enter the 2nd integer"))
        if (ans == "sum"):
            outp = int(inp1) + int(inp2)
            print(outp)
        elif (ans == "sub"):
            outp = int(inp1) - int(inp2)
            print(outp)
        elif (ans == "times"):
            outp = int(inp1) * int(inp2)
            print(outp)
        elif (ans == "div"):
            outp = int(inp1) / int(inp2)
            print(outp)
        elif (ans == "remain"):
            outp = int(inp1) % int(inp2)
            print(outp)
        else:
            print("Work in progress")
    else:
        print("Unidentified action")
    outp = ""
def changepw(): 
    global pwd
    pwd = input("Enter new password ")
    global pwdcon
    pwdcon = input("Enter password again ")
    if (pwdcon == pwd):
        print("Password changed: " + str(pwd))
    else:
        print("Password unmatch. Try again.")
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
    while (timerc < timerv):
        time.sleep(0.1)
        timerc += 0.1
    print("Time's up!")
while (forever <= 10):
    if (lockstatus == 0):
        action = input("Hello world! Welcome to PynaryOs. Enter command. ")
        if (action == "calculator"): #selected calculator
            cal()
            continue
        if (action == "changepwd"): #change pwd
            changepw()
            continue
        if (action == "showpwd"): #show pwd
            print (pwd)
            continue
        if (action == "about"): #about
            print ("Pynary means of Python and Binary (Means machine code)  :)")
            continue
        if (action == "lock"): #lock
            lock()
            continue
        if (action == "command"): #command list
            print('''
            calculator - use calculator
            lock - lock the system
            showpwd - show system password (to be used to unlock system)
            changepwd - change the system password
            timer - start timer''')
            continue
        if (action == "timer"): #timer
            timer()
            continue
        else:
            print("Unknown command")
    elif (lockstatus == 1):
        lockpwd = str(input("Enter password to access the system. (Default pwd: user) "))
        if (lockpwd == pwd):
            lockstatus = 0
            print("Unlocked!")
            continue
        else:
            print("Wrong pwd. Try again.")
            continue
    else:
        print("Unknown error occurred")