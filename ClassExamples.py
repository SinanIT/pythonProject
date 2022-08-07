class Dog:
    def __init__(self, name):
        self.name = name  # Attribute of Object
        self.legs = 4   # Attribute of Objects
    def speak(self): # Method
        print(self.name + ' says Bark!')


my_dog = Dog('Rover') # Object
another_dog = Dog('Fluffy') # Object
my_dog.speak() # Rover says Bark!
another_dog.speak() # Fluffy says Bark!
