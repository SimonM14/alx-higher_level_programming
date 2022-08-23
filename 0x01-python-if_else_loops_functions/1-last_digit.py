#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
        lastno = ((number * -1) % 10) * -1
else:
        lastno = number % 10
if lastno == 0:
        print("Last digit of {} is {} and is 0".format(number, lastno))
elif lastno > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, lastno))
elif lastno < 6 and lastno != 0:
        print("Last digit of {} is {} and is less than 6 and not\0".format(number, lastno))
