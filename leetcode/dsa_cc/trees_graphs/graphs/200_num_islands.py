from typing import List
from collections import defaultdict

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor is not None and neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        # Get the size of the grid
        m = len(grid)
        n = len(grid[0])

        # Initialize the graph
        graph = defaultdict(list)

        # Generate the graph from the given matrix
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    graph[(i, j)] = [
                        (i-1, j) if i > 0 and grid[i-1][j] == "1" else None,
                        (i, j+1) if j < n-1 and grid[i][j+1] == "1" else None,
                        (i+1, j) if i < m-1 and grid[i+1][j] == "1" else None,
                        (i, j-1) if j > 0 and grid[i][j-1] == "1" else None,
                    ]
        
        # Initialize number of islands to 0
        ans = 0
        seen = set()
        
        # Count the number of unique islands
        for node in graph:
            if node not in seen:
                ans += 1
                seen.add(node)
                dfs(node)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
    ]
    ans1 = sol.numIslands(grid1)
    print(ans1)

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    ans2 = sol.numIslands(grid2)
    print(ans2)
