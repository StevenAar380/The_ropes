import sys
import csv, os

def addlostitem():
    #global variablesd
    global lostItemlist
    global filename
    print("=================================================================================")
    #Initial Empty Dictionary - will be appended to .csv
    lostItemlist = {
        "Description": None,
        "Location": None,
        "Tube": None,
        "Heading": None,
        "Date (DD/MM/YY)": None
    }
    #User input
    description = input("Enter item discription>>> ")
    location = input("Enter item location>>> ")
    tube = input("Enter tube line>>> ")
    heading = input("What is the heading>>> ")
    date = input("Enter date found(DD/MM/YY) >>> ")

    #Assigning key value pairs for dictionary   
    lostItemlist["Description"] = description
    lostItemlist["Location"] = location
    lostItemlist["Tube"] = tube
    lostItemlist["Heading"] = heading
    lostItemlist["Date (DD/MM/YY)"] = date
    #Assigning variable to the filename
    filename = "lostItemslist.csv"
    #Conditional to ensure the dictionary isn't overwritten 
    fileExists = os.path.isfile(filename)

    with open(filename,"a" , newline="", encoding = "utf-8") as f:
        fieldnames = ["Description", "Location", "Tube", "Heading", "Date (DD/MM/YY)"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        #Only write header if new
        if not fileExists:
            writer.writeheader()
        #Append to dictionary
        writer.writerow(lostItemlist)      
        print("Item successfully added")
    menu()

def lostItemSearch():
    print("=================================================================================")
    #Redifining filename
    filename = "lostItemslist.csv"
    keyword = input("Enter your item>>> ") #Item input
    while keyword.isdigit():
        print("Invalid, string input only")
        lostItemSearch()
    with open(filename, "r", encoding="utf-8") as f: 
        csvfile = csv.reader(f, delimiter=",") #reader
        kw = keyword.strip().lower() # 
        found = False
        for row in csvfile:
            desc = row[0].strip().lower() 
            if kw in desc: #search function 
                print(row)
                found = True
                print("-" * 72)
            menu()
        if not found:
            print("-" * 72)
            print("No item found")
            menu()

        


def showAllItems():
    print("=================================================================================")
    filename = "lostItemslist.csv" 
    if not os.path.exists(filename):       # fresh check every time
        print("File doesn't exist")
        menu()
    else:
        with open(filename, newline="", encoding = "utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
            print("-----------------------If complete, press enter:----------------------------")
            finished = input("> ")
            menu()

            



def menu():
    print("=================================================================================")
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
    menu()

greeting()