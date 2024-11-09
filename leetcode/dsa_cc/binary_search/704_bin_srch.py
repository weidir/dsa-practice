from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]

            if val == target:
                return mid
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    ans1 = sol.search(nums1, target1)
    print(ans1)

    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    ans2 = sol.search(nums2, target2)
    print(ans2)

    nums3 = [5]
    target3 = 5
    ans3 = sol.search(nums3, target3)
    print(ans3)

    nums4 = [5]
    target4 = -5
    ans4 = sol.search(nums4, target4)
    print(ans4)