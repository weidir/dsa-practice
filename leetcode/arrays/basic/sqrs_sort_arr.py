from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        sqr_list = [num**2 for num in nums]
        sqr_list.sort()

        return sqr_list

if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    sol = Solution()
    ans = sol.sortedSquares(nums)
    print(ans)