
library = [["1984", "George Orwell","Dystopian",False],
           ["The Martian", "Andy Weir", "Sci-fi",False],
           ["Henry V", "William Shakespeare", "History",False]
           ]



class Student:
    def __init__(self, username, age):
        self.username = username
        self.age = age

class Books:
    def __init__(self, bookname, bookauthor, genre, borrowed): 
        self.bookname = bookname
        self.bookauthor = bookauthor
        self.genre = genre
        self.borrowed = borrowed

    def libraryRead():
        for i in range (0, len(library)):
            print(f"{i+1}. {library[i][0]}")
        return
    
    def librarybookborrow(decision): 
        decision = int(decision)
        library[decision-1][3] = True
        return

    def librarybookreturn(decision):
        decision = int(decision)
        if library[decision-1][3] == False:
            return print("you can't return something you never took -_- ")
        library[decision-1][3] = False
        return
    
    def librarybookadd(name, author, genre):
        library.append([name, author, genre, False])
        return
    

def bookborrow():
    print("What book would you like to borrow")
    Books.libraryRead()
    decision = input("enter a number:")
    while decision.isdigit() == False or int(decision) > len(library) or int(decision) < 1:
        print("invalid")
        bookborrow()
    Books.librarybookborrow(decision)
    print(library)
    bookmenu()


def bookreturn():
    print("What book would you like to return")
    Books.libraryRead()
    decision = input("enter a number:")
    while decision.isdigit() == False or int(decision) > len(library):
        print("invalid")
        bookreturn()
    Books.librarybookreturn(decision)
    print(library)
    bookmenu()

def bookadd():
    print("Very well")
    name = input("Enter name: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    Books.librarybookadd(name, author, genre)
    print(library)
    bookmenu()



def bookmenu():
    print("-" * 72)
    print("What would you like to do in the library today:")
    #Options to take at library
    print("1 - Borrow a book")
    print("2 - Return a book")
    print("3 - Add a book")
    print("4 - quit")
    choice = input("Choose a number: ")
    if choice == "1":
        bookborrow()
    elif choice == "2":
        bookreturn()
    elif choice == "3":
        bookadd()
    elif choice == "4":
        exit()
    else:
        print("Invalid Input")
        bookmenu()

def userInput():
    input_name = input("Enter full name: ") 
    input_age = input("Enter age")
    #creating studen data objects
    student = Student(input_name, input_age)
    print(f"Student username: {student.username}")
    print(f"Student age: {student.age}")
    bookmenu()
    
    

print("-" * 72)
print("Hello there")
userInput()