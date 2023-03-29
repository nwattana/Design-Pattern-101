from factory_one import ConcreteFactory1
from factory_two import ConcreteFactory2

def req_part(factory):
    
    part_a = factory.create_part_a()
    part_b = factory.create_part_b()
    print("Part A: ", part_a)
    print("Part B: ", part_b)

req_part(ConcreteFactory1())
req_part(ConcreteFactory2())
