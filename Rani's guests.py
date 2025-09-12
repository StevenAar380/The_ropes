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
    contage = 100
    total18 = 0
    while True:
        tname = input("Enter the name (type done when finished): ")
        if tname == "done":
            break
        tage = input("Enter age(number only): ")
        while tage.isdigit() == False:
            print("I said enter a number you failiure")
            tage = input("Enter age(number only): ")
        tage = int(tage)
        if tage < contage:
            contage = tage
            yperson = tname
        elif tage >= 18:
            total18 += 1
        total += 1
        guest[tname] = tage
    dictAdd(tname, tage, total,yperson, total18)
    
def dictAdd(name, age, total,yperson, total18):
    for name, age in guest.items():
        print(f"""
        -----------------------------------
        Student: {name} | Age: {age}             
        """)

    stats(total,yperson, total18)
    

def stats(total,yperson, total18):
    print("=" * 72)
    print(f"The total number of guests are {total}")
    print(f"the youngest person was {yperson}")
    print(f"the total number of people over 18 was {total18}")
    print("=" * 72)
    sys.exit()

main()