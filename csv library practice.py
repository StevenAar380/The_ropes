import csv, os

lostItems = {
    "Description": None,
    "Location": None,
    "Heading": None,
    "Date (DD/MM/YY)": None
}

description = input("Enter item discription>>>")
location = input("Enter item location>>> ")
heading = input("What is the heading>>> ")
date = input("Enter date found>>> ")

lostItems["Description"] = description
lostItems["Location"] = location
lostItems["Heading"] = heading
lostItems["Date (DD/MM/YY)"] = date

filename = "lostItemslistTester.csv"
fileExists = os.path.isfile(filename)

with open(filename,"a" , newline="", encoding = "utf-8") as f:
    fieldnames = ["Description", "Location", "Heading", "Date (DD/MM/YY)"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    #Only write header if new
    if not fileExists:
        writer.writeheader()
    #Append to dictionary
    writer.writerow(lostItems)  

with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

