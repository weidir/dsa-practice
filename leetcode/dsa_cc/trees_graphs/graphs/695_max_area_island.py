from typing import List
from collections import defaultdict

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        graph = defaultdict(list)

        # Convert grid to graph
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    graph[(i, j)] = []
                    if i > 0 and grid[i-1][j] == 1:
                        graph[(i,j)].append((i-1, j)) # Up
                    if j < n-1 and grid[i][j+1] == 1:
                        graph[(i,j)].append((i, j+1)) # Right
                    if i < m-1 and grid[i+1][j] == 1:
                        graph[(i,j)].append((i+1, j)) # Down
                    if j > 0 and grid[i][j-1] == 1:
                        graph[(i,j)].append((i, j-1)) # Left
        
        # Depth first search
        def dfs(node):
            
            neighbors = graph[node]

            for neighbor in neighbors:
                if neighbor not in island_seen:
                    island_seen.add(neighbor)
                    dfs(neighbor)

        seen = set()
        ans = 0
        for node in graph:
            island_seen = set()
            if node not in seen:
                island_seen.add(node)
                dfs(node)
            
            if len(island_seen) > ans:
                ans = len(island_seen)

            seen.union(island_seen)
        
        return ans
                

if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    ans1 = sol.maxAreaOfIsland(grid1)
    print(ans1)

    grid2 = [[0,0,0,0,0,0,0,0]]
    ans2 = sol.maxAreaOfIsland(grid2)
    print(ans2)

    grid3 = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
    ]
    ans3 = sol.maxAreaOfIsland(grid3)
    print(ans3)