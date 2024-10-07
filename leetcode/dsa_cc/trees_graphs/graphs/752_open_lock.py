from typing import List, Tuple
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        seen = set(deadends)

        if "0000" in deadends:
            return -1
        
        def get_neighbors(curr):
            neighbors = []
            for i in range(len(curr)):
                up = (int(curr[i]) + 1) % 9
                down = (int(curr[i]) - 1) if int(curr[i]) != 0 else 9
                new_up = curr[:i] + str(up) + curr[i+1:]
                new_down = curr[:i] + str(down) + curr[i+1:]
                neighbors.extend([new_up, new_down])
            
            return neighbors
        
        start = ("0000", 0)

        def bfs(start: Tuple[str, int]) -> int:

            queue = deque([start])

            while queue:

                code, steps = queue.popleft()

                if code == target:
                    return steps

                if code not in seen:
                    for neighbor in get_neighbors(code):
                        queue.append((neighbor, steps+1))
                
                seen.add(code)
                    
            return -1
        
        return bfs(start)


if __name__ == "__main__":
    sol = Solution()

    deadends1 = ["0201","0101","0102","1212","2002"]
    target1 = "0202"
    ans1 = sol.openLock(deadends1, target1)
    print(ans1)

    deadends2 = ["8888"]
    target2 = "0009"
    ans2 = sol.openLock(deadends2, target2)
    print(ans2)

    deadends3 = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target3 = "8888"
    ans3 = sol.openLock(deadends3, target3)
    print(ans3)
    