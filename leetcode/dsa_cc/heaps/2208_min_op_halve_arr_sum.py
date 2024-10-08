from typing import List
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        init_sum = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)
        # print(f"Initial sum: {init_sum}")
        # print(f"Initial heap: {nums}")

        sum_diff = 0
        steps = 0
        while abs(sum_diff) < (init_sum / 2):
            top = heapq.heappop(nums)
            half_top = top / 2
            sum_diff += top - half_top
            # print(f"Top: {top} - half top: {half_top} - sum_diff: {sum_diff}")
            heapq.heappush(nums, half_top)
            steps += 1

            # print(f"{abs(sum_diff)} - {init_sum/2}")
        
        return steps


if __name__ == "__main__":
    sol = Solution()

    nums1 = [5,19,8,1]
    ans1 = sol.halveArray(nums1)
    print(ans1)

    nums2 = [3,8,20]
    ans2 = sol.halveArray(nums2)
    print(ans2)

    nums3 = [6,58,10,84,35,8,22,64,1,78,86,71,77]
    ans3 = sol.halveArray(nums3)
    print(ans3)

    nums4 = [1]
    ans4 = sol.halveArray(nums4)
    print(ans4)