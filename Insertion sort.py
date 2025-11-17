numbers = [9,2,5,4,6,3,7,8]
sorted_list = []

print(f"Original list: {list}")

sorted_list.append(list[0])
print(sorted_list)
for i in range (1, len(list)):
    if len(sorted_list) == 1:
        if list[i] >= sorted_list[0]:
            sorted_list.append(list[i])
        else:
            sorted_list.insert(0, list[i])
        print(sorted_list)
    else:
        for j in range (len(sorted_list) -1, -1, -1):
            if list[i] < sorted_list[j]:
                if j == 0:
                    sorted_list.insert(0, list[i])
                break
            else:
                sorted_list.insert(j+1, list[i])
                break
        print(sorted_list)

