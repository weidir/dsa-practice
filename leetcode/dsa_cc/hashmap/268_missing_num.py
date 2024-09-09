from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums_all_set = set(range(len(nums) + 1))
        nums_set = set(nums)

        missing = nums_all_set.difference(nums_set)

        return missing.pop() if missing else None

if __name__ == "__main__":
    sol = Solution()

    nums1 = [3, 0, 1]
    ans1 = sol.missingNumber(nums1)
    print(ans1)