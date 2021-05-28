a = [1, 2, 3]
b = a
print(a)
print(b)
print(id(a))
print(id(b))
b[1] = 4
print(a)
print(b)
print(id(a))
print(id(b))
'''del b
print(a)
print(id(a))
'''
'''
del a
print(b)
print(id(b))
'''