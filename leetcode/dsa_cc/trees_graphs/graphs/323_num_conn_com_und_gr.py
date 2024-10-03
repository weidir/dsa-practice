from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        seen = set()

        # Convert edges into graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)

        # Define dfs algo
        def dfs(node):
            
            neighbors = graph[node]
            # print(f"Neighbors: {neighbors}")

            for neighbor in neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        # Loop through nodes
        ans = 0
        for node in graph:
            # print(f"Node: {node}")
            # print(f"Seen: {seen}")
            if node not in seen:
                ans += 1
                seen.add(node)
                # print(f"Node not seen, incrementing answer to {ans}")
                dfs(node)
            # print(f"Answer: {ans}\n")
        
        return ans + (n - len(seen))
    

if __name__ == "__main__":
    sol = Solution()

    n1 = 5
    edges1 = [[0,1],[1,2],[3,4]]
    ans1 = sol.countComponents(n1, edges1)
    print(ans1)

    n2 = 5
    edges2 = [[0,1],[1,2],[2,3],[3,4]]
    ans2 = sol.countComponents(n2, edges2)
    print(ans2)