from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
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
    N1 = ListNode(val=10)
    N2 = ListNode(val=20)
    N3 = ListNode(val=30)
    # N1.next = N2
    # N2.next = N3

    sol = Solution()
    print(sol.middleNode(head=N1).val)
        