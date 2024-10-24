#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
import sys, signal


try:
    i = 0
    filesSize = 0
    counter200 = 0
    counter401 = 0
    counter403 = 0
    counter404 = 0
    counter405 = 0
    counter500 = 0
    for line in sys.stdin:
        text = line.split()
        filesSize += int(text[-1])
        if text[-2] == "200":
            counter200 += 1
        if text[-2] == "401":
            counter401 += 1
        if text[-2] == "403":
            counter403 += 1
        if text[-2] == "404":
            counter404 += 1
        if text[-2] == "405":
            counter405 += 1
        if text[-2] == "500":
            counter500 += 1
        i += 1
        if i == 10:
            i = 0
            print(f"File size: {filesSize}")
            print(f"200: {counter200}")
            print(f"401: {counter401}")
            print(f"403: {counter403}")
            print(f"404: {counter404}")
            print(f"405: {counter405}")
            print(f"500: {counter500}")
except KeyboardInterrupt:
    print(f"File size: {filesSize}")
    print(f"200: {counter200}")
    print(f"401: {counter401}")
    print(f"403: {counter403}")
    print(f"404: {counter404}")
    print(f"405: {counter405}")
    print(f"500: {counter500}")