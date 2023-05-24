a = [1, -2, 3, 5, 7]
b = ["aga", -5, 17]
common_element = bool(set(a) & set(b))
if common_element:
    print("both lists have common element")
else:
    print("they dont have a common element")
