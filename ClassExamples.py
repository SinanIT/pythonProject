class Dog:
    #intance attributes
    legs = 4  # static attributes or variables
    def __init__(self, name):
        self.name = name  # Attribute of Object intance
        #self.legs = 4   # Attribute of Objects  instance
    def speak(self): # Method
        print(self.name + ' says Bark!')


my_dog = Dog('Rover') # Object
another_dog = Dog('Fluffy') # Object
print(my_dog.name) # Rover
print(my_dog.legs) # 4
my_dog.speak() # Rover says Bark!
another_dog.speak() # Fluffy says Bark!

print(Dog.legs) # 4

class AnotherDog:
    _legs = 4
    def __init__(self, name):
        self.name = name  # Attribute of Object intance
        #self.legs = 4   # Attribute of Objects  instance
    def speak(self): # Method
        print(self.name + ' says Bark!')

    def getLegs(self):
        return self._legs
my_dog = AnotherDog('Fluffy')
print(my_dog.name) #Fluffy
my_dog._legs = 3
print(my_dog.getLegs()) # 3
print(AnotherDog._legs) # 4  Class variable