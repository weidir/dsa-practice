from typing import List
from math import sqrt
from collections import defaultdict
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist_orig(point: List[int]) -> float:
            return round(sqrt(point[0]**2 + point[1]**2), 1)
        
        heap = []
        for point in points:
            dist = dist_orig(point)
            heapq.heappush(heap, (-dist, point))

            if len(heap) > k:
                heapq.heappop(heap)
            
        return [item[1] for item in heap]

        
if __name__ == "__main__":
    sol = Solution()

    points1 = [[1,3],[-2,2]]
    k1 = 1
    ans1 = sol.kClosest(points1, k1)
    print(ans1)

    points2 = [[3,3],[5,-1],[-2,4]]
    k2 = 2
    ans2 = sol.kClosest(points2, k2)
    print(ans2)
