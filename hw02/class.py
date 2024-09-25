# class and inheritance

class Creature:
    def __init__(self, name):
        self.name = name
        print('Creature created.')

    def talk(self):
        return "My name is " + self.name + " and I am a " + type(self).__name__ + self.makeSound()
    
    
    
class Dog(Creature):
    def __init__(self, name):
        super().__init__(name)
    
    def makeSound(self):
        return ", and I say woof."
    

class Cow(Creature):
    def __init__(self, name):
        super().__init__(name)

    def makeSound(self):
        return ", and I say Moo."

a= Dog('Doggie')
print(a.talk())

b= Cow('Mumu')
print(b.talk())