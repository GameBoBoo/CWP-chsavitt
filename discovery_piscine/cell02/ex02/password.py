#!/usr/bin/env python3
secret_password = "Python is awesome"
user_input = input().strip()

if user_input == secret_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")