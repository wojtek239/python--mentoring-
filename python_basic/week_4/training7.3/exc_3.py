list1 = ["abc", "def", "ghi", "jkl"]
list2 = [1, 2, 3, 4, 5]
list3 = ["xyz", 1, '2']

print(list1)
print(list2)
print(list3)

print("first elemenet of list 1 is: ", list1[0])
print("last element of list 1 is: ", list1[3])

list2[1] = list3[1]
print("after switching second element from list 3 to 2: ", list2)

new_val = input("please enter ur value: ")
list3[2] = new_val
print("after adding new element implemented by user: ", list3)

list1.append("word")
print("after adding new element to list1: ", list1)

del list1[2]
print("after deleting third element from list 1: ", list1)

how_many_elements = len(list3)
print("in list 3 we have: ", how_many_elements, "elements")

list1.extend(list3)
print("list 1 extended of list 3 is: ", list1)
