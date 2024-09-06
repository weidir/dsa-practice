from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        l = 0
        r = k
        arr_len = len(nums)
        arr_sum = None 
        arr_sum_max = None

        if arr_len == 1:
            return nums[0]

        while r <= arr_len:
            if arr_sum is not None:
                arr_sum = arr_sum + nums[r-1] - nums[l-1]
            else:
                arr_sum = sum(nums[l:r])
                arr_sum_max = arr_sum

            if arr_sum > arr_sum_max:
                arr_sum_max = arr_sum

            l += 1
            r += 1

        return arr_sum_max / k


if __name__ == "__main__":
    nums1 = [1,12,-5,-6,50,3]
    k1 = 4

    nums2 = [5]
    k2 = 1

    nums3 = [0, 1, 1, 3, 3]
    k3 = 4

    nums4 = [8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891]
    k4 = 93

    nums5 = [0,4,0,3,2]
    k5 = 1

    sol = Solution()
    max_avg1 = sol.findMaxAverage(nums1, k1)
    print(max_avg1)

    max_avg2 = sol.findMaxAverage(nums2, k2)
    print(max_avg2)

    max_avg3 = sol.findMaxAverage(nums3, k3)
    print(max_avg3)

    max_avg4 = sol.findMaxAverage(nums4, k4)
    print(max_avg4)

    max_avg5 = sol.findMaxAverage(nums5, k5)
    print(max_avg5)