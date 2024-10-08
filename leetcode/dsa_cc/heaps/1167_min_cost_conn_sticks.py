from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        # Create a heap of sticks
        heapq.heapify(sticks)
        
        cost = 0

        while len(sticks) > 1:
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)

            new_stick = stick1 + stick2

            cost += new_stick

            heapq.heappush(sticks, new_stick)
        
        return cost


if __name__ == "__main__":
    sol = Solution()

    sticks1 = [2,4,3]
    ans1 = sol.connectSticks(sticks1)
    print(ans1)

    sticks2 = [1,8,3,5]
    ans2 = sol.connectSticks(sticks2)
    print(ans2)