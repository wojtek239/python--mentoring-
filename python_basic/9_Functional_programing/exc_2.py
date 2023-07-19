to_sort = [("English", 88), ("Science", 90), ("Maths", 97), ("Social Science", 82)]
to_sort.sort(key=lambda x: x[1])
print(f'Sorted List is: ')
for item in to_sort:
    print(item)