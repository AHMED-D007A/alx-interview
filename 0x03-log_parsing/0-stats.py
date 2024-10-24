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
    dec = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    try:
        for line in sys.stdin:
            text = line.split()
            if len(text) > 2:
                if text[-2] in dec:
                    dec[text[-2]] += 1
            else:
                continue
            filesSize += int(text[-1])
            i += 1
            if i == 10:
                i = 0
                print_stats(filesSize, dec)
    except Exception:
        pass
    finally:
        print_stats(filesSize, dec)
        raise