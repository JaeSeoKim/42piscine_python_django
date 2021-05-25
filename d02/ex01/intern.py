#!/usr/bin/python3

class Coffee:
    def __str__(self) -> str:
        return "This is the worst coffee you ever tasted."


class Intern:
    def __init__(self, Name=None) -> None:
        self.Name = "My name? I’m nobody, an intern, I have no name." if Name is None else Name

    def __str__(self) -> str:
        return self.Name

    def work(self) -> str:
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self) -> Coffee:
        return Coffee()


def test():
    intern = Intern()
    mark = Intern("Mark")
    print(intern)
    print(mark)
    try:
        intern.work()
    except Exception as e:
        print(e)
    print(mark.make_coffee())


if __name__ == '__main__':
    test()
