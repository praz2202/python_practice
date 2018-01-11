import random
import sys


actual = random.randint(1, 9)
number =0

while number!=exit:

    number = raw_input('\nGuess a number between 1 to 9:\n')
    if number =='exit':
        print('Exiting ....')
        break
    else:
        number = int(number)
        if number == actual:
            print('You guessed it right')

        elif number>actual:
            print('you have guessed way too high')
        elif number<actual:
            print('you have guessed way too low')


