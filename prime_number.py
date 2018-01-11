import sys
def no_divisors(number):

    count =0
    if number ==2:
        pass
    else:
        x = range(2,number)

        for i in x:
            if number%i ==0:
                 count+=1
    return count

numb = raw_input('Input a number\n')
numb = int(numb)

no_of_div = no_divisors(numb)

if no_of_div ==0:
    print('This is a prime number')
else:
    print ('This is not a prime number')