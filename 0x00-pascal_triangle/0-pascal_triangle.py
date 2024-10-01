#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    return the pascal triangle.
    """
    pas_list = []
    if (n <= 0):
        return pas_list
    pas_list.append([1])
    if (n == 1):
        return pas_list
    for i in range(n - 1):
        app_list = []
        app_list.append(1)
        for l in range(len(pas_list[i])):
            if (l + 1 == len(pas_list)):
                app_list.append(1)
            else:
                app_list.append(pas_list[i][l] + pas_list[i][l + 1])
        pas_list.append(app_list)

    return (pas_list)
