a = 5
b = 5
c = b

print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))

b += 1

print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
