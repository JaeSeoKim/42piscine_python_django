#!/usr/bin/python3

class Elem:
    class ElemException(Exception):
        def __init__(self) -> None:
            super().__init__("Elem Exception!")

    def __init__(self, name: str, attr=[]) -> None:
        self.name = name
        self.content = []
        self.attr = attr

    def __str__(self) -> str:
        result = ("<{name}{attr}>\n"
                  "{content}"
                  "</{name}>")

        def dict_to_attr():
            return "".join(" {value}".format(value=value) for value in self.attr).rstrip()

        def list_to_content():
            result = "".join("{}\n".format(val)
                             for val in self.content).splitlines(True)
            return "".join("  {}".format(line) for line in result)

        return result.format(
            name=self.name,
            content=list_to_content(),
            attr=dict_to_attr())

    def add_content(self, content):
        self.content.append(content)


def test():
    html = Elem(name="html", attr={"id=\"html\"", "style=\"html\""})
    body = Elem(name="body", attr={"class=\"test\""})
    html.add_content(body)
    h1 = Elem(name="h1")
    body.add_content(h1)
    h1.add_content("hello world!")
    h1.add_content('helloworld!')
    print(html)


if __name__ == '__main__':
    test()
