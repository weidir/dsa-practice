from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        # If a given row of nodes has no children, sum those nodes
        
        queue = deque([root])

        while queue:

            num_nodes_lvl = len(queue)
            sum_lvl = 0
            num_child_lvl = 0

            for i in range(num_nodes_lvl):

                node = queue.popleft()
                sum_lvl += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

        return sum_lvl


if __name__ == "__main__":
    sol = Solution()

    N1 = TreeNode(1)
    N2 = TreeNode(2)
    N3 = TreeNode(3)
    N4 = TreeNode(4)
    N5 = TreeNode(5)
    N6 = TreeNode(6)
    N7 = TreeNode(7)
    N8 = TreeNode(8)

    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    N3.right = N6
    N4.left = N7
    N6.right = N8

    ans1 = sol.deepestLeavesSum(N1)
    print(ans1)