import math
# Slicing
name = 'My name is Sinan Koyun'
print(name[0])  # M

print(name[0:7])  # My name (up to 7)
print(name[:7])  # My name (up to 7)

print(name[11:])  # from 11 to the end  Sinan Koyun

myList = [1,2,3,4,5]

print(myList[2:4]) # [3, 4]

# FORMATTING
print('My number is ' + str(5))  # My number is  5

print(f'My number is {5}') # My number is 5

print(f'My number is {5} and twice that is {2*5}')  # My number is 5 and twice that is 10

print(f'Pi is: {math.pi: .2f}') # Pi is:  3.14

# MULTI-LINE STRINGS
myString = '''
Here is block of text 
i can add new lines!
text doesn't stop until it sees \'\'\'
'''
print(myString)

