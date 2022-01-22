#Here we will talk about Typecasting

'''
Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

    N.B :-
        Typecast is a way of changing an object from one data type to the next. ... A typecast example is the transformation of an integer into a string. This could be used to compare two numbers if one is stored as a string and the other is an integer.
'''

'''Before TypeCasting'''
a = "3434" #Double quotes er vitore ekta String
print(type(a)) #proof that "3434 is a string"
# print(a + 5) # This is a TypeError (can only concatenate str (not "int") to str)


'''After TypeCasting'''
b = int("3434") #now it is typecasted from String to Integer
print(type(b)) #proof that b is a int
print(b + 5) # result is 3439
