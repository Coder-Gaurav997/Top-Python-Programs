# Importing the 'os' and the 'shutil' module
import os
import shutil

def create_file():  # Function to create new file
    try:
        path = input("\nEnter The Path For The File To Create : ")  # Get the path from the user
        with open(path, "w") as file:  # Create the file in write mode
            print(f"\n-- File '{path}' Has Been Created Successfully --")
    except FileNotFoundError:
        print("\n-- Path Not Found --")  # Handle the FileNotFoundError exception

def create_folder():
    try:
        path = input("\nEnter The Path For The Folder To Create : ")  # Get the path from the user
        os.mkdir(path)  # Create the folder
        print(f"\n-- Folder '{path}' Has Been Created Successfully --")
    except FileNotFoundError:
        print("\n-- Path Not Found --")  # Handle the FileNotFoundError exception

def delete_file():  # Function to delete a file
    path = input("\nEnter The Path Of The File To Delete : ")  # Get the path from the user
    if os.path.exists(path):  # Check if the file exists
        os.remove(path)  # Delete the file
        print(f"\n-- File '{path}' Has Been Deleted Successfully --")
    else:
        print(f"\n-- Error! No File Named '{path}' Founded --")  # Handle the case when the file does not exist

def delete_folder():
    path = input("\nEnter The Path Of The Folder To Delete : ")  # Get the path from the user
    if os.path.exists(path):  # Check if the folder exists
        os.rmdir(path)  # Delete the folder
        print(f"\n-- Folder '{path}' Has Been Deleted Successfully --")
    else:
        print(f"\n-- Error! No Folder Named '{path}' Founded --")  # Handle the case when the folder does not exist

def rename():  # Function to rename a file
    old_path = input("\nEnter The Old Path Of The File To Rename : ")  # Get the old path from the user
    new_path = input("Enter The New Path For The File : ")  # Get the new path from the user
    if os.path.exists(old_path):  # Check if the old path exists
        os.renames(old_path, new_path)  # Rename the file
        print(f"\n-- File '{old_path}' Has Been Successfully Renamed To '{new_path}' --")
    else:
        print("\n-- Error! Unreachable Path Given --")  # Handle the case when the old path does not exist

def copy():
    src_path = input("\nEnter The Source Path Of The File To Copy : ")  # Get the source path from the user
    dst_path = input("Enter The Destination Path Of The File : ")  # Get the destination path from the user
    if os.path.exists(src_path) and os.path.exists(dst_path):  # Check if both paths exist
        shutil.copy(src_path, dst_path)  # Copy the file
        print(f"\n-- File '{src_path}' Has Been Successfully Copied To '{dst_path}' --")
    else:
        print("\n-- Error! Unreachable Path Given --")  # Handle the case when either path does not exist

def move():
    src_path = input("\nEnter The Source Path Of The File To Move : ")  # Get the source path from the user
    dst_path = input("Enter The Destination Path Of The File : ")  # Get the destination path from the user
    if os.path.exists(src_path) and os.path.exists(dst_path):  # Check if both paths exist
        shutil.move(src_path, dst_path)  # Move the file
        print(f"\n-- File '{src_path}' Has Been Successfully Moved To '{dst_path}' --")
    else:
        print("\n-- Error! Unreachable Path Given --")  # Handle the case when either path does not exist

def open_file():  # Function to open and read data of a file
    path = input("\nEnter The Path Of The File To Open : ")  # Get the path from the user
    if os.path.exists(path):  # Check if the file exists
        os.startfile(path)  # Open the file
    else:
        print(f"\n-- Error! No File Named '{path}' Found --")  # Handle the case when the file does not exist

def list():
    path = input("\nEnter The Path Of The Folder : ")  # Get the path from the user
    if os.path.exists(path):  # Check if the folder exists
        list = os.listdir(path)  # Get the list of files and folders in the directory
        print(f"\n{list}")
        count = len(list)
        print(f"\n-- {count} Files And Folders Are Founded In '{path}' --")
    else:
        print(f"\n-- Error! Unreachable Path Given --")  # Handle the case when the folder does not exist

def check_existance():  # Function to checks that whether the file exists or not
    path = input("\nEnter The Path Of The File To Check Its Existance : ")  # Get the path from the user
    if os.path.exists(path):  # Check if the file exists
        print("\n-- File Exists --")
    else:
        print("\n-- File Does Not Exists --")  # Handle the case when the file does not exist

def exit_file_manager():  # Function to exit the file manager
    print("\n-- Exitting File Manager --\n")
    exit()  # Exit the program

menu_options = {
    1: create_file,
    2: create_folder,
    3: delete_file,
    4: delete_folder,
    5: rename,
    6: copy,
    7: move,
    8: open_file,
    9: list,
    10: check_existance,
    11: exit_file_manager
    }

print("\nWELCOME TO FILE MANAGER")
print("-----------------------")

print("1. Create A New File")
print("2. Create A New Folder")
print("3. Delete A File")
print("4. Delete A Folder")
print("5. Rename A File Or A Folder")
print("6. Copy A File Or A Folder")
print("7. Move A File Or A Folder")
print("8. Open A File")
print("9. List All Files And Folders In A Directory")
print("10. Check File's Existance")
print("11. Exit File Manager")

def main():
    while True:
        try: 
            user_choice = int(input("\nYour Choice : "))  # Get the user's choice
        except ValueError:
            print("\n-- ERROR! ENTER A VALID CHOICE --")  # Handle the ValueError exception
            continue

        if user_choice in menu_options:
            menu_options[user_choice]()  # Call the corresponding function
        else:
            print("\n-- ERROR! ENTER A VALID CHOICE --")  # Handle the case when the user enters an invalid choice

if __name__ == "__main__":
    main()  # Call the main function

# Author: GAURAV PANDEY