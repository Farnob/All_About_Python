#Here we will talk about input() function

'''
The input() function allows a user to insert a value into a program. input() returns a string value. You can convert the contents of an input using any data type. For instance, you can convert the value a user inserts to a floating-point number. 
'''

a = input("Enter a value:-")
print(a)
print(type(a))
b = input("Enter another value :- ")
b = int(b) #Type casted from String to Integer
print(b)
print(type(b))