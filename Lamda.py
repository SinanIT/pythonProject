print(2 +3) #5
print((lambda x: x +3)(5)) #8


myList = [2,5,6,9,1,4,]
print(sorted(myList)) # [1, 2, 4, 5, 6, 9]

myList= [{'num' : 3}, {'num' : 2}, {'num':1}]

#sorted(myList) # TypeError: list indices must be integers or slices, not tuple

print(sorted(myList, key=lambda x: x['num'])) # [{'num': 1}, {'num': 2}, {'num': 3}]