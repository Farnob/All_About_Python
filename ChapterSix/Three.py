'''
write a program to print yes when the age entered by the user is greater than or equal to 18
'''

age = int(input("Enter your age user:- "))

if(age < 18):
    print("You are too small buddy.")
elif(age == 18):
    print("You are okay. You can have it.")
elif(age > 18 and age < 25):
    print("You are perfect for this.")
elif(age > 25 and age < 30):
    print("You are not perfect but you can have it.")
else:
    print("NO")
