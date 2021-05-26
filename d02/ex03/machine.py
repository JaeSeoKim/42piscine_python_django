#!/usr/bin/python3

import random
from beverages import HotBeverage, Coffee, Tea, Cappuccino, Chocolate


class CoffeeMachine:

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            self.name = "empty cup"
            self.price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self) -> None:
        self.bronkenCount = 10

    def repair(self) -> None:
        self.bronkenCount = 10

    def serve(self, drink: HotBeverage) -> HotBeverage():
        if (self.bronkenCount <= 0):
            raise CoffeeMachine.BrokenMachineException
        self.bronkenCount -= 1
        if random.randint(0, 5) == 0:
            return CoffeeMachine.EmptyCup()
        return drink()


def test():
    coffeeMachine = CoffeeMachine()
    for _ in range(23):
        try:
            print(coffeeMachine.serve(random.choice(
                [Coffee, Tea, Cappuccino, Chocolate])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffeeMachine.repair()


if __name__ == '__main__':
    test()
