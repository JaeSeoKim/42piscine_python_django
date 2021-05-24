#!/usr/bin/python3

import sys

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


def dict_get_key_from_value(dict: dict, value):
    for key, item in dict.items():
        if item == value:
            return key
    return None


def print_state(value: str):
    value = dict_get_key_from_value(capital_cities, value)
    if not value:
        print("Unknown capital city")
        return
    print(dict_get_key_from_value(states, value))


def main():
    if len(sys.argv) == 2:
        print_state(sys.argv[1])


if __name__ == '__main__':
    main()
