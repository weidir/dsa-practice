from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        lvl = 0
        ans_list = []

        while queue:
            
            num_nodes_lvl = len(queue)
            lvl_list = []

            for _ in range(num_nodes_lvl):

                node = queue.popleft()

                if lvl % 2 == 0:
                    lvl_list.append(node.val)
                else:
                    lvl_list = [node.val] + lvl_list

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            ans_list.append(lvl_list)
            lvl += 1
            
        return ans_list
    

if __name__ == "__main__":
    sol = Solution()

    N1 = TreeNode(3)
    N2 = TreeNode(9)
    N3 = TreeNode(20)
    N4 = TreeNode(15)
    N5 = TreeNode(7)

    N1.left = N2
    N1.right = N3
    N3.left = N4
    N3.right = N5

    ans1 = sol.zigzagLevelOrder(N1)
    print(ans1)