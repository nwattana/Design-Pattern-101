# Create Postoffice send mail for client
# give me Coffee
# """

from abc import ABC, abstractmethod
from termcolor import colored
from art import art


class MyAbstractFacade(ABC):

    @abstractmethod
    def result(self):
        pass


class MyFacade(MyAbstractFacade):
    args = []
    message = '\
1. Planting the coffee trees\n\
2. Harvesting the coffee cherries\n\
3. Processing the coffee cherries\n\
4. Sorting and grading the coffee beans\n\
5. Roasting the coffee beans\n\
6. Grinding the coffee beans\n\
7. Brewing the coffee\n\
'.strip("\n").split("\n")

    def __init__(self):
        for i in self.message:
            self.args.append(i)

    def do_subprocess1(self):
        print(colored("Subprocess 1 start", "green"))
        for i, val in enumerate(self.args):
            if i == 3:
                break
            if val == '':
                continue
            print("Do ", val)
        print(colored("Subprocess 1 Success", "red"))
    
    def do_subprocess2(self):
        print(colored("Subprocess 2", "green"))
        for i, val in enumerate(self.args):
            if val == '' or i < 3:
                continue
            print("Do ", val)
        print(colored("Subprocess 2 Success", "red"))

    @property
    def show(self):
        self.do_subprocess1()
        self.do_subprocess2()
        return self

    def result(self):
        print('coffee is ready')
        return "  ~\n" + art("coffee") + art("put the table back")
    
    @property
    def get_coffee(self):
        return self.result()


if __name__ == "__main__":

    facade = MyFacade()
    # print(colored(facade.show.result(), "light_green", attrs=["blink"]))
    print(facade.get_coffee)
    # print(facade.show.get_coffee)
