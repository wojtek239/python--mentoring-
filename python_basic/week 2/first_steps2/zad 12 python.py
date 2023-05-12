import copy

list1 = ['a', 'b', 'c']
list2 = list1
list3 = list1[:]
list4 = copy.copy(list1)
list5 = copy.deepcopy()

print(list1)
print(list2)
print(list3)


print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))

list1.append('d')

print(list1)
print(list2)
print(list3)
print(list4)

print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))
