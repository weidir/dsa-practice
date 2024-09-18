from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        nodes = [self.val]
        curr = self.next
        while curr is not None:
            nodes.append(curr.val)
            curr = curr.next

        return "-> ".join([str(node) for node in nodes])

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        print("\n")

        if not head or not head.next or left == right:
            return head
        
        # Add buffer head node
        buff_head = ListNode(None)
        buff_head.next = head
        
        curr = buff_head
        prev = None
        curr_pos = 0
        left_node = None
        right_node = None
        left_node_prev = None
        right_node_prev = None

        while curr and curr_pos <= right:

            if curr_pos == left:
                left_node = curr
                left_node_prev = prev

            if curr_pos == right:
                right_node = curr
                right_node_prev = prev

            prev = curr
            curr = curr.next
            curr_pos += 1
        
        print(f"Left node: {left_node.val if left_node else None}; node before left: {left_node_prev.val if left_node_prev else None}")
        print(f"Right node: {right_node.val if right_node else None}; node before right: {right_node_prev.val if right_node_prev else None}")
        
        # Switch the left and right nodes
        if right - left > 1:

            # Switch the previous left and right nodes
            if left_node_prev:
                print(f"Updating the next node of the left node's previous node")
                left_node_prev.next = right_node
            if right_node_prev:
                print(f"Updating the next node of the right node's previous node")
                right_node_prev.next = left_node

            print(f"Nodes to switch aren't next to each other")
            left_next_node = left_node.next
            left_node.next = right_node.next
            right_node.next = left_next_node

        else:
            print(f"Nodes to switch are next to each other")
            print(f"Left node: {left_node.val}; left next node: {left_node.next.val if left_node.next else None}")
            print(f"Right node {right_node.val}; right next node: {right_node.next.val if right_node.next else None}")

            # Switch the previous left and right nodes
            if left_node_prev:
                print(f"Updating the next node of the left node's previous node")
                left_node_prev.next = right_node
            right_node_next = right_node.next
            right_node.next = left_node
            left_node.next = right_node_next

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
    print(ans1)
    assert ans1.val == 1

    N6 = ListNode(5)
    left2 = 1
    right2 = 1
    ans2 = sol.reverseBetween(head=N6, left=left2, right=right2)
    print(ans2)
    assert ans2.val == 5

    N7 = ListNode(3)
    N8 = ListNode(5)
    N7.next = N8
    left3 = 1
    right3 = 1
    ans3 = sol.reverseBetween(head=N7, left=left3, right=right3)
    print(ans3)
    assert ans3.val == 3

    N9 = ListNode(3)
    N10 = ListNode(5)
    N9.next = N10
    left4 = 1
    right4 = 2
    ans4 = sol.reverseBetween(head=N9, left=left4, right=right4)
    print(ans4)
    assert ans4.val == 5