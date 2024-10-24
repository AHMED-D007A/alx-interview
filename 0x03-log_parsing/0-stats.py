#!/usr/bin/python3
"""
log parsing
"""

import sys


def print_stats(files_size, dec):
    """
    print the stats
    """
    print(f"File size: {files_size}")
    for key in sorted(dec.keys()):
        if dec[key] != 0:
            print(f"{key}: {dec[key]}")

if __name__ == "__main__":
    """
    the script that reads stdin line by line and computes metrics
    """
    i = 0
    filesSize = 0
    dec = {'200': 0,
                   '301': 0,
                   '400': 0,
                   '401': 0,
                   '403': 0,
                   '404': 0,
                   '405': 0,
                   '500': 0}

    try:
        for line in sys.stdin:
            args = line.split(' ')
            if len(args) > 2:
                status_line = args[-2]
                file_size = args[-1]
                if status_line in dec:
                    dec[status_line] += 1
                filesSize += int(file_size)
                i += 1
                if i == 10:
                    print_stats(filesSize, dec)
                    i = 0
    except Exception:
        pass
    finally:
        print_stats(filesSize, dec)
