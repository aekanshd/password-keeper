
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
