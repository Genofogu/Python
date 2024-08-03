#Write a python program to rename a file name to "rename_file"

import os    
oldname = input("Upload your file for renaming:")
newname = input("Write a new name of your file:")

with open(oldname,"r") as renaming:
    a = renaming.read()
with open(newname,"w") as renaming:
    renaming.write(a)
    
os.remove(oldname)                   #for deleting the file

