#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = []
    temp_res = 0
    for i in range(o, list_length):
        try:
            temp_res = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp_res = 0
            print("Wrong type")
        except ZeroDivisionError:
            temp_res = 0
            print("division by 0")
        except IndexError:
            temp_res = 0
            print("out of range")
        finally:
            pass
        div.append(temp_res)
    return div