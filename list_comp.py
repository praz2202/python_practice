import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

a = random.sample(range(1,20),12)
b = random.sample(range(1,20),15)

x = [i for i in b if i in a]
x = list(set(x))
print x