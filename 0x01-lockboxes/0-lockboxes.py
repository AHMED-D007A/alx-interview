#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def canUnlockAll(boxes):
    """
    return True if all boxes is unlocked False otherwise.
    """
    keys = [0]
    openedBoxes = []
    closedBoxes = [i for i in range(len(boxes))]
    while len(keys) != 0 and len(openedBoxes) != len(boxes):
        for keyinhand in keys:
            if keyinhand in closedBoxes:
                openedBoxes.append(keyinhand)
                closedBoxes.remove(keyinhand)
            for keyinbox in boxes[keyinhand]:
                if keyinbox not in keys and keyinbox in closedBoxes:
                    keys.append(keyinbox)
        keys.remove(keyinhand)
    return len(openedBoxes) == len(boxes)
