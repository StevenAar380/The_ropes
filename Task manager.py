Mclaren = ["P1", "720s","750s","senna", "senna gtr"]

def car_generator(luckyno):
    luckyno -= 1
    return Mclaren[luckyno]


print("Congratulations you got a free Mclaren!")
luckyno = int(input("Enter your lucky number (1-5)>>> "))
print(f"Well done sir, you got a {car_generator(luckyno)}")