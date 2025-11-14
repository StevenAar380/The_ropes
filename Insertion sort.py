list = [9,2,3,4,5,6,7,8,1]
sorted_list = []

print(f"Original list: {list}")

sorted_list.append(list[0])
for i in range (1, len(list)):
    currentItem = list[i]
    if currentItem >= sorted_list[0]:
        

