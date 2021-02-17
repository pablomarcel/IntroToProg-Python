# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Pablo Montijo,2.15.2021,Added code to complete assignment 5
# Pablo Montijo,2.16.2021,Added .strip() line 38
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
# objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {"Task": "", "Priority": ""}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
"""  # A menu of user options


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

objFile = open('ToDoList.txt', 'r')
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here

        print(f'{"Task":<20}' + f'{"Priority":>10}')

        objFile = open('ToDoList.txt', 'r')
        for row in objFile:
            lstRow = row.split(",")
            print(f'{lstRow[0]:<20}' + f'{lstRow[1].strip():>10}')
        objFile.close()

        continue
    # Step 4 - Add a new item to the list/Ta1ble
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here

        strTask = input('Enter a Task: ')
        strPriority = input('Enter a Priority: ')
        lstTable.append({"Task": strTask, "Priority": strPriority})

        continue
    # Step 5 - Remove an item from the list/Table based on its name
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here

        strTaskToRemove = input('Enter a Task to Remove: ')
        for row in lstTable:
            if row["Task"] == strTaskToRemove:
                lstTable.remove(row)
                print('row removed')

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here

        objFile = open('ToDoList.txt', 'w')

        for row in lstTable:
            objFile.write(row["Task"] + ',' + row["Priority"] + '\n')
        objFile.close()

        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
