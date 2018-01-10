
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
    f.write(str(datetime.datetime.now()) + " " + by + " " + str(thrown_error) + "\n")
    f.close()

# Log applications startups
def LogStartUp():
    f = open("bin/logs.txt", "a+")
    f.write("\n=============================================\n\nApplication Started at "+str(datetime.datetime.now())+ "\n\n")
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
            f.write(content + "\n")  # TODO: CHECK IF NEW LINE CHARACTER IS NEEDED OR NOT
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