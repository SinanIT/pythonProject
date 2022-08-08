animalList = [('a', 'adwark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]
animals = {item[0]: item[1] for item in animalList}
print(animals)  # {'a': 'adwark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

animals = {key: value for key, value in animalList}
print(animals)  # {'a': 'adwark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

print(animals.items())  # dict_items([('a', 'adwark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')])
print(list(animals.items()))  # [('a', 'adwark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]

# list of dictioanry
print([{'letter': key, 'name': value} for key, value in animals.items()]) # [{'letter': 'a', 'name': 'adwark'}, {'letter': 'b', 'name': 'bear'}, {'letter': 'c', 'name': 'cat'}, {'letter': 'd', 'name': 'dog'}]
