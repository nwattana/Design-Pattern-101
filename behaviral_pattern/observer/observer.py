from __future__ import annotations
from abc import ABC, abstractmethod
from termcolor import colored


class AbstractSubscriptionEvent(ABC):
    """
    A Class representing an abstract store
    had Three methods:
    attach: attach an observer to the subject
    detach: detach an observer from the subject
    notify: notify all observers about an event
    """

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Event(AbstractSubscriptionEvent):
    _name: str = None
    
    def __init__(self, name):
        self._subscribers = []
        self._name = name

    @property
    def name(self):
        return colored(self._name, "red")
    
    def attach(self, observer: Observer):
        print(f"{self.name} Attached an observer. {observer.name}")
        self._subscribers.append(observer)

    def detach(self, observer: Observer):
        self._subscribers.remove(observer)

    def notify(self):
        print(f"{self.name} start Notifying")
        for i in self._subscribers:
            print(f"Event1: Notifying {i.name} about {self.name}")


class Observer:
    _event_list = []
    _name: str = None

    @property
    def name(self):
        return colored(self._name, "green")

    def __init__(self, name: str = "Observer"):
        self._name = name

    def subscribe(self, event):
        self._event_list.append(event)
        event.attach(self)

    def unscribe(self, event):
        self._event_list.remove(event)
        event.detach(self)


if __name__ == "__main__":
    
    event1 = Event("Funny Event")
    event2 = Event("Horror Event")
    ob1 = Observer("Obs1")
    ob2 = Observer("Obs2")
    ob3 = Observer("Obs3")
    ob1.subscribe(event1)
    ob3.subscribe(event1)
    
    ob2.subscribe(event2)
    print("")
    event1.notify()
    print("")
    event2.notify()
