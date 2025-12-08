items = [1,2,7,4,5,6,3,8,9,10]

class Stack():
    def stackMenu(items):
        print("-" * 72)
        print("How would you like to interact with your stack?")
        print()


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