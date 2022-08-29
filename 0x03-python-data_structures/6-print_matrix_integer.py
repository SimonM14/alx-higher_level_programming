#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for vert in matrix:
        for hor in vert:
            print("{:d}".format(hor), end=" " if hor != vert[-1] else "")
        print()
