Physics = int(input("Enter your marks here :- "))
Chemistry = int(input("Enter your marks here :- "))
Biology = int(input("Enter your marks here :- "))

if(Physics < 33 or Chemistry < 33 or Biology < 33):
    print("You are Fail.")


if(((Physics + Chemistry + Biology) / 3)< 40 ):
    print("You are Fail.")
else:
    print("Congratulations! You have attain 40% marks.")