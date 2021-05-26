#!/usr/bin/python3

from path import Path


def main():
    try:
        Path.makedirs('my_program')
    except FileExistsError as e:
        print(e)
    Path.touch('something')
    f = Path('something')
    f.write_lines(['hello', 'world!'])
    print(f.read_text())


if __name__ == '__main__':
    main()
