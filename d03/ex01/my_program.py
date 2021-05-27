#!/usr/bin/env python3

from path import Path


def main():
    try:
        Path.makedirs('something')
    except FileExistsError as e:
        print(e)
    Path.touch('something/something')
    f = Path('something/something')
    f.write_lines(['hello', 'world!'])
    print(f.read_text())


if __name__ == '__main__':
    main()
