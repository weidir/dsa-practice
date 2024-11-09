from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            print(f"Left: {l} - right: {r} - mid: {mid}")

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
            
            print(f"Left: {l} - right: {r}\n")
        
        return l
    

if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,3,5,6]
    target1 = 5
    ans1 = sol.searchInsert(nums1, target1)
    print(ans1)