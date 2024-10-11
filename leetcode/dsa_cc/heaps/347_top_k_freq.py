from typing import List
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Get frequencies of each number in the list
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # Push onto heap with frequency first
        heap = []
        for num, frequency in freq.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [freq_num[1] for freq_num in heap]

if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,1,1,2,2,3]
    k1 = 2
    ans1 = sol.topKFrequent(nums1, k1)
    print(ans1)