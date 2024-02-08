#!/usr/bin/python3

import sys
num = len(sys.argv)
if num != 2:
    sys.exit()
def state():
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
    if sys.argv[1] in capital_cities.values():
        for key, value in states.items(): # Iterate over the states dictionary to find the corresponding state abbreviation
            if capital_cities[value] == sys.argv[1]: # if the value of the state matches to the key of the capital_cities dictionary then print the key of the states dictionary
                print (key)
                sys.exit()
    else:
        print ("Unknown capital city")

if __name__ == '__main__':
    state()