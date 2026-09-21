#!/usr/bin/env python3
num = float(input("Give me a number: ").strip())

if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")