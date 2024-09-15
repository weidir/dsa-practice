from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node(val={self.val})"

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        curr = head.next
        prev = head

        while curr:
            print(f"Current node: {curr}")
            print(f"Previous node: {prev}")

            if curr.val == prev.val:
                print(f"Current and previous node had same value, removing current node")
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return head


if __name__ == "__main__":
    sol = Solution()

    N1 = ListNode(1)
    N2 = ListNode(2)
    N3 = ListNode(3)
    N4 = ListNode(4)
    N5 = ListNode(5)
    N1.next = N2
    N2.next = N3
    N3.next = N4
    N4.next = N5

    ans1 = sol.deleteDuplicates(head=N1)
    print(ans1.val)

    N6 = ListNode(1)
    N7 = ListNode(2)
    N8 = ListNode(3)
    N9 = ListNode(4)
    N10 = ListNode(5)
    N11 = ListNode(6)
    N6.next = N7
    N7.next = N8
    N8.next = N9
    N9.next = N10
    N10.next = N11

    ans2 = sol.deleteDuplicates(head=N6)
    print(ans2.val)

    N12 = ListNode(1)
    N13 = ListNode(1)
    N14 = ListNode(1)
    N12.next = N13
    N13.next = N14

    ans3 = sol.deleteDuplicates(head=N12)
    print(ans3.val)

    N15 = ListNode(1)
    N16 = ListNode(1)
    N17 = ListNode(2)
    N18 = ListNode(3)
    N19 = ListNode(3)
    N15.next = N16
    N16.next = N17
    N17.next = N18
    N18.next = N19

    ans4 = sol.deleteDuplicates(head=N15)
    print(ans4.val)