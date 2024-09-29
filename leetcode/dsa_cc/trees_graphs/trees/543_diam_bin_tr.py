from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree_1(self, root: Optional[TreeNode]) -> int:
        
        # For any given node, find the longest paths on either side
        # Sum those paths together
        # Keep track of the maximum value seen

        self.max_len = 0

        def longest_path(root: Optional[TreeNode]) -> int:
            print(f"Node: {root.val} - max length: {self.max_len}")
            
            if not root.right and not root.left:
                # print(f"Reached leaf node")
                return 0
            
            if not root.right and root.left:
                longest_left = longest_path(root.left) + 1
                # print(f"Longest left path: {longest_left}")
                self.max_len = max(self.max_len, longest_left)
                return longest_left
            
            elif not root.left and root.right:
                longest_right = longest_path(root.right) + 1
                # print(f"Longest right path: {longest_right}")
                self.max_len = max(self.max_len, longest_right)
                return longest_right
            
            elif root.left and root.right:
                longest_left = longest_path(root.left) + 1
                longest_right = longest_path(root.right) + 1
                # print(f"Longest left path: {longest_left} - longest right path: {longest_right}")
                max_path = longest_left + longest_right
                # print(f"Max path: {max_path}")

                self.max_len = max(self.max_len, max_path)

                return max(longest_left, longest_right)
        
        longest_path(root)
    
        return self.max_len
    
    def diameterOfBinaryTree_2(self, root: Optional[TreeNode]) -> int:

        def max_depth(node: TreeNode) -> int:

            if not node:
                return 0
            
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)

            return 1 + max(left_depth, right_depth)

        return max_depth(root.left) + max_depth(root.right)


if __name__ == "__main__":
    sol = Solution()

    N1 = TreeNode(1)
    N2 = TreeNode(2)
    N3 = TreeNode(4)
    N4 = TreeNode(5)
    N5 = TreeNode(3)

    N1.left = N2
    N1.right = N5
    N2.left = N3
    N2.right = N4

    ans1_1 = sol.diameterOfBinaryTree_1(N1)
    ans1_2 = sol.diameterOfBinaryTree_2(N1)
    print(ans1_1)
    print(ans1_2)

    N1.left = N2
    N1.right = None
    N2.left = N2.right = None

    ans2 = sol.diameterOfBinaryTree_1(N1)
    print(ans2)