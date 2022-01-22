myDict = {
    "fast" : "In a Quick Manner",
    "harry" : "A Coder",
    "marks" : [1, 2, 3],
    "anotherDict" : {
        "Fahmidur" : "Python Developer",
        "Django" : "A Python Framework",
        "SpringBoot" : "A Java Framework for Web Development"
    },
    1 : 2
}

# print(type(myDict.keys())) #Prints the keys of the Dictionary but it is of type <class 'dict_keys'>. Acts like a list but not a list
# print(list(myDict.keys())) #Type casted into a list

# print(type(myDict.values())) ##Prints the keys of the Dictionary but it is of type <class 'dict_vlaues'>. Acts like a list but not a list

# print(myDict.items())

print(myDict)
updateDict = {
    "lovish" : "Friend",
    "Dhaka" : "Capital city of our country.",
    "harry" : "A Dancer"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get('lovish'))

print(myDict.get("harry2")) #Returns None as harry2 is not present in the Dictionary
print(myDict["harry2"]) #throws an error as harry2 is not present in the Dictionary