
def tip_calculator(amount, percentage):
    tip = amount * percentage/100
    total = amount + tip 
    return total

print("hi")
print(f"welcome to the tip calculator")
tipamount = int(input("Enter tip amount>>> "))
tipercentage = int(input("Enter tip percentage>>> "))
print(f"The total cost is {tip_calculator(tipamount, tipercentage)}")