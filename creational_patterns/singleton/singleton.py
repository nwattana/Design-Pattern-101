from rich import inspect as insp
from termcolor import colored
class Singleton:
    
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance !=  None:
            raise Exception(colored("This class is a Singleton", "red", attrs=["blink"]))
        else:
            Singleton.__instance = self

s1 = Singleton()
insp(s1)

s2 = Singleton.get_instance()
insp(s2)

s3 = Singleton.get_instance()
insp(s3)

s4 = Singleton()
