#!/usr/bin/python3

import sys
num = len(sys.argv)
if num != 2:
    sys.exit()
def capital_city():
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
    if sys.argv[1] in states:
        print (capital_cities[states[sys.argv[1]]])
    else:
        print ("Unknown state")

if __name__ == '__main__':
    capital_city()
