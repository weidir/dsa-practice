from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        r = l + 1
        nums_len = len(nums)
        max_len = 0
        num_zeros = r - l - sum(nums[l:r])

        # Need to find a window where the number of 0's = k
        # Need to expand window if number of 0's < k (r += 1)
        # Need to shrink the window if the number of 0's is > k (l += 1)
        while r <= nums_len:
            print(f"Begin values, l: {l}, r: {r}, window: {nums[l:r]}, num_zeros: {num_zeros}, max len: {max_len}")
            window = r - l
            if num_zeros <= k:
                if window > max_len:
                    max_len = window
                r += 1

                if r <= nums_len and nums[r-1] == 0:
                    num_zeros = num_zeros + 1
            else:
                l += 1
                if nums[l-1] == 0:
                    num_zeros = num_zeros - 1
                
            print(f"End values, l: {l}, r: {r}, max len: {max_len}\n")
        
        return max_len


if __name__ == "__main__":

    sol = Solution()

    nums1 = [1,1,1,0,0,0,1,1,1,1,0]
    k1 = 2

    nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k2 = 3

    nums3 = [0,0,0,1]
    k3 = 4

    print(f"{sol.longestOnes(nums1, k1)}\n")
    print(f"{sol.longestOnes(nums2, k2)}\n")
    print(f"{sol.longestOnes(nums3, k3)}\n")