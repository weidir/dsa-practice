from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs_min(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right:
            return root.val
        
        if not root.right:
            left_max = self.dfs_min(root.left)
            return min(left_max, root.val)
        
        elif not root.left:
            right_max = self.dfs_min(root.right)
            return min(right_max, root.val)

        else:
            left_max = self.dfs_min(root.left)
            right_max = self.dfs_min(root.right)

            return min(left_max, right_max, root.val)


    def dfs_max(self, root: Optional[TreeNode]) -> int:
        
        if not root.left and not root.right:
            return root.val
        
        if not root.right:
            left_max = self.dfs_max(root.left)
            return max(left_max, root.val)
        
        elif not root.left:
            right_max = self.dfs_max(root.right)
            return max(right_max, root.val)

        else:
            left_max = self.dfs_max(root.left)
            right_max = self.dfs_max(root.right)

            return max(left_max, right_max, root.val)


    def dfs_min_iter(self, root: Optional[TreeNode]) -> int:

        stack = [root]
        min_val = None

        while stack:

            top = stack.pop()

            if min_val is None:
                min_val = top.val
            elif top.val < min_val:
                min_val = top.val

            if top.right:
                stack.append(top.right)

            if top.left:
                stack.append(top.left)
        
        return min_val    

    def dfs_max_iter(self, root: Optional[TreeNode]) -> int:

        stack = [root]
        max_val = None

        while stack:

            top = stack.pop()

            if max_val is None:
                max_val = top.val
            elif top.val > max_val:
                max_val = top.val

            if top.right:
                stack.append(top.right)

            if top.left:
                stack.append(top.left)
        
        return max_val
        

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        def max_min_helper(node, mx, mn):

            if not node:
                return
            
            # Update result
            self.result = max(
                self.result,
                abs(node.val - mx),
                abs(node.val - mn)
            )

            # Update max and min values
            mx = max(mx, node.val)
            mn = min(mn, node.val)

            max_min_helper(node.left, mx, mn)
            max_min_helper(node.right, mx, mn)
        
        self.result = 0
        mx = root.val
        mn = root.val

        max_min_helper(node=root, mx=mx, mn=mn)

        return self.result

        
if __name__ == "__main__":
    sol = Solution()

    N1 = TreeNode(8)
    N2 = TreeNode(3)
    N3 = TreeNode(1)
    N4 = TreeNode(6)
    N5 = TreeNode(4)
    N6 = TreeNode(7)
    N7 = TreeNode(10)
    N8 = TreeNode(14)
    N9 = TreeNode(13)
    N1.left = N2
    N1.right = N7
    N2.left = N3
    N2.right = N4
    N4.left = N5
    N4.right = N6
    N7.right = N8
    N8.right = N9

    min_val = sol.dfs_min(N1)
    print(min_val)
    min_val_iter = sol.dfs_min_iter(N1)
    print(min_val_iter)
    max_val = sol.dfs_max(N1)
    print(max_val)
    max_val_iter = sol.dfs_max_iter(N1)
    print(max_val_iter)

    max_diff = sol.maxAncestorDiff(N1)
    print(f"Max difference: {max_diff}")