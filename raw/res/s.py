
# made with love by Aekansh Dixit (https://github.com/aekanshd/) 
# Please credit me in all your future updates, that's all - you're free to use this code commercially, too.
# (c) Aekansh Dixit, 2018 provided under The MIT License (https://opensource.org/licenses/MIT)


# This file displays the signup screen
from tkinter import *
import f

# This function is used to check if this module was imported correctly or not.
def works():
    return True


def showWindow():
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them.
    global roots
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Password Keeper') # This renames the title of said window to 'signup'
    roots.geometry('500x200')
    instruction = Label(roots, text='Please Enter New Credentials\n',font="Helvetica 20 bold") # This puts a label, so just a piece of text saying 'please enter blah'
    instruction.grid(row=0, column=0, columnspan=3, sticky=E) # This just puts it in the window, on r ow 0, col 0. If you want to learn more look up a tkinter tutorial :)

    headingL = Label(roots, text='Welcome to the Password Keeper. We need you to enter a global password which will be asked each time you want to view stored passwords.\n',justify=LEFT,wraplength=300) # This just does the same as above, instead with the text new username.
    headingL.grid(row=1, column=0, columnspan=3, rowspan=3,sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    showSignature()

    pwordL = Label(roots, text='Global Password: ') # ""
    pwordL.grid(row=5, column=0, sticky=W) # ""
    # nameE = Entry(roots) # This now puts a text box waiting for input.
    # nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    pwordE.grid(row=5, column=1) # ^^
    signupButton = Button(roots, text='Continue', command=storeGlobalPwd) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
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
    signL = Label(roots,
                  text='                                                    This project was made by Aekansh Dixit (First Year Student of PES University, Bengaluru) for the Python Project Assignments of the first semester.')
    signL.grid(row=0, column=10, sticky=W)

