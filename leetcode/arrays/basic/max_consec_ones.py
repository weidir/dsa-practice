from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current = 0
        max = 0

        for num in nums:
            if num == 1:
                current += 1
            else:
                current = 0
            
            if current > max:
                max = current
        
        return max
        

if __name__ == "__main__":
    test_list = [1, 1, 0, 1, 1]
    sol = Solution()
    ans = sol.findMaxConsecutiveOnes(test_list)
    print(ans)