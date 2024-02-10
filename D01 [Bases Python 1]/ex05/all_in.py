#!/usr/bin/python3

import sys
num = len(sys.argv)
if num != 2:
    sys.exit()
def all_in():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    parts = sys.argv[1].split(',')
    for element in parts:
        element = element.strip()
        check = 0
        for key, value in states.items():
            if element.lower() in key.lower():
                print (capital_cities[value], "is the capital of", key)
                check = 1
        for key, value in capital_cities.items():
            if element.lower() in value.lower():
                for k, v in states.items():
                    if v == key:
                        print (value, "is the capital of", k)
                        check = 1
        if check != 1 and element != "":
            print (element, "is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()