import os
from pathlib import Path

#Create path object with a folder destination
folder = Path("C:/Users/garri/OneDrive/Desktop/python programs")  
#Iterate through folder contents
for item in folder.iterdir():                           
    print(item)

#Check if  item is file or folder
for item in folder.iterdir():                             
    if item.is_file():                                       
        print("FILE: ", item.name)
    elif item.is_dir():
        print("FOLDER: ", item.name)

#Create an empty folder
folder.mkdir(exist_ok = True)  #Prevents creation if it already exists

#Delete folder (only if empty)
folder.rmdir()

#Getting filenames
file = folder / "Wordle.exe"
print(file.name)    #Wordle.exe
print(file.stem)    #Wordle
print(file.suffix)  # .exe


