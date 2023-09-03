my_list = [1, 2, 4, 5, 9, 4, 12, 1, 4, 2, 6, 2, 9]
my_list.sort()
new_list = []
z = len(my_list)
for i in my_list:
    if (z - 1) < 0:
        continue
    # print(my_list[z - 1], my_list[z - 2])
    if my_list[z - 1] != my_list[z - 2]:
        new_list.append(my_list[z - 1])
    z = z - 1
new_list.sort()
my_list = new_list
print("The list with unique elements only:")
print(my_list)
