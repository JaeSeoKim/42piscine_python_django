#!/usr/bin/python3
import os
import sys
import re
import settings


def main():
    if (len(sys.argv) != 2):
        return print("wrong argument count")
    path = sys.argv[1]
    regex = re.compile(".*\.template")
    if not regex.match(path):
        return print("wrong extension, (required: .template)")
    if not os.path.isfile(path):
        return print("does not exit file... : {}".format(path))
    f = open(path, "r")
    template = "".join(f.readlines())
    f.close()
    file = template.format(
        name=settings.name, surname=settings.surname, title=settings.title,
        age=settings.age, profession=settings.profession)
    regex = re.compile("(\.template)")
    path = "".join([path[0:regex.search(path).start()], ".html"])
    f = open(path, "w")
    f.write(file)
    f.close()


if __name__ == '__main__':
    main()
