#Random Selector
import random
done = 0
list = []

print("Hello there")
while done != 1:
    temp = input("Enter name (type null when complete!) >>> ")
    list.append(temp)
    print(list)
    if temp.lower() == "null":
        done = 1
        rand = random.randint(0,len(list))
        print("Your random person is", list[rand])