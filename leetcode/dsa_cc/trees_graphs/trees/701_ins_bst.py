from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        def dfs_bst_insert(node: TreeNode, val: int) -> None:
            
            if not node:
                return

            if val > node.val and node.right:
                dfs_bst_insert(node.right, val)
            elif val < node.val and node.left:
                dfs_bst_insert(node.left, val)
            elif val > node.val and not node.right:
                node.right = TreeNode(val)
            elif val < node.val and not node.left:
                node.left = TreeNode(val)
        
        dfs_bst_insert(root, val)

        return root
    

if __name__ == "__main__":
    sol = Solution()

    N1 = TreeNode(4)
    N2 = TreeNode(2)
    N3 = TreeNode(7)
    N4 = TreeNode(1)
    N5 = TreeNode(3)

    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5

    ans1 = sol.insertIntoBST(N1, 5)