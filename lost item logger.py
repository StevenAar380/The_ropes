import sys
import csv, os

def addlostitem():
    global lostItemlist
    lostItemlist = {
        "Description": None,
        "Location": None,
        "Tube": None,
        "Heading": None,
        "Date (DD/MM/YY)": None
    }
    
    description = input("Enter item discription>>>")
    location = input("Enter item location>>> ")
    tube = input("Enter item tube")
    heading = input("What is the heading>>> ")
    date = input("Enter date found>>> ")

    lostItemlist["Description"] = description
    lostItemlist["Location"] = location
    lostItemlist["Tube"] = tube
    lostItemlist["Heading"] = heading
    lostItemlist["Date (DD/MM/YY)"] = date

    filename = "lostItemslistTester.csv"
    fileExists = os.path.isfile(filename)

    with open(filename,"a" , newline="", encoding = "utf-8") as f:
        fieldnames = ["Description", "Location", "Heading", "Date (DD/MM/YY)"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        #Only write header if new
        if not fileExists:
            writer.writeheader()
        #Append to dictionary
        writer.writerow(lostItemlist)      
        print("Item successfully added")

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