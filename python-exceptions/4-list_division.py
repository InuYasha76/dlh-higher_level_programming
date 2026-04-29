#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is None:
        my_list_1 = []
    if my_list_2 is None:
        my_list_2 = []
    my_result_list = [0] * list_length
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            my_result_list[i] = result
    return my_result_list
