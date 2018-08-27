# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)

import os, errno


# Function to write a file at a given path
def WriteFileInPath(content, path):
    try:
        with open(path, "w+") as f:
            f.write(content)  # TODO: CHECK IF NEW LINE CHARACTER IS NEEDED OR NOT
            f.close()
            return "Created " + path
    except IOError as e:
        print(e)
        return False


# This function creates given folders.
def installFolder(folder):
    try:
        os.makedirs(folder)
        print("Created directory", folder)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


main = '''
# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This is the main file for the Password Keeper Program.

# Import main modules
import sys

sys.path.insert(0, 'res')
sys.path.insert(0, 'bin')

# Import app modules
import f


#Log the startup
f.LogStartUp()

# Check if the modules work or not.
print("Application started. This project was made by Aekansh Dixit (First Year Student of PES University, Bengaluru) for the Python Project Assignments of the first semester.")

# 0n the launch, we will check if the application was already launched or not by viewing our data fileset.
# TODO: Install the res folder along with the files, and empty bin folder

if(not f.checkFileExists("bin/gp.txt")):
    f.Log("This is the first launch.","mainFile")
    import s
    s.showWindow()
else:
    f.Log("Data found","mainFile")
    import m
    m.showWindow()
'''
al = '''

# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This file stores the algorithm to encrypt account passwords.
import random
import f

# Function to encrypt the password
def encrypt(pwd):
    pwdls=list(pwd)
    pwd = ""
    al = ""
    l = ""
    for i in range(0,len(pwdls)):
        diff=int(random.randrange(0,10))
        pwd+=str(ord(pwdls[i])+diff)
        al+=str(diff)
        l+=str(len(str(ord(pwdls[i])+diff)))
    f.Log("Encrypt password request.","encrypt[al]")
    return pwd+"x"+al+"x"+l


# Function to decrypt the password
def decrypt(pwd):
    code=pwd.split("x")
    a = 0 # Start of split
    b = 0 # End of Split
    c = list(code[2]) # Split by how much?
    d = list(code[1]) # Subtract by how much?
    pwd_chars=[]
    for i in c:
        letter=code[0][a:a+int(c[b])]
        pwd_chars.append(letter)
        a=a+int(c[b])
        b += 1

    pwd=""
    for i in range(0,len(pwd_chars)):
        pwd+=chr(int(pwd_chars[i])-int(d[i]))

    f.Log("Decrypt password request.","decrypt[al]")
    return pwd'''
ap = '''
# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This file stores the algorithm to encrypt the global password.
import random
import f
import json


# This function is used to check if this module was imported correctly or not.
def works():
    return True


# This function will generate a random salt and store it somewhere safe.
def genSalt():
    diff = int(random.randrange(0, 10))
    opps = ["+", "-"]
    secure_random = random.SystemRandom()
    opp = secure_random.choice(opps)
    final = str(diff) + opp
    saltfile = open("res/s.txt", "w+")
    saltfile.write(final)
    saltfile.close()
    f.Log("Salt created", "genSalt")


# Read the salt from a secured file.
def readSalt():
    global difference
    global operator
    try:
        with open("res/s.txt", "r", encoding='utf-8') as saltfile:
            contents = saltfile.read()
            operator = contents.strip()[-1]
            difference = int(contents[:-1])
            saltfile.close()
            return True
    except IOError as e:
        f.Log(e, "readSalt")
        return False


# Encrypt the given content
def encrypt(content):
    ls = list(content)
    content = ""
    readSalt()
    if (operator == "+"):
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) + difference)
    elif (operator == "-"):
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) - difference)
    return content

# Decrypt the given content
def decrypt(content):
    ls = list(content)
    content = ""
    readSalt()
    if operator == "+":
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) - difference)
    elif operator == "-":
        for i in range(0, len(ls)):
            content += chr(ord(ls[i]) + difference)
    return content


# This function store the encrypted password in a safe file.
def storeGlobal(pwd):
    saltfile = open("bin/gp.txt", "w+", encoding='utf-8')
    dict1 = {"p": pwd}
    contents = json.dumps(dict1)
    saltfile.write(encrypt(str(contents)))
    saltfile.close()
    f.Log("GPwd stored", "storeGlobal")


# This function matches the password
def checkPassword(pwd):
    try:
        with open("bin/gp.txt", "r", encoding='utf-8') as gpfile:
            contents = decrypt(gpfile.read())
            data = f.JSONtoDict(contents)
            if encrypt(pwd) == data["p"]:
                return True
            else:
                f.Log("Bad Global", "checkPassword")
                return False
    except IOError as e:
        f.Log(e, "checkPassword")
        return False
'''
d = '''
# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This file is used to access the data - read and write
import f
import ap
import al

data_path = "bin/d.txt"

# This function is used to check if this module was imported correctly or not.
def works():
    return True


# This function counts the number of accouts
def countAccounts():
    try:
        with open(data_path, "r", encoding='utf-8') as datafile:
            contents = datafile.read()
            if contents == "":
                f.Log("No accounts found on startup", "countAccounts")
                datafile.close()
                return 0
            else:
                contents = f.JSONtoDict(ap.decrypt(contents))
                count=len(contents)
                f.Log("Found "+str(count)+" account(s) on startup","countAccounts")
                datafile.close()
                return count
    except IOError as e:
        f.Log(e, "moreThanOne")
        return -1


# This function reads the data from the file
# Returns dict
def readData():
    try:
        with open(data_path, "r", encoding='utf-8') as datafile:
            contents = datafile.read()
            if contents != "":
                contents = f.JSONtoDict(ap.decrypt(contents))
            datafile.close()
            return contents

    except IOError as e:
        f.Log(e, "readData")
        return "error"


# This function writes the data to the file
# Returns bool
def writeData(contents):
    try:
        with open(data_path, "w+", encoding='utf-8') as file:
            file.write(ap.encrypt(str(contents)))
            file.close()
            return True

    except IOError as e:
        f.Log(e, "writeData")
        return False


# This function adds new data
# Returns True/False
def addEntry(name,uname,pwd):
    accounts = readData()
    pwd = al.encrypt(pwd)
    entry = {"n":name,"u":uname,"p":pwd}
    if accounts == "error":
        return False
    else:
        if accounts == "":
            writeData(f.DICTtoJSON({countAccounts() + 1: entry}))
        else:
            accounts.update({str(countAccounts() + 1): entry})
            writeData(f.DICTtoJSON(accounts))
        f.Log("New account added: "+name,"addEntry")
        return True


def deleteAccount(id):
    accounts = readData()
    if accounts == "error":
        return False
    else:
        if accounts == "":
            f.Log("No account(s) to delete.", "deleteAccount")
            return False
        else:
            accounts.pop(id,None)
            writeData(f.DICTtoJSON(accounts))
        f.Log("Account deleted: " + id, "deleteAccount")
        return True
'''
f = '''
# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This file contains all the function definitions required for the main modules to work.
# from pathlib import Path - Old age method, not needed.
import os
import datetime
import json
import tkinter


# This function is used to check if this module was imported correctly or not.
def works():
    return True


# Log errors and everything that helps us troubleshoot!
def Log(thrown_error, by):
    f = open("bin/logs.txt", "a+")
    f.write(str(datetime.datetime.now()) + " " + by + " " + str(thrown_error) + "\\n")
    f.close()

# Log applications startups
def LogStartUp():
    f = open("bin/logs.txt", "a+")
    f.write("\\\n=============================================\\\n\\\nApplication Started at "+str(datetime.datetime.now())+ "\\\n\\\n")
    f.close()


# Boolean function to check if data file exists or not
def checkFileExists(path):
    # if(Path(path).is_file()):
    if os.path.isfile(path):
        return True
    else:
        return False


# Function to write a file at a given path
def WriteFileInPath(content, path):
    try:
        with open(path, "a+") as f:
            f.write(content + "\\n")  # TODO: CHECK IF NEW LINE CHARACTER IS NEEDED OR NOT
            f.close()
            return True
    except IOError as e:
        Log(e, "WriteFileInPath")
        return False

# Function to delete a file at a given path
def DeleteFilelnPath(path):
    if checkFileExists(path):
        os.remove(path)
        return True
    else:
        Log(path + " does not exist", "DeleteFileInPath")
        return False


# Function to convert a JSON to a dict
# Returns a dictionary.
def JSONtoDict(content):
    return json.loads(content)


# Function to convert a dict to a JSON
# Returns a JSON String.
def DICTtoJSON(content):
    return json.dumps(content)


# This function creates creates given folders.
def installFolders(folders):
    for folder in folders:
        os.mkdirs(folder)
        Log("Created folder " + folder, "install")


def createDataFile():
    try:
        with open("bin/d.txt", "a+") as file:
            file.close()
            return True
    except IOError as e:
        Log(e, "createDataFile")
        return False
'''
m = '''

# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This file displays the main screen of the app
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox
from tkinter import simpledialog
import f
import d
import ap
import al



# This function is used to check if this module was imported correctly or not.
def works():
    return True


unlocked = False  # To check if this session is unlocked or not, by default it is not (False)


# This function displays the main screen.
def showWindow():
    global pwordE  # These globals just make the variables global to the entire script, meaning any definition can use them.
    global roots

    roots = Tk()  # This creates the window, just a blank one.
    roots.title('Password Keeper')  # This renames the title of said window to 'signup'
    window_height = "175" if d.countAccounts() == -1 else str(175 + (d.countAccounts() * 35))
    roots.geometry('580x'+window_height)
    roots.resizable(0,0)

    """Contributionds by Prince Kelvin Onyenanu,
    to the Password Keeper App"""
    menubar = tk.Menu(roots)
    roots.config(menu=menubar)

    settingsMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=settingsMenu)
    settingsMenu.add_command(label="About", command=about)
    settingsMenu.add_separator()
    settingsMenu.add_command(label="Exit", command=exitWindow)


    # Row 1
    # Title
    title = Label(roots, text='Password Keeper', font="Helvetica 20 bold")
    title.grid(row=0, column=0, columnspan=3, sticky=W)


    # Row 2 is reserved for unlocked session notice.
    if not unlocked:
        gapL = Label(roots, text='\\n', fg="red")
        gapL.grid(row=2, column=0, sticky=W, columnspan=3)
    else:
        unlockedL = Label(roots, text='Session Unlocked: Information is not secure.\\n', fg="red")
        unlockedL.grid(row=2, column=0, sticky=W, columnspan=3)
    # Row 3
    availActionsL = Label(roots, text='Available Actions:')
    availActionsL.grid(row=3, column=0, sticky=W)

    refreshBtn = Button(roots, text='Refresh', command=refreshWindow)
    refreshBtn.grid(row=3, column=1, sticky=E, padx=5)
    # Main Buttons - Delete All, Add Entry
    if d.countAccounts() > 0:
        deleteAllBtn = Button(roots, text='Delete All', fg='red', command=confirmDeleteAll)
        deleteAllBtn.grid(row=3, column=2, sticky=E, padx=5)
        addEntryBtn = Button(roots, text='Add Entry', command=addEntry)
        addEntryBtn.grid(row=3, column=4, sticky=E, padx=5)
    else:
        addEntryBtn = Button(roots, text='Add Entry', command=addEntry)
        addEntryBtn.grid(row=3, column=2, sticky=E, padx=45)
    if unlocked:
        lockBtn = Button(roots, text='Lock Session', command=lockSession)
        lockBtn.grid(row=3, column=3, sticky=E, padx=5)
    else:
        unlockBtn = Button(roots, text='Unlock Session', command=unlockSession)
        unlockBtn.grid(row=3, column=3, sticky=E, padx=5)

    myaccL = Label(roots, text='\\nMy Accounts', font="Helvetica 12 bold")
    myaccL.grid(row=4, column=0, sticky=W, columnspan=3)

    # Row 3
    if d.countAccounts() == 0:
        nodataL = Label(roots, text='\\nNo accounts found. Click on Add Entry above to add a new account.')
        nodataL.grid(row=5, column=0, sticky=W, columnspan=3)
    elif d.countAccounts() == -1:
        errorL = Label(roots, text='\\nThere was an error fetching the data.',fg="red")
        errorL.grid(row=5, column=0, sticky=W, columnspan=3)
    else:
        displayAccounts()

    # Row 4
    # accL = Label(roots, text='\\n\\nGoogle Account')
    # accL.grid(row=3, column=0, sticky=W, columnspan=2)
    # viewDetailsBtn = Button(roots, text='View Details', command=storeGlobalPwd)
    # viewDetailsBtn.grid(row=3, column=2, sticky=SW)
    # Label(roots, text='\\n\\nMicrosoft Account').grid(row=4, column=0, sticky=W, columnspan=2)
    # Button(roots, text='View Details', command=storeGlobalPwd).grid(row=4, column=2, sticky=SW)


    roots.mainloop()  # This just makes the window keep open, we will destroy it soon

    # nameE.get()


# This function stores the global password
# TODO: delete this function because it's not needed in this file.
def storeGlobalPwd():
    import ap
    import m
    ap.genSalt()
    pwd = ap.encrypt(pwordE.get())  # encrypt the given password
    ap.storeGlobal(pwd)
    f.createDataFile()
    roots.destroy()  # This will destroy the signup window. :)
    m.showWindow()


# This function destroys the window, and reopens it to refresh the data.
def refreshWindow():
    f.Log("Window has been refreshed.", "refreshWindow")
    roots.destroy()
    showWindow()


# This function opens the Add New Entry window.
def addEntry():
    global entryWindow
    global nameE
    global unameE
    global passE
    global gapL
    entryWindow = Tk()
    entryWindow.title('New Account')
    entryWindow.geometry('350x250')
    entryWindow.resizable(0,0)
    title = Label(entryWindow, text='Enter New Account Details\\n', font="Helvetica 15 bold")
    title.grid(row=0, column=0, columnspan=3, sticky=W)
    nameL = Label(entryWindow, text='Account Name: ')
    nameL.grid(row=1, column=0, sticky=W)
    nameE = Entry(entryWindow)
    nameE.grid(row=1, column=1)
    unameL = Label(entryWindow, text='Username: ')
    unameL.grid(row=2, column=0, sticky=W)
    unameE = Entry(entryWindow)
    unameE.grid(row=2, column=1)
    passL = Label(entryWindow, text='Password: ')
    passL.grid(row=3, column=0, sticky=W)
    passE = Entry(entryWindow, show='*')
    passE.grid(row=3, column=1)
    gapL = Label(entryWindow, text='\\n')
    gapL.grid(row=4, column=0, columnspan=2, sticky=W)
    entryBtn = Button(entryWindow, text='Add New Account', fg='green', command=addEntryHandler)
    entryBtn.grid(row=5, column=1, columnspan=2, sticky=E)


# This function is used to check if all the fields are checked or not
def addEntryHandler():
    name = nameE.get()
    uname = unameE.get()
    pwd = passE.get()
    if name == "" or uname == "" or pwd == "":
        gapL.config(text='\\nPlease enter all the fields.\\n', fg='red')
    else:
        if d.addEntry(name, uname, pwd):
            gapL.config(text='\\nSuccess!\\n', fg='green')
            entryWindow.destroy()
            refreshWindow()
        else:
            gapL.config(text='\\nThere was an error.\\n', fg='red')


# This function populates the list in the main screen.
def displayAccounts():

    accounts = d.readData()
    row = 6
    for key, value in accounts.items():
        account = value
        Label(roots, text=account["n"], font="sans-serif 10 bold").grid(row=row, column=0, sticky=W, pady=5)
        Button(roots, text='View Details', fg='green', command=lambda key=key: viewDetails(key)).grid(row=row, column=2, sticky=E,padx=10)
        if not unlocked:
            deleteBtn = Button(roots, text='Delete Account', command=lambda key=key: deleteEntryHandler(key))
            deleteBtn.grid(row=row, column=3, padx=10, sticky=E)
        else:
          deleteBtn = Button(roots, text='Delete Account', command=lambda key=key: deleteEntryHandler(key))
          deleteBtn.grid(row=row, column=3, padx=10, sticky=E)  

        row += 1


# This function opens the View Details window.
def viewDetails(id):
    global detailsWindow
    global decryptPwdT
    global decryptPwdE
    global decryptPwdBtn
    global detailsGapL2
    global pwdTL

    data = d.readData()
    name = data[id]["n"]
    username = data[id]["u"]
    password = "********"

    detailsWindow = Tk()
    detailsWindow.title('Account Details')
    detailsWindow.geometry('450x260')
    detailsWindow.resizable(0,0)
    title = Label(detailsWindow, text=name + '\\n', font="Helvetica 15 bold")
    title.grid(row=0, column=0, columnspan=3, sticky=W)
    unameL = Label(detailsWindow, text='Username', font="sans-serif 10 bold")
    unameL.grid(row=1, column=0, sticky=W)
    unameTL = Label(detailsWindow, text=username)
    unameTL.grid(row=2, column=0, sticky=W)
    pwdL = Label(detailsWindow, text='Password', font="sans-serif 10 bold")
    pwdL.grid(row=1, column=1, sticky=W)
    pwdTL = Label(detailsWindow, text=password)
    pwdTL.grid(row=2, column=1, sticky=W)


    if not unlocked:
        detailsGapL = Label(detailsWindow, text='\\n', justify=LEFT)
        detailsGapL.grid(row=3, column=0, columnspan=4, sticky=W)
        decryptPwdT = Label(detailsWindow, text="Global Password: ", justify=LEFT)
        decryptPwdT.grid(row=4, column=0, sticky=W)
        decryptPwdE = Entry(detailsWindow, show='*')
        decryptPwdE.grid(row=4, column=1, columnspan=3, sticky=W)
        detailsGapL2 = Label(detailsWindow, text='\\nEnter global password to decrypt info.\\n', justify=LEFT)
        detailsGapL2.grid(row=5, column=0, columnspan=3, sticky=W)
        decryptPwdBtn = Button(detailsWindow, text='Decrypt Password', command=lambda key=data[id]["p"]: decryptHandler(key))
        decryptPwdBtn.grid(row=4, column=4, columnspan=4, sticky=E,padx=15)
    else:
        detailsGapL = Label(detailsWindow, text='\\n', justify=LEFT)
        detailsGapL.grid(row=3, column=0, columnspan=4, sticky=W)
        decryptPwdBtn = Button(detailsWindow, text='Decrypt Password', command=lambda key=data[id]["p"]: decryptHandler(key))
        decryptPwdBtn.grid(row=6, column=1, sticky=W)
        loginPwdBtn = Button(detailsWindow, text='Copy Password', command=lambda key=data[id]["p"]: copy_button(key))
        loginPwdBtn.grid(row=6, column=5, columnspan=4, sticky=E)
        detailsGapL2 = Label(detailsWindow, text='\\n\\n')
        detailsGapL2.grid(row=7, column=0, columnspan=2, sticky=W)



# This function confirms the deletion password
def decryptHandler(pwd):
    if not unlocked:
        gpwd = decryptPwdE.get()
        if gpwd != "":
            if ap.checkPassword(gpwd) == True:
                detailsGapL2.config(text='\\nPassword decrypted.\\nClose the window to encrypt it.\\n', fg='green')
                decryptPwdBtn.grid_remove()
                decryptPwdE.grid_remove()
                decryptPwdT.grid_remove()
                pwdTL.config(text=al.decrypt(pwd))
                loginPwdBtn = Button(detailsWindow, text='Copy Password', command=lambda key=pwd: copy_button(key))
                loginPwdBtn.grid(row=6, column=5, columnspan=4, sticky=E)
            else:
                detailsGapL2.config(text='\\nIncorrect global password.\\n', fg='red')
        else:
            detailsGapL2.config(text='\\nPlease enter your global password.\\n', fg='red')
    else:
        detailsGapL2.config(text='\\nPassword decrypted.\\nClose the window to encrypt it.\\n', fg='green')
        pwdTL.config(text=al.decrypt(pwd))
        decryptPwdBtn.grid_remove()

# This fucntion adds our signature
def showSignature():
    text='This project was made by Aekansh Dixit (First Year Student of PES University, Bengaluru) for the Python Project Assignments of the first semester.'
    return text


# This function confirms the deletion of an account by prompts.
def deleteEntryHandler(id):
    if not unlocked:
        pwd = simpledialog.askstring("Delete Account?",
                                     "Enter your global password to confirm deletion of this account.\\n\\nWarning: This can not be undone.",
                                     show='*')
        if pwd is not None:
            if ap.checkPassword(pwd) == True:
                deleteAccount(id)
            else:
                messagebox.showerror("Error", "Wrong Password. (or error)")
    else:
        confirm = messagebox.askokcancel("Delete Account?",
                                         "Do you want to delete this account?\\n\\nWarning: This can not be undone.")
        if confirm:
            deleteAccount(id)


# Function to directly copy password
def copy_button(pwd):
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(al.decrypt(pwd))
    clip.destroy()


# This function deletes an account.
def deleteAccount(id):
    if d.deleteAccount(id):
        refreshWindow()
    else:
        messagebox.showerror("Error", "Oops! Something went wrong.")


# This function confirms the deletion of all accounts by prompts.
def confirmDeleteAll():
    if not unlocked:
        pwd = simpledialog.askstring("Delete All?",
                                     "Enter your global password to confirm deletion of all accounts.\\n\\nWarning: This can not be undone.",
                                     show='*')
        if pwd is not None:
            if ap.checkPassword(pwd) == True:
                deleteAll()
            else:
                messagebox.showerror("Error", "Wrong Password. (or error)")
    else:
        confirm = messagebox.askokcancel("Delete Account?",
                                         "Do you want to delete all accounts?\\n\\nWarning: This can not be undone.")
        if confirm:
            deleteAll()


# This function deletes all the accounts.
def deleteAll():
    if d.writeData(""):
        f.Log("Deleted all accounts.", "deleteAll")
        refreshWindow()
    else:
        f.Log("Could not delete all accounts. Must've logged it above.", "deleteAll")


# This function unlocks the session.
def unlockSession():
    global unlocked
    pwd = simpledialog.askstring("Unlock Session",
                                 "If you unlock this session, you will not be asked to enter a password\\neach time you want to decrypt or delete an account's information.\\nUse when safe.\\n\\nEnter your global password to continue.",
                                 show='*')
    if pwd is not None:
        if ap.checkPassword(pwd) == True:
            unlocked = True
            f.Log("This session has been unlocked.", "unlockSession")
            refreshWindow()
        else:
            f.Log("This session couldn't unlocked.", "unlockSession")
            messagebox.showerror("Error", "Wrong Password. (or error)")


# This function locks the session.
def lockSession():
    global unlocked
    unlocked = False
    f.Log("This session has been locked.", "lockSession")
    refreshWindow()

# This function displays the about
def about(*event):
    global aboutWindow

    aboutWindow = Tk()
    aboutWindow.title("About the developers")
    aboutWindow.geometry("528x297")
    aboutWindow.resizable(0, 0)

    aboutText = showSignature()

    paper = st.ScrolledText(aboutWindow, width=350, height=200, font=("Consolas", 11))
    paper.insert("1.0", aboutText)
    paper.configure(state='disabled')
    paper.pack()

    aboutWindow.mainloop()

#This function destroys the main window
def exitWindow(*event):
    roots.destroy()
'''
s = '''
# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This file displays the signup screen
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext as st
import f
import m

# This function is used to check if this module was imported correctly or not.
def works():
    return True


def showWindow():
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them.
    global roots
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Password Keeper') # This renames the title of said window to 'signup'
    roots.geometry('500x200')
    roots.resizable(0,0)

    #this creates a menu
    menubar = tk.Menu(roots)
    roots.config(menu=menubar)

    settingsMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=settingsMenu)
    settingsMenu.add_command(label="About", command=about)
    settingsMenu.add_separator()
    settingsMenu.add_command(label="Exit", command=exitWindow)

    instruction = Label(roots, text='Please Enter New Credentials',  font="Helvetica 20 bold") # This puts a label, so just a piece of text saying 'please enter blah5
    instruction.grid(row=0, column=0, columnspan=3, sticky=E) # This just puts it in the window, on r ow 0, col 0. If you want to learn more look up a tkinter tutorial :)

    headingL = Label(roots, text='\\nWelcome to the Password Keeper. We need you to enter a global password which will be asked each time you want to view stored passwords.\\n',justify='left',wraplength=300) # This just does the same as above, instead with the text new username.
    headingL.grid(row=1, column=0, columnspan=3, rowspan=3,sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    showSignature()

    pwordL = Label(roots, text='Global Password: ') # ""
    pwordL.grid(row=5, column=0, sticky=W) # ""
    # nameE = Entry(roots) # This now puts a text box waiting for input.
    # nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    pwordE.grid(row=5, column=1) # ^^
    signupButton = Button(roots, text='Continue', fg="green", command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(row=5,column=3, sticky=W)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon

    #nameE.get()

def storeGlobalPwd():
    import ap
    import m
    ap.genSalt()
    pwd = ap.encrypt(pwordE.get()) # encrypt the given password
    ap.storeGlobal(pwd)
    f.createDataFile()
    roots.destroy() # This will destroy the signup window. :)
    m.showWindow()

# This fucntion adds our signature
def showSignature():
    text = 'This project was made by Aekansh Dixit (First Year Student of PES University, Bengaluru) for the Python Project Assignments of the first semester.'
    return text

# This function displays the about
def about(*event):
    global aboutWindow

    aboutWindow = Tk()
    aboutWindow.title("About the developers")
    aboutWindow.geometry("528x297")
    aboutWindow.resizable(0, 0)

    aboutText = showSignature()

    paper = st.ScrolledText(aboutWindow, width=350, height=200, font=("Consolas", 11))
    paper.insert("1.0", aboutText)
    paper.configure(state='disabled')
    paper.pack()

    aboutWindow.mainloop()

#This function destroys the main window
def exitWindow(*event):
    roots.destroy()
'''

# Start installing the files
print(
    "This project was made by Aekansh Dixit (First Year Student of PES University, Bengaluru) for the Python Project Assignments of the first semester.")
print("Creating directories...")
installFolder("Password Keeper")
installFolder("Password Keeper/bin")
installFolder("Password Keeper/res")
print("Creating main file...")
print(WriteFileInPath(main, "Password Keeper/main.py"))
print("Creating other files...")
print(WriteFileInPath(al, "Password Keeper/res/al.py"))
print(WriteFileInPath(ap, "Password Keeper/res/ap.py"))
print(WriteFileInPath(d, "Password Keeper/res/d.py"))
print(WriteFileInPath(f, "Password Keeper/res/f.py"))
print(WriteFileInPath(m, "Password Keeper/res/m.py"))
print(WriteFileInPath(s, "Password Keeper/res/s.py"))
print("Installation finished.")
