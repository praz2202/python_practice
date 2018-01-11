import sys
import datetime
print('Hi, enter your name\n')
name = raw_input()

print('How old are you?\n')
age = raw_input()
age = int(age)

present = datetime.datetime.now()
present_year = present.year

later_year = present_year+(100 - age)


print '\nyou will be 100 years of age by', later_year