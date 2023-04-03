from art import *
from rich import print

tprint("Builder")

class House:
    def __init__(self):
        self.part = {}


class BuilderHouse:
    def __init__(self):
        self.product = {}
        self.type = "Wood"
    
    @property
    def add_window(self):
        self.product['window'] = f"window {self.type}"
        return self
    
    @property
    def add_door(self):
        self.product['door'] = f"door {self.type}"
        return self
    
    @property
    def add_floor(self):
        self.product['floor'] = f"floor {self.type}"
        return self
    
    @property
    def add_roof(self):
        self.product['roof'] = f"roof {self.type}"
        return self
    
    def get_product(self):
        return self.product


    def __str__(self):
        return self.product.__str__()

class BuilderHouse2(BuilderHouse):
    def __init__(self):
        super().__init__()
        self.type = "Brick"

    @property
    def fireplace(self):
        self.product['fireplace'] = f"fireplace {self.type}"
        return self

myhouse = BuilderHouse2().add_window.add_door.add_floor.add_roof.fireplace.get_product()
print(myhouse)