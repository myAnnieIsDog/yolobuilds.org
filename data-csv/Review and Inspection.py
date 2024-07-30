# Flow Control Examples
#
# Operators:
#   ==  equal to
#   !=  not equal to
#   <   less than
#   >   greater than
#   <=  less than or equal to
#   >=  greater than or equal to
#   The above operators return Boolean Values of True or False
#
# Boolean Operators:
#   and:
#       True and True = True
#       True and False = False
#       False and True = False
#       False and False = False
#   or:
#       True or True = True
#       True or False = True
#       False or True = True
#       False or False = False
#   not:
#       not True = False
#       not False = True
#       not not not True = False

# Importing modules
# First import all the functions from the module(s)
import random
import sys, os
from math import *

# Then use the function within the module
for i in range(5):
    print(random.randint(1, 10))

# Or import a single function from a module to use the function directly
# This is not a best practice in most cases.
from time import localtime, time
print(localtime(time()))

# if Statements
if 2 + 2 == 4 and not 2 + 2 != 5 and 2 * 2 < 3 + 2 and 5 == 0:
    print('True.')
elif False or not True:
    print('True.')
else:
    print('False.')

# while Loop Statements
spam = 0
while spam < 5:
    print('Hello, World!')
    spam = spam + 1
    if spam >= 3:
        continue
    if spam == 3:
        break

# for Loop Statement
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print(total)

if total == 5050:
    sys.exit()
total = 0
for i in range(9,-10,-2):
    print(i)





