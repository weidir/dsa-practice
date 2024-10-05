from typing import List, Tuple
from collections import deque, defaultdict

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        graph = defaultdict(list)

        if n == 0 or grid[0][0] != 0:
            return -1

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

        self.shortest = 0
        self.seen = set()

        # BFS
        def bfs(node):

            queue = deque([node])

            while queue:

                self.shortest += 1

                num_nds_lvl = len(queue)

                for _ in range(num_nds_lvl):

                    node = queue.popleft()

                    if node not in self.seen:
                        self.seen.add(node)

                        if node == (n - 1, n - 1):
                            return self.shortest

                        if node in graph:
                            queue.extend(graph[node])
                                            
            return -1

        return bfs((0,0))


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

    grid4 = [
        [0,0,0],
        [1,1,0],
        [1,1,1]
    ]
    ans4 = sol.shortestPathBinaryMatrix(grid4)
    print(ans4)