#!/usr/bin/python3
d = 0
u = 1
while d < 9:
    while u < 10:
        r = d * 10 + u
        if r != 89:
            print("{:0>2}".format(r), end=", ")
        else:
            print("{:0>2}".format(r))
        u += 1
    d += 1
    u = d + 1
