items = [1,2,7,4,5,6,3,8,9,10]

class Stack():
    def stackMenu(self):
        print("-" * 72)
        print("How would you like to interact with your stack?")
        print("1 - Select an item")
        print("2 - Add an item")
        print("3 - Remove and item")
        print("4 - peek the top")
        stackChoice = input(">>> ")

        if stackChoice == "1":
            Stack.itemSelect()
        elif stackChoice == "2":
            Stack.itemAdd()
        elif stackChoice == "3":
            Stack.itemRemove()
        elif stackChoice() == "4":
            Stack.peekAboo()

    def itemSelect():
        global items
        print(f"What list in the item would you like to select (1 - {len(items)-1}")
        option = input(">>> ")
        while option.isdigit() == False:
            print("invalid")
            option = input(">>> ")
        option = int(option)

        if len(items)-1 - option:
            print(items[option])
        else:
            for i in range(len(items)-1, option):

        

    def itemAdd():
        print("What would you like to add")
        userInput = input(">>> ")
        if userInput.isdigit() == True:
            userInput = int(userInput)
        items.append(userInput)
    
    def itemRemove():
        ...
    def peekAboo():
        ...

def main():
    global items
    print("-" * 72)
    print("What data functionality would you like to use:")
    print("1 - Stack")
    print("2 - Queue")
    choice = input(">>> ")

    if choice == "1":
        stack = Stack()
        stack.stackMenu()

main()