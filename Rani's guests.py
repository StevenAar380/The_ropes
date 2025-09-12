import sys

guest = {
}

def main():
    print("=" * 72)
    print("Hello RANI!")
    nameinput()



def nameinput():
    total = 0
    yperson = ""
    total18 = 0
    while True:
        tname = input("Enter the name: ")
        tage = int(input("Enter age: "))
        if tage < tage:
            yperson = tname
        if tage >= 18:
            total18 += 1
        if tname == "done" or tage == "done":
            break
        total += 1
        guest[tname] = tage
        dictAdd(tname, tage, total,yperson, total18)
    
def dictAdd(name, age, total,yperson, total18):
    for name, age in guest.items():
        print(f"""
        -----------------------------------
        Student: {name} | Grade: {age}             
        """)

    stats(total,yperson, total18)
    

def stats(total,yperson, total18):
    print(f"The total number of guests are {total}")
    print(f"the youngest person was {yperson}")
    print(f"the total number of people over 18 was {total18}")
    sys.exit()

main()