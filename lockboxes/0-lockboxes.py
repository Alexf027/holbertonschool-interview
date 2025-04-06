#!/usr/bin/python3
"""
Module that defines canUnlockAll function to determine
if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): Each box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened = set([0])  # we start with box 0 opened
    keys = set(boxes[0])  # keys we have

    while keys:
        key = keys.pop()
        if key < n and key not in opened:
            opened.add(key)
            keys.update(boxes[key])  # add new keys from the opened box

    return len(opened) == n
