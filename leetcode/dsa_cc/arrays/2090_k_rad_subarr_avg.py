from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        # Define important constants
        n = len(nums)
        window_len = (k * 2) + 1

        # Get running sum
        run_sum = 0
        run_sum_arr = []
        for val in nums:
            run_sum = run_sum + val
            run_sum_arr.append(run_sum)

        k_avg_arr = []
        for i in range(n):
            # If radius arms go out of bounds, impute -1
            if i - k < 0 or i + k >= n:
                k_avg_arr.append(-1)
            else:
                if i > k:
                    k_avg = (run_sum_arr[i+k] - run_sum_arr[i-k-1]) // window_len
                else:
                    k_avg = run_sum_arr[i+k] // window_len
                k_avg_arr.append(k_avg)
        
        return k_avg_arr


if __name__ == "__main__":
    sol = Solution()

    nums1 = [7,4,3,9,1,8,5,2,6]
    k1 = 3
    ans1 = sol.getAverages(nums1, k1)
    print(ans1)

    nums2 = [100000]
    k2 = 0
    ans2 = sol.getAverages(nums2, k2)
    print(ans2)

    nums3 = [18334,25764,19780,92480,69842,73255,89893]
    k3 = 0
    ans3 = sol.getAverages(nums3, k3)
    print(ans3)