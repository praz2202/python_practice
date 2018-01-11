import sys


number = raw_input('Enter a number : ')

try:
    number = int(number)

except ValueError:
    print('value is not an integer')
    sys.exit(0)


#print (isinstance(number, (int, long)))

if number%2 ==0:
    print('Given number is even')

else:
    print('Given number is odd')