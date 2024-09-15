from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast.next:
            slow = slow.next
            if fast.next.next is not None:
                fast = fast.next.next
            else:
                fast = fast.next
        
        return slow

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 1
        node_list = []
        node = head
        while node:
            if node.next:
                size += 1
            node_list.append(node)

            node = node.next
            
        return node_list[size // 2]


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

    ans1 = sol.middleNode(head=N1)
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

    ans2 = sol.middleNode(head=N6)
    print(ans2.val)
