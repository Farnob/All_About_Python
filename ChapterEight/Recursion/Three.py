def factorial(n):
    if(n == 0 or n == 1): #Base condition which doesn't call the function further
        return 1
    else: #Function calling itself
        return n * factorial(n - 1)

'''
            This works as follows:
            factorial(4)
            4 * factorial(3)
            4 * [3 * factorial(2)]
            4 * 3 * [2 * factorial(1)]
            4 * 3 * 2 * [1] [function returned]
'''
f = factorial(5)
print(f)