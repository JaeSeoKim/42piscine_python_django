#!/usr/bin/python3

import sys


def get_item(dict: dict, target: str):
    for key, item in dict.items():
        if key.upper() == target.upper():
            return item
    return None


def get_key(dict: dict, target: str):
    for key, item in dict.items():
        if item.upper() == target.upper():
            return key
    return None


def print_state_or_capital_city(str: str):
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
    value = get_item(states, str)
    key = get_key(capital_cities, str)
    if value:
        print(capital_cities.get(value),
              "is the state of", get_key(states, value))
    elif key:
        print(capital_cities.get(key), "is the capital of", get_key(states, key))
    else:
        print(str, "is neither a capital city nor a state")


def main():
    for i, v in enumerate(sys.argv):
        if i == 0:
            continue
        tokens = v.split(",")
        for token in tokens:
            token = token.strip()
            if token == "":
                continue
            print_state_or_capital_city(token)


if __name__ == '__main__':
    main()
