num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the second number:- "))
num3 = int(input("Enter the third number:- "))
num4 = int(input("Enter the fourth number:- "))

# if(num1 > num2):
#     print("Num1 is Greater than num2.")
#     f1 = num1
# else:
#     print("Num2 is Greater than num1.")
#     f1 = num2

# if(num3 > num4):
#     print("Num3 is greater than num3")
#     f2 = num3

# else:
#     print("Num4 is greater than num3.")
#     f2 = num4 

if(num1 > num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num3):
    f2 = num2
else:
    f2 = num3

if(f1 > f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest.")