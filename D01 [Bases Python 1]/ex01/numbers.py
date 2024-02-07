#!/usr/bin/python3

try:
    with open('number.txt', 'r') as file:
        content = file.read()
        parts = content.split(',')
        for element in parts:
            print(element)
except FileNotFoundError:
    print("File not found")