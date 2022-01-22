letter = '''Dear <|NAME|>,
    Greetings from ABC coding house. I am happy to inform you that you are selected as a python developer in our startup.
Congratulations!
Happy Coding!

Date: <|DATE|>
'''

name = input("Enter Your Name:- \n")
date = input("Enter Today's Date:- \n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)