# )0_0(#
# Title: Assignment07
# Desc: Script for user to enter birthdays demonstrating pickling and error handling (try/except)
# Change Log
# lredinger,191116,created file
# lredinger,191118, custom MenuOutOfRange exception
# lredinger,191119, updated birthday input, imported os, fixed pickle issue


import pickle  # adds ability to serialize data to .dat file
import os  # adds function to search for file, create and remove

# Data -------------------------------------------- #
strFileName = "birthdayList.dat"
bDayList = []
class MenuOutOfRange(Exception):
    pass
class MonthOutOfRange(Exception):
    pass
class DayOutOfRange(Exception):
    pass
strMenu = '''
==========User Menu===========
1. Add Birthday to list
2. Delete a Birthday
3. Show all Birthdays 
4. Save and Quit
===============================
'''

# Processing -------------------------------------- #
def save_birthdays_to_file(file_name, list_of_data):
    """add list data to binary (pickle) file
        :param = file name (objFile)
        :param = list of data (bDayList)
        :return = none"""
    print(bDayList)
    with open("birthdayList.dat", "ab") as objFile:
        pickle.dump(bDayList, objFile)
        print("\nBirthdays have been saved")


def read_birthdays_from_file(file_name):
    """Read birthdays from binary (pickle)
        :param = none
        :return = none"""
    with open("birthdayList.dat", "rb") as objFile:
        objFileData = pickle.load(objFile)
        objFile.close()
    print(objFileData)


def delete_birthday_from_list():
    """Deletes a birthday from list
    :param = none
    :return = none"""
    print(bDayList)
    nameDelete = input("Who's birthday do you want to delete? ")
    for birthday in bDayList:
        if nameDelete == birthday[0]:
            bDayList.remove(birthday)
            print(birthday[0] + " was removed.")  # prints the name of the person removed
            return  # stops the loop if name found
    print(nameDelete + " is not on the list.")
    return

# Presentation ------------------------------------ #
def addBirthdays():
    """Add birthdays to list
    :param none
    :return none"""
    strName = input("Enter a Name: ")
    try:
        bMonth = int(input("For " + strName + " Enter the month (MM): "))
        if bMonth not in range(1, 13):
            raise MonthOutOfRange  # Forces user to enter valid date
        bDay = int(input("For " + strName + " Enter the day (DD): "))
        if bDay not in range(1, 32):
            raise DayOutOfRange  # Forces user to enter valid date
        birthday = str(bMonth) + "/" + str(bDay)
        bDayObj = [strName, birthday]
        bDayList.append(bDayObj)
    except MonthOutOfRange:
        print("Please enter a valid numeric month")
        addBirthdays()
    except DayOutOfRange:
        print("Please enter a valid numeric day")
        addBirthdays()


# ------------------Main Script------------------- #
if os.path.exists("birthdayList.dat"):  # searches for existing file
    with open("birthdayList.dat", "rb") as objFile:  # opens file
        # bDayList.append("Birthdays to remember:")
        bDayList = pickle.load(objFile)  # loads any existing data into bDayList
    os.remove("birthdayList.dat")  # deletes the file (so each program session is latest/greatest)

print("This script will allow you to store Birthdays in a binary file and read them. \n"
      "Never forget your mom's birthday again!")
while True:
    try:
        print(strMenu)
        usrChoice = int(input("\nWhat would you like to do? "))
        if usrChoice not in range(1, 5):
            raise MenuOutOfRange  # user must choose int from menu options

        #  user choice 1 (Add birthday to list)
        if usrChoice == 1:
            addBirthdays()
            continue

        #  user choice 2 (Delete a Birthday)
        elif usrChoice == 2:
            delete_birthday_from_list()

        #  user choice 3 (Show all Birthdays)
        elif usrChoice == 3:
            print(bDayList)

        # user choice 4 (save data to file(pickle) and quit)
        elif usrChoice == 4:
            save_birthdays_to_file(strFileName, bDayList)
            break

    # Error Handling
    except ValueError as e:  # user entered str instead of int
        print("\n!!!ERROR!!!\nThat's not a valid menu option")
        print("Menu option cannot be text: ", e)
    except MenuOutOfRange:  # user entered int not matched to menu
        print("\n!!!ERROR!!!\nYour selection is out of range.\nPlease select a menu option between 1-4")
