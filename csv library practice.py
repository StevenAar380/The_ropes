import csv, os

Review = {
    'Name': None,
    'year group': None,
    'Form': None,
    'Form tutor': None,

}

name = input("Enter your name: ")
yeargroup = input("Enter your year group:  ")
form = input("Enter your form class: ")
formtutor = input("Enter your form tutor name (miss/mister): ")

Review['Name'] = name
Review['year group'] = yeargroup
Review['Form'] = form
Review['Form tutor'] = formtutor

filename = "School system.csv"
fileExists = os.path.isfile(filename)


with open(filename ,'a' ,newline='' , encoding='utf-8') as f:
    fileheader = ['Name', 'year group', 'Form', 'Form tutor']
    writer = csv.DictWriter(f, fieldnames=fileheader)
    if not fileExists:
        writer.writeheader()
    writer.writerow(Review)

with open(filename, newline='' ,encoding='utf-8') as f:
    reader= csv.reader(f)
    for row in reader:
        print(row)
print("You are officially on the system!! ")
