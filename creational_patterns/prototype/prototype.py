from abc import abstractmethod
from art import *

class Prototype:
    @abstractmethod
    def clone(self):
        pass


class Zombie(Prototype):
    def __init__(self, name, health):
        print(f"Create {name} with {health} health")
        self.name = name
        self.health = health

    def clone(self):
        return Zombie(self.name + "-clone", self.health)

    def __str__(self):
        return f"{self.name} {self.health}"

    def get_attack(self, damage):
        self.health -= damage
        print(f"{self.name} get {damage} damage")
        if self.health <= 0:
            self._death()

    def _death(self):
        self.delete()

    def __del__(self):
        print(f"{self.name} is dead")


zombie1 = Zombie("zombie 1", 100)
zombie1.get_attack(10)
zombie2 = zombie1.clone()
zombie3= zombie2.clone()
zombie3.get_attack(10)
zombie4 = zombie3.clone()
tprint("End")

