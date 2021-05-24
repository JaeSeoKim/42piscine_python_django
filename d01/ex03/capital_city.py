#!/usr/bin/python3

import sys


def print_capital_city(key: str):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    key = states.get(key)
    if not key:
        print("Unknown state")
        return
    print(capital_cities.get(key))


def main():
    if len(sys.argv) == 2:
        print_capital_city(sys.argv[1])


if __name__ == '__main__':
    main()
