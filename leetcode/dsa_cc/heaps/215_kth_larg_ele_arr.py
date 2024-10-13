from typing import List
import heapq

class Solution:
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        
        heap = []
        for num in nums:
            # print(f"Num: {num}")
            heapq.heappush(heap, num)
            # print(f"Heap: {heap}")

            if len(heap) > k:
                pop = heapq.heappop(heap)
                # print(f"Popped off: {pop}")

        return heap[0]


    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        print(nums)

        return nums[-k] if len(nums) >= k else 0


if __name__ == "__main__":
    sol = Solution()

    nums1 = [3,2,1,5,6,4]
    k1 = 2
    ans1_h = sol.findKthLargest_heap(nums1, k1)
    ans1_s = sol.findKthLargest_sort(nums1, k1)
    print(ans1_h)
    print(ans1_s)

    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    ans2_h = sol.findKthLargest_heap(nums2, k2)
    ans2_s = sol.findKthLargest_sort(nums2, k2)
    print(ans2_h)
    print(ans2_s)
