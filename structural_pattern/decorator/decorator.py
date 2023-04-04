from abc import ABC, abstractmethod
from termcolor import colored

class MyAbstractDecorator(ABC):

    @abstractmethod
    def post_function(self, function) -> None:
        pass

    @abstractmethod
    def pre_function(self, function) -> None:
        pass


class HelloDecorator(MyAbstractDecorator):

    def post_function(self, function, *args, **kwargs) -> None:
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            print("Hello, I'm post function")
        return wrapper

    def pre_function(self, function, *args, **kwargs) -> None:
        def wrapper(*args, **kwargs):
            print("Hello, I'm pre function")
            function(*args, **kwargs)
        return wrapper

    def around_function(self, function, *args, **kwargs) -> None:
        def wrapper(*args, **kwargs):
            print("Hello, I'm pre of around function")
            function(*args, **kwargs)
            print("Hello, I'm post of around function")
        return wrapper


decor = HelloDecorator()


@decor.pre_function
def hello(*args):
    print("Hello1", args)


@decor.post_function
def hello2(*args):
    print("Hello2", args)


@decor.around_function
def hello3(*args ):
    print("Hello3", args)


@decor.post_function
@decor.around_function
@decor.pre_function
def hello4(*args):
    print("Hello4", args)


if __name__ == "__main__":
    hello("arg1", "arg2")
    print("\n")
    hello2("arg1", "arg2", "arg3")
    print("\n")
    hello3("arg1", "arg2", "arg3", "arg4")
    print("\n")
    hello4("arg1", "arg2", "arg3", "arg4", "arg5")