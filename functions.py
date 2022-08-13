print('Hello')
# defining
def multiplyByThree(val):
    return 3 * val
print(multiplyByThree(4))  # 12

#
def multiply(val1, val2):
    return val1 * val2

print(multiply(3, 4))  # 12
#
c = [1, 2, 3]
def appendFourToList(mylist):
    mylist.append(4)
appendFourToList(c)
print(c) # [1, 2, 3, 4]