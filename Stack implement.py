items = ["tom","jerry","harry","ben","tim"]

def push():
    print("Enter the item you want to add")
    newItem = input(">>> ")
    items.append(newItem)
    print(items)

def pop():
    items.remove(items.remove[len(items)-1])
    print("item removed")
    print(items)

def top():
    print(f"item peeked: {items[len(items)-1]}")
    

def main():
    print("="*72)
    print("What would you like to do")
    print("1 -  PUSH ")
    print("2 - POP")
    print("3 - TOP")
    print("4 - Exit ")
    choice = input(">>> ")
    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == 3:
        top()
    elif choice == "4":
        exit()
    else:
        print("="*72)
        print("Invalid Input - please enter a number only")
        main()

print("-" * 72)
print("Initializing...")
main()