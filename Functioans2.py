import math
def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2


print(performOperation(2, 3, 'sum'))


# named parameters

def performOperation(num1, num2, operation= 'sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performOperation(2, 3, 'sum'))

def performOperation(num1, num2, operation= 'sum', messege = 'Default message'):
    print(messege)
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
print(performOperation(2, 3, messege='A new message',operation='multiply')) # override

# Keyword argments must come after positional arguments
# Afterwards, keyword arguments can be in any order

# ARGS

def performOperation(*args): ## we need asterix here before args
    print(args)

print(performOperation(1,2,3)) # (1, 2, 3) # without asterix @TypeError: performOperation() takes 1 positional argument but 3 were given

# kwargs  keyword argumets

def performOperation(*args, **kwargs): ## we need asterix here before args
    print(args)
    print(kwargs)
print(performOperation(1,2,3, operation = 'sum'))  # (1, 2, 3) {'operation': 'sum'}


def performOperation(*args, operation = 'sum'): ## we need asterix here before args
    if operation == 'sum':
        return sum(args)
    if operation == 'multiply':
        return math.prod(args)
print(performOperation(1,2,3,6,7,8, operation = 'sum'))
