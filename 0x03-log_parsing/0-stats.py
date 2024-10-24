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
            filesSize += int(text[-1])
            if text[-2] == "200":
                dec["200"] += 1
            if text[-2] == "301":
                dec["301"] += 1
            if text[-2] == "400":
                dec["400"] += 1
            if text[-2] == "401":
                dec["401"] += 1
            if text[-2] == "403":
                dec["403"] += 1
            if text[-2] == "404":
                dec["404"] += 1
            if text[-2] == "405":
                dec["405"] += 1
            if text[-2] == "500":
                dec["500"] += 1
            i += 1
            if i == 10:
                i = 0
                print_stats(filesSize, dec)
    except Exception:
        pass
    except KeyboardInterrupt:
        print_stats(filesSize, dec)
        raise
