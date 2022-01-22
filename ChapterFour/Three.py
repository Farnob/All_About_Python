L_one = [1, 8, 7, 2, 21, 15]

L_one.sort()
# print(L_one) #Sorts the list from low to high
L_one.append(100)
# print(L_one) #Adds an element at the end of the list
'''L_one.reverse()'''
# print(L_one) #Reverses the list
L_one.extend(L_one)
# print(L_one) #Add the elements of a list (or any iterable), to the end of the current list
L_one.insert(3, 22222)
# print(L_one) #Adds an element at the specified position { point to be noted is that the first value inside the brackets is the position where you want to insert the value and the second value inside the brackets is the element itself.}
L_one.pop(2)
# print(L_one) #will delete the element at index 2
L_one.remove(100)
# print(L_one) #will delete 100 from the list and if there is two or more 100 in the list than it will remove the first 100 of the list

