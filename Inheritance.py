class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name  # Attribute of Object intance
        #self.legs = 4   # Attribute of Objects  instance
    def speak(self): # Method
        print(self.name + ' says Bark!')

    def getLegs(self):
        return self._legs

myDog = Dog ('Rover')
myDog.speak() # Rover says Bark!

class Doberman(Dog):
    '''extend the method'''
    def speak(self):  # Overriden method
        print(f'{self.name} says: Yap yap yap!')

    # new method
    def wagTail(self):
        print('Vigorus wagging!')

dog = Doberman('Roxy')
dog.speak() # Roxy says: Yap yap yap!
dog.wagTail() # Vigorus wagging!

