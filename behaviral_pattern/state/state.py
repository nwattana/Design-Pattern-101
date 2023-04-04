from __future__ import annotations
from abc import ABC, abstractmethod
# from rich import print
from termcolor import colored as col


# Change state
# Handle for each state

# Abstractstete has context as property, context setter, abstract(handle1, handle2)

class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        print(col(f"Context: Transition to {type(state).__name__}", "red"))
        self._state = state
        self._state.context = self

    def show_state(self):
        print(
                col(f"\nCurrent State {type(self._state).__name__}",
                "blue",
                attrs=["blink"])
              )

    def request(self):
        self.show_state()
        self._state.handle1()

    def request2(self):
        self.show_state()
        self._state.handle2()

    def request3(self):
        self.show_state()
        self._state.handle3()


class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context):
        # print(f"State: Setting context from {self.context} to {context}")
        self._context = context

    @abstractmethod
    def handle1(self):
        pass

    @abstractmethod
    def handle2(self):
        pass

    @abstractmethod
    def handle3(self):
        pass

    def __call__(self):
        print("State: Call")


class ConcreteStateA(State):
    def handle1(self):
        print(col("ConcreateStateA handles request1", "green"))

    def handle2(self):
        print(col("ConcreateStateA cannot handle request2", "yellow"))
        print(col("ConcreateStateA wants to change the state of the context", "yellow"))
        self.context.transition_to(ConcreteStateB())
 
    def handle3(self):
        print(col("ConcreateStateA cannot handle request3", "yellow"))
        print(col("ConcreateStateA wants to change the state of the context", "yellow"))
        self.context.transition_to(ConcreteStateC())


class ConcreteStateB(State):
    def handle1(self):
        print(col("ConcreateStateB cannot handle request1", "yellow"))
        print(col("ConcreateStateB wants to change the state of the context", "yellow"))
        self.context.transition_to(ConcreteStateA())

    def handle2(self):
        print(col("ConcreateStateB handles request2", "green"))
    
    def handle3(self):
        print(col("ConcreateStateB cannot handle request3", "yellow"))
        print(col("ConcreateStateB wants to change the state of the context", "yellow"))
        self.context.transition_to(ConcreteStateC())


class ConcreteStateC(State):
    def handle1(self):
        print(col("ConcreateStateC handles request1", "green"))

    def handle2(self):
        print(col("ConcreateStateC cannot handle request2", "yellow"))
        print(col("ConcreateStateC wants to change the state of the context", "yellow"))
        self.context.transition_to(ConcreteStateA())

    def handle3(self):
        print(col("ConcreateStateC handles request3", "green"))


if __name__ == "__main__":
    context = Context(ConcreteStateA())

    context.request()
    print("-----------------------\n")
    context.request2()
    context.request2()
    print("-----------------------\n")
    context.request3()
    context.request3()
    print("-----------------------\n")
