# LIST

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myList[3:])  # [4, 5, 6, 7, 8, 9]

print(myList[0:10:2])  # [1, 3, 5, 7, 9] same below
print(myList[::2])  # [1, 3, 5, 7, 9]

for i in range(100):
    print(i)
myList = list(range(100))
print(myList[::10])  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print(myList[::-10])  # [99, 89, 79, 69, 59, 49, 39, 29, 19, 9]  backward

# MODUFYING LIST
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myList.append(10)
print(myList)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myList.insert(3, 'A new Value')
print(myList)  # [1, 2, 3, ' A new Value', 4, 5, 6, 7, 8, 9, 10]

# Remove Value
myList.remove('A new Value')
print(myList)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

myList.pop(8)
print(myList)

while len(myList):
    print(myList.pop())

print(myList) # After loop it is empty   []

a= [1,2,3,4,5]
b= a
a.append(6)
print(b)  # [1, 2, 3, 4, 5, 6]

a= [1,2,3,4,5]
b= a.copy()
a.append(6) #// it add element to the end of the list
print(a) #  [1, 2, 3, 4, 5, 6]
print(b)  # [1, 2, 3, 4, 5]

