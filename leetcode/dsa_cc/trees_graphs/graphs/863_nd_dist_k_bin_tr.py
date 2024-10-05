from typing import List
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # Create an adjacency matrix graph
        graph = defaultdict(list)
        def bfs_tree(root):

            queue = deque([root])

            while queue:

                for _ in range(len(queue)):

                    node = queue.popleft()

                    if node.val not in graph:
                        graph[node.val] = []

                    if node.left:
                        graph[node.val].append(node.left.val)
                        graph[node.left.val].append(node.val)
                        queue.append(node.left)
                    if node.right:
                        graph[node.val].append(node.right.val)
                        graph[node.right.val].append(node.val)
                        queue.append(node.right)
        
        bfs_tree(root)

        if target.val not in graph:
            return []

        # Perform BFS on the new graph
        self.distance = 0
        seen = set()
        def bfs_graph(target: TreeNode):

            queue = deque([target.val])

            while queue:

                if self.distance == k:
                    return list(queue)
                
                for _ in range(len(queue)):

                    node = queue.popleft()
                    seen.add(node)

                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            queue.append(neighbor)
                
                self.distance += 1
            
            return []
        
        return bfs_graph(target)


if __name__ == "__main__":
    sol = Solution()

    N1 = TreeNode(3)
    N2 = TreeNode(5)
    N3 = TreeNode(1)
    N4 = TreeNode(6)
    N5 = TreeNode(2)
    N6 = TreeNode(0)
    N7 = TreeNode(8)
    N8 = TreeNode(7)
    N9 = TreeNode(4)

    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    N5.left = N8
    N5.right = N9
    N3.left = N6
    N3.right = N7

    target1 = TreeNode(5)
    k1 = 2
    ans1 = sol.distanceK(N1, target1, k1)
    print(ans1)

    N10 = TreeNode(1)
    target2 = TreeNode(1)
    k2 = 3
    ans2 = sol.distanceK(N10, target2, k2)
    print(ans2)

    N11 = TreeNode(0)
    N12 = TreeNode(1)
    N13 = TreeNode(2)
    N14 = TreeNode(3)
    N15 = TreeNode(4)

    N11.left = N12
    N12.right = N13
    N13.right = N14
    N14.right = N15

    target3 = TreeNode(3)
    k3 = 0
    ans3 = sol.distanceK(N11, target3, k3)
    print(ans3)
