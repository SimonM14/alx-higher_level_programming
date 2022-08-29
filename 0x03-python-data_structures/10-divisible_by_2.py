#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for idx in range(len(my_list)):
        if my_list[idx] % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
