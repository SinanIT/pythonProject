# SETs

mySet= {'a', 'b', 'c'}
print(mySet) # {'a', 'c', 'b'}

mySet = set(['a', 'b', 'c', 'c'])
print(mySet) #{'a', 'c', 'b'}

mySet = set(('a', 'b', 'c', 'd'))
print(mySet) #{'a', 'c', 'b', 'd'}

mySet = set(('a', 'b', 'c', 'c'))
print(mySet) #{'a', 'c', 'b'}

'''
 Declared with curly brackets {}
 All elements are unique
 The order does Not matter
 No index
 No slicing
 Element can be added
'''
mySet.add('Z')
print(mySet) # {'c', 'b', 'a', 'Z'}

print('a' in mySet) # True

print('z' in mySet) # False

print(len(mySet)) # 4

while len(mySet):
    print(mySet.pop())
print(mySet) # it is an emptyr set set()

mySet = {'a', 'b', 'c', 'd', 'e'}
mySet.discard('a')
print(mySet) # {'d', 'e', 'c', 'b'}

#TUPLES
'''
similar to list
declared with parentheses
order preserve
Can NOT modified
has index

Why we use it?

More efficient than list
They don't grow or change
Store compactly in memory
'''
myTuple = ('a', 'b', 'c')
print(myTuple) # ('a', 'b', 'c')
def returnMultipleValues():
    return 1,2,3
print(type(returnMultipleValues()))  # it returns tuple <class 'tuple'>

myTuple = 'a', 'b', 'c'  # not preferred
print(type(myTuple)) # <class 'tuple'>

a,b,c = returnMultipleValues()
print(a)
print(b)
print(c)



