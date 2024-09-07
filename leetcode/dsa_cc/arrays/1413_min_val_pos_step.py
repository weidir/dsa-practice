from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        # Get the running sum
        run_sum = 0
        min_run_sum = 0
        for val in nums:
            run_sum = run_sum + val
            if run_sum < min_run_sum:
                min_run_sum = run_sum
        if min_run_sum > 1:
            return 1
        else:
            return abs(min_run_sum) + 1

        

if __name__ == "__main__":

    sol = Solution()

    nums1 = [-3,2,-3,4,2]
    ans1 = sol.minStartValue(nums1)
    print(ans1)

    nums2 = [1,2]
    ans2 = sol.minStartValue(nums2)
    print(ans2)

    nums3 = [1,-2,-3]
    ans3 = sol.minStartValue(nums3)
    print(ans3)