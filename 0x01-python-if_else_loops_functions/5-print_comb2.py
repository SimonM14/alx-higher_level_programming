#!/usr/bin/python3
for i in range(0, 99):
    if i == 98:
        print(i)
    else:
        print("{:0>2d}".format(i), end=", ")