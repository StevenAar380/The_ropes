
library = [["1984", "George Orwell","Dystopian","free"],
           ["The Martian", "Andy Weir", "Sci-fi","free"],
           ["Henry V", "William Shakespeare", "History","free"]
           ]

print(library[0])


'''

class Student:
    def __init__(self, username, age):
        self.username = username
        self.age = age

class Books:
    def __init__(self, bookname, bookauthor, genre, status):
        library 
        self.bookname = bookname
        self.bookauthor = bookauthor
        self.genre = genre
        self.status = status


    def libraryRead():
        for i in range (0, 3):
            print(f"{i+1}. {library[i][0]}")
        return


def bookmenu():
    print("What would you like to do in the library today:")
    #Options to take at library
    print("1 - Borrow a book")
    print("2 - Return a book")
    print("3 - Add a book")
    print("4 - Remove a book")
    choice = input("Choose a number: ")
    if choice == "1":
        print("What book would you like to borrow")
        Books.libraryRead()
        decision = input("enter a number:")
        
    elif choice == "2":
        ...
    elif choice == "3":
        ...
    elif choice == "4":
        ...
    else:
        print("Invalid Input")
        bookmenu()

def userInput():
    input_name = input("Enter full name: ") 
    input_age = input("Enter age")
    #creating object
    student = Student(input_name, input_age)
    print(f"Student username: {student.username}")
    print(f"Student age: {student.age}")
    bookmenu()
    
    

print("-" * 72)
print("Hello there")
userInput()'''