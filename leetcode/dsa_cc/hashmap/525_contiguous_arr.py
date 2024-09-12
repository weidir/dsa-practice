from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        max_len = 0

        # Compute prefix sum but averaged around 0
        run_sum = 0
        prefix_sum = []
        for val in nums:
            if val == 0:
                run_sum -= 1
            else:
                run_sum += 1

            prefix_sum.append(run_sum)
        
        print(f"Prefix sum arr: {prefix_sum}")
        
        # Loop through prefix sums and check if sums have been seen before
        max_len = 0
        sum_ind = {0: -1}
        for index, sum in enumerate(prefix_sum):
            if sum in sum_ind:
                sub_arr_len = index - sum_ind[sum]
                if sub_arr_len > max_len:
                    max_len = sub_arr_len
            else:
                sum_ind[sum] = index

        return max_len
        

if __name__ == "__main__":
    sol = Solution()

    nums1 = [0,1]
    ans1 = sol.findMaxLength(nums1)
    print(ans1)

    nums2 = [0,1,0]
    ans2 = sol.findMaxLength(nums2)
    print(ans2)

    nums3 = [0,0,0,1,1,1,0]
    ans3 = sol.findMaxLength(nums3)
    print(ans3)