from typing import List, Tuple
from collections import deque, defaultdict

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        graph = defaultdict(list)

        # Create an adjacency mapping from the grid
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    if i > 0 and grid[i-1][j] == 0:
                        graph[(i, j)].append((i-1, j)) # Up
                    if i > 0 and j < n-1 and grid[i-1][j+1] == 0:
                        graph[(i, j)].append((i-1, j+1)) # Up right
                    if j < n-1 and grid[i][j+1] == 0:
                        graph[(i, j)].append((i, j+1)) # Right 
                    if i < n-1 and j < n-1 and grid[i+1][j+1] == 0:
                        graph[(i, j)].append((i+1, j+1)) # Down right
                    if i < n-1 and grid[i+1][j] == 0:
                        graph[(i, j)].append((i+1, j)) # Down
                    if i < n-1 and j > 0 and grid[i+1][j-1] == 0:
                        graph[(i, j)].append((i+1, j-1)) # Down left
                    if j > 0 and grid[i][j-1] == 0:
                        graph[(i, j)].append((i, j-1)) # Left
                    if i > 0 and j > 0 and grid[i-1][j-1] == 0:
                        graph[(i, j)].append((i-1, j-1)) # Up left

        queue = deque([(0, 0)])
        self.shortest = 1

        # BFS
        def bfs(queue):

            while queue:
                for node in queue:
                    
                    if node == (n-1, n-1):
                        return self.shortest
                    
                    queue.append(node)
            
            return -1

        return bfs(queue)


if __name__ == "__main__":
    sol = Solution()

    grid1 = [[0,1],[1,0]]
    ans1 = sol.shortestPathBinaryMatrix(grid1)
    print(ans1)

    grid2 = [[0,0,0],[1,1,0],[1,1,0]]
    ans2 = sol.shortestPathBinaryMatrix(grid2)
    print(ans2)

    grid3 = [[1,0,0],[1,1,0],[1,1,0]]
    ans3 = sol.shortestPathBinaryMatrix(grid3)
    print(ans3)