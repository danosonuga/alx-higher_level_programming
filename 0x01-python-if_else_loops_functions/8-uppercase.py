#!/usr/bin/python3
def uppercase(str):
    for s in range(str):
        if ord(s) >= 97 and ord(s)<=122:
            s = ord(s) - 32
            print("{:c}".format(s), end='')
        elif ord(s) == 32:
            print(" ")
