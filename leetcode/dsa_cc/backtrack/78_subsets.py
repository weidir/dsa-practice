from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr: List[int], idx: int) -> None:

            print(f"Current: {curr} - Index: {idx}")

            # Base case
            if idx > len(nums):
                return
            
            ans.append(curr[:])
            print(f"Answer: {ans}")
            for ii in range(idx, len(nums)):
                if nums[ii] not in curr:
                    curr.append(nums[ii])
                    backtrack(curr, ii + 1)
                    curr.pop()
        
        ans = []
        backtrack([], 0)
        return ans


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,2,3]
    ans1 = sol.subsets(nums1)
    print(ans1)