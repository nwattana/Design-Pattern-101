from abstract_factory import (
                                AbstractFactory,
                                AbstractPartA,
                                AbstractPartB
                            )

class ConcreteFactory2(AbstractFactory):
    
    def create_part_a(self):
        return ConcretePartA2()

    def create_part_b(self):
        return ConcretePartB2()

class ConcretePartA2(AbstractPartA):
    
    def __init__(self):
        self.part = 'Part A2 jing jing'

class ConcretePartB2(AbstractPartB):
    
    def __init__(self):
        self.part = 'Part B2 jing jing'