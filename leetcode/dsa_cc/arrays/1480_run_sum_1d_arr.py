from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        run_sum = 0
        run_sum_list = []
        for num in nums:
            run_sum = run_sum + num
            run_sum_list.append(run_sum)

        return run_sum_list

if __name__ == "__main__":
    nums = [1,2,3,4]

    sol = Solution()
    ans = sol.runningSum(nums)
    print(ans)