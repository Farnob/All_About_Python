#n! = 1 * 2 * 3 * ..... * n

from math import prod


n = 5
product = 1
for i in range(n):
    product = product * (i + 1)
print(product)