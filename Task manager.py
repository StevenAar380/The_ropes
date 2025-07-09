#Project: Student Gradebook Manager

gradeBook = {
}


def bookdisplay():
    print(f"""
    ====================================
    Name: {gradeBook.get("name","N/A")}
    Grade: {gradeBook.get("grade","N/A")}
    =====================================
    """)



print("========================================")
print("Welcome to the Student Gradebook Manager")
thename = input("enter the name>>> ")
gradeBook.update({"name":thename})
thegrade = input("Enter the grade>>> ")
gradeBook.update({"grade": thegrade})

bookdisplay()
    