#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
output = "Last digit of"
if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = ((number * -1) % 10) * -1
if lastdigit > 5:
    print(f"{output} {number} is {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"{output} {number} is {lastdigit} and is 0")
else:
    print(f"{output} {number} is {lastdigit} and is less than 6 and not 0")
