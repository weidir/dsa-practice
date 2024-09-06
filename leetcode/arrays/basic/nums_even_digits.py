from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        for num in nums:
            str_val = str(num)
            if len(str_val) % 2 == 0:
                count += 1
        
        return count

if __name__ == "__main__":
    nums = [12,345,2,6,7896]
    sol = Solution()
    ans = sol.findNumbers(nums)
    print(ans)