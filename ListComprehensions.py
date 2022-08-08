myList = [1, 2, 3, 4, 5]
print([2 * item for item in myList])  # [2, 4, 6, 8, 10]

# Filter
myList = list(range(100))
filteredList = [item for item in myList if item % 10 == 0]
print(filteredList)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

filteredList = [item for item in myList if item % 10 < 3]
print(
    filteredList)  # [0, 1, 2, 10, 11, 12, 20, 21, 22, 30, 31, 32, 40, 41, 42, 50, 51, 52, 60, 61, 62, 70, 71, 72, 80, 81, 82, 90, 91, 92]

# List comprehensions with functions

myString = 'My name is Sinan Deger. I live in Cary'
print(myString.split("."))  # ['My name is Sinan Deger', ' I live in Cary']

print(myString.split()) # ['My', 'name', 'is', 'Sinan', 'Deger.', 'I', 'live', 'in', 'Cary']   to removing '.' we create a def

def cleanWord(word):
    return word.replace('.', '').lower()


print([cleanWord(word) for word in myString.split()]) # ['my', 'name', 'is', 'sinan', 'deger', 'i', 'live', 'in', 'cary']

# clean and filter at the same time
print([cleanWord(word) for word in myString.split() if len(cleanWord(word))< 3])  # ['my', 'is', 'i', 'in']
