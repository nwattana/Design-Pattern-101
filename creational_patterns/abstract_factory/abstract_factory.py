# Description: Abstract Factory Pattern
# Date: 29/3/2023
# Pattern Intend: 
#   Abstract Factory is a creational design pattern that 
#   lets you produce families of related objects without 
#   specifying their concrete classes.


class AbstractFactory:

    def __init__(self):
        self.parts = []

    def create_part_a(self):
        pass

    def create_part_b(self, part):
        pass

    def __str__(self):
        return f'AbstractFactory: {self.parts}'

class AbstractPartA:

    def __init__(self):
        self.part = 'Part A'

    def __str__(self):
        return f'AbstractPartA: {self.part}'

class AbstractPartB:

    def __init__(self):
        self.part = 'Part B'

    def __str__(self):
        return f'AbstractPartB: {self.part}'



