from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs_min(self, root):

        # If root is None, we've reached a leaf where min depth subsequent branches is 0
        if not root:
            return 0

        # If left node is None, just compute depth of right branch
        if not root.left:
            return self.dfs_min(root.right) + 1
        
        # If right node is None, just compute length of left branch
        elif not root.right:
            return self.dfs_min(root.left) + 1

        # If both left and right nodes are present
        else:
            
            left_depth = self.dfs_min(root.left)
            right_depth = self.dfs_min(root.right)

            return min(left_depth, right_depth) + 1


    def minDepth(self, root: Optional[TreeNode]) -> int:

        return self.dfs_min(root)
        

if __name__ == "__main__":
    sol = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    ans1 = sol.minDepth(root1)
    print(f"Answer 1: {ans1}")
    assert ans1 == 2

    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    ans2 = sol.minDepth(root2)
    print(f"Answer 2: {ans2}")
    assert ans2 == 5