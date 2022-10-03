list1 = []
list2 = []

with open("C:\\Users\\chitroju\\Desktop\\py\\file1.txt") as file1:
    data1 = file1.readlines()
    list1 = [int(i.strip()) for i in data1]

with open("C:\\Users\\chitroju\\Desktop\\py\\file2.txt") as file2:
    data2 = file2.readlines()
    list2 = [int(i.strip()) for i in data2]

print(list1)
print(list2)
final_list = [i for i in list1 if i in list2]
print(final_list)
