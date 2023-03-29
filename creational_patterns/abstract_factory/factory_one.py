from abstract_factory import (
                                AbstractFactory,
                                AbstractPartA,
                                AbstractPartB
                            )

class ConcretePartA1(AbstractPartA):

    def __init__(self):
        self.part = 'Part A1 jing jing'

class ConcretePartB1(AbstractPartB):

    def __init__(self):
        self.part = 'Part B1 jing jing'

class ConcreteFactory1(AbstractFactory):

    def create_part_a(self):
        return ConcretePartA1()

    def create_part_b(self):
        return ConcretePartB1()