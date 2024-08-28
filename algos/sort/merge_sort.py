from typing import Tuple

def merge_sort(list: list) -> list:
    """
    Implements the merge sort algorithm by sorting a given list in ascending order and returns a new sort list
    Steps:
    - Divide: Find the midpoint of the given list and divide into sublists
    - Conquer: Recursively sort the sublists
    - Combine: Merge the sorted sublists
    """

    if len(list) <= 1:
        return list
    
    left, right = split(list)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def split(list: list) -> Tuple[list]:
    """
    Splits a given list in half on the midpoint into two sublists
    """

    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right
    

def merge(left: list, right: list) -> list:
    """
    """