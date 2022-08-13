# Funtions are just variables associate some data
x = 5
def x():
    return 5
print(x.__code__.co_varnames)   # ()
print(x.__code__.co_code)  # b'd\x01S\x00'


def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)
print(performOperation(1,2, operation = 'sum'))

#locals()  defined inside the funtion

def performOperation(num1 , num2, operation = 'sum'):
    print(locals())
print(performOperation(1,2, operation = 'multiply')) #{'nm1': 1, 'num2': 2, 'operation': 'multiply'}


#globals
#Methods have access the global data
# Methods don't have acces eachother data
#Pythhon cheks the local scope first then chek to glabal

message = 'Some global messaga'
varA = 2
def funtion1(varA, varB):
    message = 'some local data'
    print(message) # v
    print(varA)  # result 1 because it define in local scope
    print(locals())

def funtion2 (varC, varB):
    print(message)
    print(varA) # resut 2 because varA not defined inside the method, it cames from ,global
    print(locals())
print(funtion1(1,2)) # {'varA': 1, 'varB': 2}
print(funtion2(3,4)) # {'varC': 3, 'varB': 4}


def funtion1(varA, varB):
    message = 'some local data'
    print(varA) # 1
    def inner_funtion(varA, varB):
        print(varA) # 123
        print(f'inner_funtion local scope: {locals()}')
    inner_funtion(123, 456)
print(funtion1(1,2)) #  inner_funtion local scope: {'varA': 123, 'varB': 456}
