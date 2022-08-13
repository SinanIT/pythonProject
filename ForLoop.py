my_List = {1,2,3,4,5}
for item in my_List:
    print(item)


animalLookup = {
    'a' : ['aardwark', 'antelope'],
    'b' : ['bear'],
    'c' : ['cat'],
    'd' : ['dog'],
}
for letters, animals in animalLookup.items():
    pass

for letters, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    else:
        print(f'Only animal : {animals[0]}')
                        #Only animal : bear
                        #Only animal : cat
                        #Only animal : dog'''

for letters, animals in animalLookup.items():
    if len(animals) > 1:
        print(f'Found {len(animals)} : {animals}')
        continue
    else:
        print(f'Only animal : {animals[0]}')

#For else
for number in range( 2, 100):
    for factor in range (2, int(number**0.5)):
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime')



