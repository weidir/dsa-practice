from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check_divisor(divisor: int, nums: List[int], threshold: int) -> bool:
            div_list = [ceil(num / divisor) for num in nums]
            val = sum(div_list)
            check = val <= threshold
            print(f"Divisor check result: {round(val, 1)} --> val <= threshold: {check}")
            return check
    
        l = 1
        r = max(nums)

        while l <= r:
            mid = (l + r) // 2
            print(f"Left: {l} - Right: {r} - Mid: {mid}")

            if check_divisor(mid, nums, threshold):
                r = mid - 1
            else:
                l = mid + 1
            print(f"New left: {l} - new right: {r}\n")
        
        return l


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,2,5,9]
    threshold1 = 6
    ans1 = sol.smallestDivisor(nums1, threshold1)
    print(ans1)

    nums2 = [44,22,33,11,1]
    threshold2 = 5
    ans2 = sol.smallestDivisor(nums2, threshold2)
    print(ans2)
            