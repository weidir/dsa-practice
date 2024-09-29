from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if not root:
            return root
        
        self.closest = root.val
        self.closest_dist = abs(target - root.val)
        
        def dfs_close_helper(root: TreeNode, target: float) -> int:

            if not root:
                return
            
            current_dist = abs(target - root.val)
            
            if current_dist < self.closest_dist:
                self.closest_dist = current_dist
                self.closest = root.val
            elif current_dist == self.closest_dist:
                self.closest = min(root.val, self.closest)
            
            if root.left:
                dfs_close_helper(root.left, target)
            if root.right:
                dfs_close_helper(root.right, target)

            return self.closest

        return dfs_close_helper(root, target)


if __name__ == "__main__":
    sol = Solution()

    N1 = TreeNode(4)
    N2 = TreeNode(2)
    N3 = TreeNode(5)
    N4 = TreeNode(1)
    N5 = TreeNode(3)

    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    
    ans1 = sol.closestValue(N1, 3.714286)
    print(f"Answer 1: {ans1}")