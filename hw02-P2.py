#homework02-problem2

# First develop a Creature class. Creatures have names. If I have a Creature
# object I can ask it to speak(). It will say: “My name is ... and I am Creature.”
# There should also exist more specific types of Creatures, e.g. Dogs. So, a
# Dog is a Creature. A Dog will say: “My name is ... and I am a Dog: woof.”
# Do the same with Cows

class Creature:
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def speak(self):
        print ("""
        My name is {} and I am a {} : {}.
        """.format(self.name, self.type, self.sound))
    
dog = Creature("Doggie", "Dog", "woof")
dog.speak()

cow = Creature("Cowboy", "Cow", "Moo~")
cow.speak()


# Christian's solution:
class creature:
    def __init__(self, name) -> None:
        self.name = name
        print('Creature created')
    
    def talk(self):
        return "My name is " + self.name + " and I am a " + type(self).__name__ + self.makeSound()
    
    def makeSound(self):
        return ". "
    
class dog(creature):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def makeSound(self):
        return ", and I say woof. "
    
a = creature('bob')
print(a.talk())

a = dog('daisy')
print(a.talk())