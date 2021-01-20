
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
