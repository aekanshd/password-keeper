
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
    return pwd