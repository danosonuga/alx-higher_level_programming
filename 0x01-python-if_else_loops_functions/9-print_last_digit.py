#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        num = number % 10
        return (num)
    elif number < 0:
        num = -(number)
        num = num % 10
        return (num)
