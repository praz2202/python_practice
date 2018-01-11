import sys
def reverse(word):
    x =''
    for i in range(len(word)):
        x+=word[len(word)-i-1]

    return x





word = raw_input('enter a string\n')
word = str(word)
rev = reverse(word)
if rev == word:
    print('yes, it is a palindrome')
else:
    print('No, it is not a palindrome')





