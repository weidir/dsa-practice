from typing import List
from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        graph = defaultdict(list)
        restricted = set(restricted)
        seen = set([0])
        self.count = 1

        # Convert edges to graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
    
        # Depth-first search
        def dfs(node):

            neighbors = graph[node]
            # print(f"Node: {node}")
            # print(f"Neighbors: {neighbors}")
            # print(f"Count: {self.count}\n")

            for neighbor in neighbors:
                if neighbor not in seen and neighbor not in restricted:
                    self.count += 1
                    seen.add(neighbor)
                    dfs(neighbor)
            
        dfs(0)

        return self.count


if __name__ == "__main__":
    sol = Solution()

    n1 = 7
    edges1 = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted1 = [4,5]
    ans1 = sol.reachableNodes(n1, edges1, restricted1)
    print(ans1)

    n2 = 7
    edges2 = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
    restricted2 = [4,2,1]
    ans2 = sol.reachableNodes(n2, edges2, restricted2)
    print(ans2)