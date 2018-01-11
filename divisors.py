import sys

number = raw_input("Enter number: ")

number = int(number)

x = range(2,number+1)

for i in x:
    if number%i ==0:
        print i