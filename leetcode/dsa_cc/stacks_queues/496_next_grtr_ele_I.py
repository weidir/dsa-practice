from typing import List
from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        next_greatest = {val: None for val in nums1}

        # For each value in nums1, traverse the nums2 list from back to front
        # until you find the value in nums1 you are concerned about
        # As you loop through, if the value is great than the nums1 value of interest
        # update the hashmap with that index
        


if __name__ == "__main__":
    sol = Solution()

    numsA1 = [4,1,2]
    numsB1 = [1,3,4,2]
    ans1 = sol.nextGreaterElement(numsA1, numsB1)
    print(f"Answer 1: {ans1}")
    # assert ans1 == [-1,3,-1]

    numsA2 = [2,4]
    numsB2 = [1,2,3,4]
    ans2 = sol.nextGreaterElement(numsA2, numsB2)
    print(f"Answer 2: {ans2}")
    # assert ans2 == [3,-1]