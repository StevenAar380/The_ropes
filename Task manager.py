#Project: Student Gradebook Manager

gradeBook = {
}


def bookdisplay():
    for name, grade in gradeBook.items():
        print(f"""
        ------------------------------------
        student: {name} | Grade: {grade}
        ------------------------------------
        """)

done = 0

print("========================================")
print("Welcome to the Student Gradebook Manager")
while True:
    tname = input("enter the name>>> ")
    tgrade = input("Enter their grade>>> ")
    if tname == "done" or tgrade == "done":
        break
    gradeBook[tname] = tgrade

bookdisplay()
print(gradeBook)