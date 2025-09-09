import sys
import csv

def addlostitem():
    lostItemlist = {
    }
    



def lostItemSearch():
    print("function called 2")



def showAllItems():
    print("function called 3")




def menu():
    print("What would you like to do:")
    print("1 Add lost items")
    print("2 Item search by keyword")
    print("3 Show all items")
    print("4 exit")
    choice = input("(choose a number)>>> ")
    if choice == "1":
        addlostitem()
    elif choice == "2":
        lostItemSearch()
    elif choice == "3":
        showAllItems()
    elif choice == "4":
        print("Thank you for using the service")
        sys.exit()
    else:
        print("invalid output")
        menu()


def greeting():
    print("=================================================================================")
    print("Welcome to the tfl lost item logger")
    print("=================================================================================")
    menu()

greeting()