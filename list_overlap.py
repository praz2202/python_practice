import sys
a = [1,2,4,7,8,10]
b=[1,3,5,8,1,4,4]
x =[]
for i in b:
    if (i in a) == True:
        x.append(i)

x= list(set(x))

print x

