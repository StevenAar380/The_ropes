items = [1,2,3,4,5,6,7,8,9,10]

for i in range(0, len(items)-1):
    for j in range(1, len(items)):
        if i < j:
            print("Ordered")
        else:
            print("Disordered")