from typing import Tuple
from random import randint

# Overall linear time complexity: O(n)
# Overal linear space complexity: O(n)
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

# Logarithmic time complexity: O(log n)
# However in python list slicing takes place in O(k) where k is the length of the slice
# So techincally this takes place in O(klog n) time
def split(list: list) -> Tuple[list]:
    """
    Splits a given list in half on the midpoint into two sublists
    """

    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right
    
# O(n log n) time complexity, 
def merge(left: list, right: list) -> list:
    """
    Merge two lists (arrays), sorting them in the process
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        elif left[i] > right[j]:
            l.append(right[j])
            j += 1
        elif left[i] == right[j]:
            l.append(left[i])
            l.append(right[j])
            i += 1
            j += 1
    
    # Account for left list being longer than right list
    while i < len(left):
        l.append(left[i])
        i += 1
    
    # Account for right list being longer than left list
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

# Linear time complexity: O(n)
def verify_sorted(list):

    if len(list) in [0, 1]:
        return True
    
    return list[0] <= list[1] and verify_sorted(list[1:])


if __name__ == "__main__":

    alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
    blist = [randint(0, 500) for _ in range(500)]
    asort = merge_sort(alist)
    bsort = merge_sort(blist)
    
    assert verify_sorted(asort)
    assert verify_sorted(bsort)
    print("All checks passed")
