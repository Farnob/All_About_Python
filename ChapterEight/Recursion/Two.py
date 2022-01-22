# def fact_iterative(n):
#     product = 1
#     for i in range(n):
#         product = product * (i + 1)
#     return product

def fact_Recursive(n):
    if(n == 1 or n == 0): #Base Condition
        return 1
    else: #Function calling itself
        return n * fact_Recursive(n - 1)

# f = fact_iterative(5)
f = fact_Recursive(2)

print("The Result is:- ", f)