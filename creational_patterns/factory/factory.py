from rich import inspect as insp
from termcolor import colored

class Animal():
    body = "Four leg"

    def speak(self):
        pass

    def display(self):
        return self.body

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meaow"

class Bird(Animal):
    body = "2 Leg have wing can fly"

class AnimalFactory:
    def get_animal(self,animaltype=None):
        match animaltype:
            case 'cat':
                return Cat()
            case 'dog':
                return Dog()
            case 'bird':
                return Bird()

factory = AnimalFactory()
cat = factory.get_animal('cat')
bird = factory.get_animal('bird')
dog = factory.get_animal('dog')
print(cat.speak())
print(dog.speak())
print(bird.display())
