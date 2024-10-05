from typing import List, Union, Tuple
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        # Start BFS from the entrance
        # Skip over adding walls to the queue

        m = len(maze)
        n = len(maze[0])

        # Function to check if coordinate is an exit or not
        def is_exit(coordinate: Union[List[int], Tuple[int]]) -> bool:
            x, y = coordinate[0], coordinate[1]
            if x == 0 or x == m - 1:
                return True
            elif y == 0 or y == n - 1:
                return True
            return False

        def is_valid(coordinate: Union[List[int], Tuple[int]]) -> bool:
            x, y = coordinate[0], coordinate[1]
            if (0 <= x <= m - 1) and (0 <= y <= n - 1) and (maze[x][y] == "."):
                return True
            return False

        seen = set()
        seen.add(tuple(entrance))
        self.distance = 0

        def bfs(entrance: List[int]):
            
            queue = deque([tuple(entrance)])

            while queue:

                for _ in range(len(queue)):

                    node = queue.popleft()

                    if is_exit(node):
                        if tuple(node) != tuple(entrance):
                            return self.distance

                    seen.add(tuple(node))
                    
                    x, y = node[0], node[1]
                    for adj in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)]:
                        if is_valid(adj) and tuple(adj) not in seen:
                            queue.append(adj)
                            seen.add(adj)
                    
                self.distance += 1
            
            return -1
        
        return bfs(entrance)


if __name__ == "__main__":
    sol = Solution()

    maze1 = [
        ["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]
    ]
    entrance1 = [1,2]
    ans1 = sol.nearestExit(maze1, entrance1)
    print(ans1)
    assert ans1 == 1

    maze2 = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance2 = [1,0]
    ans2 = sol.nearestExit(maze2, entrance2)
    print(ans2)
    assert ans2 == 2

    maze3 = [[".","+"]]
    entrance3 = [0,0]
    ans3 = sol.nearestExit(maze3, entrance3)
    print(ans3)
