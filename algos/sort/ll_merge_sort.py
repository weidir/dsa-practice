# Implementation of merge sort algorithm on a linked list\

# Update python path to make sure imports work from other folders
# Make sure the run this script from the root directory of the repository
from typing import Tuple
import os
import sys
sys.path.insert(0, os.getcwd())

# Import LinkedList implementation
from structs.linked_list import LinkedList, Node

# Runs in (kn log n) time
def merge_sort(linked_list: LinkedList) -> LinkedList:

    if linked_list.size() <= 1:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

# Quasi logarithmic time complexity: O(k log n)
def split(linked_list: LinkedList) -> Tuple[LinkedList]:

    if linked_list is None or linked_list.head is None:
        return linked_list, None

    midpoint = linked_list.size() // 2
    midpoint_node = linked_list.index(midpoint - 1)
    left = linked_list
    right = LinkedList(head=midpoint_node.next_node)
    midpoint_node.next_node = None
    left.tail = midpoint_node
    right.find_tail()

    return left, right

# Runs in linear time: O(n)
def merge(left_ll: LinkedList, right_ll: LinkedList) -> LinkedList:

    merged = LinkedList()
    merged.head = Node(data=0)
    current = merged.head

    left_head = left_ll.head
    right_head = right_ll.head

    while left_head or right_head:
        # If left head node is None, we've traversed the full left LL
        if left_head is None:
            current.next_node = right_head
            # Call next on right to get to stopping condition
            right_head = right_head.next_node
        # If right head node is None, we've traversed the full right LL
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        # Not at either tail node
        else:
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        
        # Increment the current node forward
        current = current.next_node

    # Remove the fake head
    merged.head = merged.head.next_node
    
    return merged


if __name__ == "__main__":
    N1 = Node(data=1, name="N1")
    N2 = Node(data=25, name="N2")
    N3 = Node(data=5, name="N3")
    N4 = Node(data=50, name="N4")
    N5 = Node(data=20, name="N5")
    N6 = Node(data=15, name="N6")
    N7 = Node(data=73, name="N7")
    N8 = Node(data=47, name="N8")
    N9 = Node(data=156, name="N9")
    N10 = Node(data=11, name="N10")
    N11 = Node(data=271, name="N11")
    N12 = Node(data=92, name="N12")

    allist = LinkedList()
    allist.append(N1)
    allist.append(N2)
    allist.append(N3)
    allist.append(N4)
    allist.append(N5)
    allist.append(N6)

    bllist = LinkedList()
    bllist.append(N7)
    bllist.append(N8)
    bllist.append(N9)
    bllist.append(N10)
    bllist.append(N11)
    bllist.append(N12)

    assert allist.size() == 6
    assert allist.head == N1
    assert allist.tail == N6

    left, right = split(allist)

    assert left.size() == 3
    assert right.size() == 3
    assert left.head.data == 1
    assert left.tail.data == 5
    assert right.head.data == 50
    assert right.tail.data == 15

    sllist = merge_sort(bllist)
    print(f"Sorted linked list: {sllist}")

    assert sllist.size() == 6
    assert sllist.index(0).data == 11

    print("All checks passed")
