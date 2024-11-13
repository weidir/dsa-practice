from typing import List

class Solution:
    def moveZeroesNaive(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ans = []
        zeros_seen = 0

        for num in nums:
            if num != 0:
                ans.append(num)
            else:
                zeros_seen += 1
        
        ans.extend([0] * zeros_seen)
        nums[:] = ans

    def moveZeroesOptimal(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_len = len(nums)

        l = 0
        r = 1

        while r < nums_len:
            if nums[r] != 0:
                while nums[l] != 0 and l < r:
                    l += 1
                l_val = nums[l]
                nums[l] = nums[r]
                nums[r] = l_val

                r += 1
                l += 1
            else:
                r += 1
                

if __name__ == "__main__":
    sol = Solution()

    nums1 = [0,1,0,3,12]
    # sol.moveZeroesOptimal(nums1)
    sol.moveZeroesNaive(nums1)
    print(nums1)

    nums2 = [0,0,1]
    sol.moveZeroesOptimal(nums2)
    print(nums2)