from pathlib import Path

# Function to display all files and folders in current directory
def readfileandfolder():
    path = Path('.')  # current directory
    items = list(path.rglob('*'))  # recursively get all files/folders
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


# CREATE FILE
def createfile():
    try:
        readfileandfolder()  # show existing files
        name = input("Enter file name to create: ")

        p = Path(name)

        # check if file already exists
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter content to write in file: ")
                fs.write(data)

            print("File created successfully.")
        else:
            print("File already exists.")

    except Exception as err:
        print(f"Error occurred: {err}")


# READ FILE
def readfile():
    try:
        readfileandfolder()
        name = input("Enter file name to read: ")

        p = Path(name)

        if p.exists():
            with open(p, "r") as fs:
                print("\nFile Content:\n")
                print(fs.read())
        else:
            print("File does not exist.")

    except Exception as err:
        print(f"Error occurred: {err}")


# UPDATE FILE (append new data)
def updatefile():
    try:
        readfileandfolder()
        name = input("Enter file name to update: ")

        p = Path(name)

        if p.exists():
            with open(p, "a") as fs:  # append mode
                data = input("Enter new content to add: ")
                fs.write("\n" + data)

            print("File updated successfully.")
        else:
            print("File does not exist.")

    except Exception as err:
        print(f"Error occurred: {err}")


# DELETE FILE
def deletefile():
    try:
        readfileandfolder()
        name = input("Enter file name to delete: ")

        p = Path(name)

        if p.exists():
            p.unlink()  # delete file
            print("File deleted successfully.")
        else:
            print("File does not exist.")

    except Exception as err:
        print(f"Error occurred: {err}")


# MENU
while True:
    print("\n====== FILE MANAGEMENT SYSTEM ======")
    print("Press 1 for Creating a file")
    print("Press 2 for Reading a file")
    print("Press 3 for Updating a file")
    print("Press 4 for Deleting a file")
    print("Press 5 for Exit")

    try:
        check = int(input("Enter your choice: "))

        if check == 1:
            createfile()

        elif check == 2:
            readfile()

        elif check == 3:
            updatefile()

        elif check == 4:
            deletefile()

        elif check == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select correct option.")

    except ValueError:
        print("Please enter a valid number.")