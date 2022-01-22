'''
If you want to create an empty set the syntax is given below.
'''
b = set()
print(type(b))
print(b)

b.add(4)
b.add(5)
# b.add([4, 5, 6]) #cannot add list
b.add((4, 5, 6)) #can obviously add tuple inside a set
print(b)