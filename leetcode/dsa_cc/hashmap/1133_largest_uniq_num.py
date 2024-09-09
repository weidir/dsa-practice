from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        counts = {}
        for val in nums:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

        nums.sort(reverse=True)
        
        for val in nums:
            if counts[val] == 1:
                return val
            
        return -1

if __name__ == "__main__":
    sol = Solution()

    nums1 = [5,7,3,9,4,9,8,3,1]
    ans1 = sol.largestUniqueNumber(nums1)
    print(ans1)

    nums2 = [9,9,8,8]
    ans2 = sol.largestUniqueNumber(nums2)
    print(ans2)