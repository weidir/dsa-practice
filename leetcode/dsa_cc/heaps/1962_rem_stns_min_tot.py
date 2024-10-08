from typing import List
import heapq
from math import floor

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        # Create a max heap from the list of piles
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            pile = heapq.heappop(piles)
            half_pile = floor(pile / 2)
            heapq.heappush(piles, half_pile)
        
        return abs(sum(piles))


if __name__ == "__main__":
    sol = Solution()

    piles1 = [5,4,9]
    k1 = 2
    ans1 = sol.minStoneSum(piles1, k1)
    print(ans1)

    piles2 = [4,3,6,7]
    k2 = 3
    ans2 = sol.minStoneSum(piles2, k2)
    print(ans2)