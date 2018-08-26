
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
        gapL = Label(roots, text='\n', fg="red")
        gapL.grid(row=2, column=0, sticky=W, columnspan=3)
    else:
        unlockedL = Label(roots, text='Session Unlocked: Information is not secure.\n', fg="red")
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

    myaccL = Label(roots, text='\nMy Accounts', font="Helvetica 12 bold")
    myaccL.grid(row=4, column=0, sticky=W, columnspan=3)

    # Row 3
    if d.countAccounts() == 0:
        nodataL = Label(roots, text='\nNo accounts found. Click on Add Entry above to add a new account.')
        nodataL.grid(row=5, column=0, sticky=W, columnspan=3)
    elif d.countAccounts() == -1:
        errorL = Label(roots, text='\nThere was an error fetching the data.',fg="red")
        errorL.grid(row=5, column=0, sticky=W, columnspan=3)
    else:
        displayAccounts()

    # Row 4
    # accL = Label(roots, text='\n\nGoogle Account')
    # accL.grid(row=3, column=0, sticky=W, columnspan=2)
    # viewDetailsBtn = Button(roots, text='View Details', command=storeGlobalPwd)
    # viewDetailsBtn.grid(row=3, column=2, sticky=SW)
    # Label(roots, text='\n\nMicrosoft Account').grid(row=4, column=0, sticky=W, columnspan=2)
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
    title = Label(entryWindow, text='Enter New Account Details\n', font="Helvetica 15 bold")
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
    gapL = Label(entryWindow, text='\n')
    gapL.grid(row=4, column=0, columnspan=2, sticky=W)
    entryBtn = Button(entryWindow, text='Add New Account', fg='green', command=addEntryHandler)
    entryBtn.grid(row=5, column=1, columnspan=2, sticky=E)


# This function is used to check if all the fields are checked or not
def addEntryHandler():
    name = nameE.get()
    uname = unameE.get()
    pwd = passE.get()
    if name == "" or uname == "" or pwd == "":
        gapL.config(text='\nPlease enter all the fields.\n', fg='red')
    else:
        if d.addEntry(name, uname, pwd):
            gapL.config(text='\nSuccess!\n', fg='green')
            entryWindow.destroy()
            refreshWindow()
        else:
            gapL.config(text='\nThere was an error.\n', fg='red')


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
          deleteBtn = Button(roots, text='Delete Account', command=lambda key=key: deleteAccount(key))
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
    title = Label(detailsWindow, text=name + '\n', font="Helvetica 15 bold")
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
        detailsGapL = Label(detailsWindow, text='\n', justify=LEFT)
        detailsGapL.grid(row=3, column=0, columnspan=4, sticky=W)
        decryptPwdT = Label(detailsWindow, text="Global Password: ", justify=LEFT)
        decryptPwdT.grid(row=4, column=0, sticky=W)
        decryptPwdE = Entry(detailsWindow, show='*')
        decryptPwdE.grid(row=4, column=1, columnspan=3, sticky=W)
        detailsGapL2 = Label(detailsWindow, text='\nEnter global password to decrypt info.\n', justify=LEFT)
        detailsGapL2.grid(row=5, column=0, columnspan=3, sticky=W)
        decryptPwdBtn = Button(detailsWindow, text='Decrypt Password', command=lambda key=data[id]["p"]: decryptHandler(key))
        decryptPwdBtn.grid(row=4, column=4, columnspan=4, sticky=E,padx=15)
    else:
        detailsGapL = Label(detailsWindow, text='\n', justify=LEFT)
        detailsGapL.grid(row=3, column=0, columnspan=4, sticky=W)
        decryptPwdBtn = Button(detailsWindow, text='Decrypt Password', command=lambda key=data[id]["p"]: decryptHandler(key))
        decryptPwdBtn.grid(row=6, column=1, sticky=W)
        loginPwdBtn = Button(detailsWindow, text='Copy Password', command=lambda key=data[id]["p"]: copy_button(key))
        loginPwdBtn.grid(row=6, column=5, columnspan=4, sticky=E)
        detailsGapL2 = Label(detailsWindow, text='\n\n')
        detailsGapL2.grid(row=7, column=0, columnspan=2, sticky=W)
        


# This function confirms the deletion password
def decryptHandler(pwd):
    if not unlocked:
        gpwd = decryptPwdE.get()
        if gpwd != "":
            if ap.checkPassword(gpwd) == True:
                detailsGapL2.config(text='\nPassword decrypted.\nClose the window to encrypt it.\n', fg='green')
                decryptPwdBtn.grid_remove()
                decryptPwdE.grid_remove()
                decryptPwdT.grid_remove()
                pwdTL.config(text=al.decrypt(pwd))
                loginPwdBtn = Button(detailsWindow, text='Copy Password', command=lambda key=pwd: copy_button(key))
                loginPwdBtn.grid(row=6, column=5, columnspan=4, sticky=E)
            else:
                detailsGapL2.config(text='\nIncorrect global password.\n', fg='red')
        else:
            detailsGapL2.config(text='\nPlease enter your global password.\n', fg='red')
    else:
        detailsGapL2.config(text='\nPassword decrypted.\nClose the window to encrypt it.\n', fg='green')
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
                                     "Enter your global password to confirm deletion of this account.\n\nWarning: This can not be undone.",
                                     show='*')
        if pwd is not None:
            if ap.checkPassword(pwd) == True:
                deleteAccount(id)
            else:
                messagebox.showerror("Error", "Wrong Password. (or error)")
    else:
        confirm = messagebox.askokcancel("Delete Account?",
                                         "Do you want to delete this account?\n\nWarning: This can not be undone.")
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
                                     "Enter your global password to confirm deletion of all accounts.\n\nWarning: This can not be undone.",
                                     show='*')
        if pwd is not None:
            if ap.checkPassword(pwd) == True:
                deleteAll()
            else:
                messagebox.showerror("Error", "Wrong Password. (or error)")
    else:
        confirm = messagebox.askokcancel("Delete Account?",
                                         "Do you want to delete all accounts?\n\nWarning: This can not be undone.")
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
                                 "If you unlock this session, you will not be asked to enter a password\neach time you want to decrypt or delete an account's information.\nUse when safe.\n\nEnter your global password to continue.",
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
