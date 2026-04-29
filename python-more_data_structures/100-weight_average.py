#!/usr/bin/python3
def weight_average(my_list=[]):
    return (sum(v * w for v, w in my_list) /
            sum(w for v, w in my_list) if my_list else 0)
