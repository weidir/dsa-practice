from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        l = r = counter = 0
        product = 1

        if k <= 1:
            return 0

        while r < n:
            product *= nums[r]

            while product >= k:
                product //= nums[l]
                l += 1
            
            counter += 1 + (r - l)
            r += 1

        return counter


if __name__ == "__main__":
    sol = Solution()

    nums1 = [10,5,2,6]
    k1 = 100
    ans1 = sol.numSubarrayProductLessThanK(nums1, k1)

    nums2 = [1,2,3]
    k2 = 0
    ans2 = sol.numSubarrayProductLessThanK(nums2, k2)
    print(ans1, ans2)