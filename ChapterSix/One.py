'''
IF else and elif statements are a multiway decision taken by our program due to certain conditions in our code.

Syntax is :

if(condition 1):
    print("YES") #if the condition 1 is true
elif(condition 2):
    print("Maybe") #if the condition 2 is true
else:
    print("NO") #otherwise

'''

w = int(input())
if(w <= 5) :
    print("YES")
elif(w > 5 and w <= 10):
    print("Maybe")
else:
    print("NO")