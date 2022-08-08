from collections import defaultdict
animals = {
    'a': 'aardwark',
    'b': 'bear',
    'c': 'cat',
}
print(animals)  # {'a': 'aardwark', 'b': 'bear', 'c': 'cat'}
animals['d'] = 'dog'

# add
print(animals)  # {'a': 'aardwark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

#update
animals['a'] = 'antelope'
print(animals) # {'a': 'antelope', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

#keys
print(animals.keys())  # dict_keys(['a', 'b', 'c', 'd'])  you can add a key but KEYS are immutable can not update/change directly
# to be update the dictionari you can convert to them list than update

print(list(animals.keys())) # ['a', 'b', 'c', 'd']
print(animals.values()) # dict_values(['antelope', 'bear', 'cat', 'dog'])

print(animals.get('e', 'elephant')) #  elephant
print(animals.get('e')) # None
print(animals) # {'a': 'antelope', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

#length
print(len(animals))  # 4

# DICTIOANRY of LIST
animals = {
    'a': ['aardwark', 'antelope'],
    'b': ['bear'],
}
animals['b'].append('bison')
print(animals) # {'a': ['aardwark', 'antelope'], 'b': ['bear', 'bison']}

animals['c'] = ['cat']
print(animals) # {'a': ['aardwark', 'antelope'], 'b': ['bear', 'bison'], 'c': ['cat']}

# what if we don't whetter the ket exist in dict or not? we just know what we want to add
# this can be handle two ways. first is if
if 'd' not in animals:
    animals['d'] = []
animals['d'] = ['bird']
# second way importin this: from collections import defaultdict
animals = defaultdict(list)
animals['e'].append('elephant')
print(animals)  # defaultdict(<class 'list'>, {'e': ['elephant']})
animals['e'].append('emu')
print(animals) # defaultdict(<class 'list'>, {'e': ['elephant', 'emu']})


