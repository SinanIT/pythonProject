# LIST  // oerder of element is important

my_list = [1, 2, 3, 4]
print(my_list)
my_list = ['List', 'Of', 'Strings']
print(my_list)

my_list = ['List', True, 'Strings', [1, 'Iki']]
print(my_list)

my_list = [['List', 'Of', 'Strings'], [True, False], [1, 2, 3, 5]]
print(my_list)
my_list.append([9])  # we can modify the list [['List', 'Of', 'Strings'], [True, False], [1, 2, 3, 5], [9]]
print(my_list)

length = len(my_list)
print(length)

print([1, 2] == [2, 1])  # False
print([1, 2] == [1, 2])  # True

############################ SET ############################### ==> all the elements in it have to be unique

my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))  # <class 'set'>
my_set = {1, 1, 3, 4, 4}
length = len(my_set)
print(length)  # 3. No duplication
print(my_set)  # {1, 3, 4}
# Ordering element is not important
print({1, 2} == {2, 1})  # True
print({1, 2} == {1, 2})  # True

############################TUPLES#########################
# Tuples are declared with (). Tuples can not be modified

# Why we use tuples?  == > It is memory efficient, Good for storing lots of small things


my_tuple = (1, 2, 3)
tuple_length = len(my_tuple)
print(tuple_length)  # 3
print((1, 2) == (2, 1))  # False

############################################ DICTIONARY ###################################
# key value pairs. Keys are unique
my_dictionary = {
    'apple': 'A red fruit',
    'bear': 'A scary Animal'
}
print(my_dictionary)  # {'apple': 'A red fruit', 'bear': 'A scary Animal'}
print(my_dictionary.keys())  # dict_keys(['apple', 'bear'])
print(my_dictionary['apple'])  # A red fruit

"""
Set and Dictionaries
Both are defined with curly brackets
Set have unique values, dictionaries have unique keys
the order does not matter

"""



