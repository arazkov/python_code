#!/usr/bin/python3

def palendrom(d_nam_1, d_nam_2):
    namber = str(d_nam_1 * d_nam_2)

    if namber == namber[::-1]:
        return d_nam_1 * d_nam_2


nam_pal = 0
for nam_1 in range(100, 1000):
    for nam_2 in range(100, 1000):
        if palendrom(nam_1, nam_2):
            if palendrom(nam_1, nam_2) > nam_pal:
                nam_pal = palendrom(nam_1, nam_2)
print(nam_pal)
