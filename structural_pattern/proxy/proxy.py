from abc import ABC, abstractmethod
from termcolor import colored


class MyAbstractProxy(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

    @abstractmethod
    def pre_request(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def post_request(self, *args, **kwargs) -> None:
        pass


class MyProxy(MyAbstractProxy):

    __message = "From Proxy 1"

    def __init__(self, service) -> None:
        self.service = service

    def request(self) -> None:
        self.pre_request()
        self.service.request()
        self.post_request()

    def pre_request(self, *args, **kwargs) -> None:
        print("Do Something before request")

    def post_request(self, *args, **kwargs) -> None:
        print("Do Something after request")


class SimpleService:
    _message = "From Service 1"

    @classmethod
    def request(self) -> None:
        print(self._message)


def client_code(subject) -> None:
    subject.request()


if __name__ == "__main__":
    print(colored("Client - Service", "light_red", attrs=["blink"]))
    client_code(SimpleService())
    print(colored("Client - Proxy", "light_green", attrs=["blink"]))
    
    proxy = MyProxy(SimpleService())
    client_code(proxy)
