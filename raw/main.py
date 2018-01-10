
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
