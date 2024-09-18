from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return str(self.val)
    
    def linked_list(self):

        nodes = [self.val]
        curr = self.next

        while curr:

            nodes.append(curr.val)
            curr = curr.next
        
        return "-> ".join([str(node) for node in nodes])


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        print(head.linked_list(), "\n")

        if not head or not head.next or left == right:
            return head

        # Add buffer head to account for when left is 1
        buff_head = ListNode(None)
        buff_head.next = head
        
        curr = buff_head
        prev = None
        curr_pos = 0

        while curr and curr_pos <= right:

            if curr_pos >= left and curr_pos < right:
                print(f"Current node: {curr}; prev node: {prev}")
                next_node = curr.next
                print(f"Next node: {next_node}")
                curr.next = next_node.next
                print(f"Current node's next node set to: {curr.next}")
                next_node.next = prev.next
                print(f"Next node's next node set to: {next_node.next}")
                prev.next = next_node
                print(f"Previous node's next node set to: {prev.next}")

                print(buff_head.linked_list(), "\n")
            else:
                prev = curr
                curr = curr.next

            curr_pos += 1

        return buff_head.next


if __name__ == "__main__":
    sol = Solution()

    left1 = 2
    right1 = 4
    N1 = ListNode(1)
    N2 = ListNode(2)
    N3 = ListNode(3)
    N4 = ListNode(4)
    N5 = ListNode(5)
    N1.next = N2
    N2.next = N3
    N3.next = N4
    N4.next = N5

    ans1 = sol.reverseBetween(head=N1, left=left1, right=right1)
    assert ans1.val == 1

    N6 = ListNode(5)
    left2 = 1
    right2 = 1
    ans2 = sol.reverseBetween(head=N6, left=left2, right=right2)
    assert ans2.val == 5

    N7 = ListNode(3)
    N8 = ListNode(5)
    N7.next = N8
    left3 = 1
    right3 = 1
    ans3 = sol.reverseBetween(head=N7, left=left3, right=right3)
    assert ans3.val == 3

    N9 = ListNode(3)
    N10 = ListNode(5)
    N9.next = N10
    left4 = 1
    right4 = 2
    ans4 = sol.reverseBetween(head=N9, left=left4, right=right4)
    assert ans4.val == 5