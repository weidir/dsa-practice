from typing import List
from collections import defaultdict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        target_len = len(arr) // 2

        counts = defaultdict(int)

        # Get counts of each value in the array
        for item in arr:
            counts[item] += 1
        # print(counts)

        count_list = []
        for val, count in counts.items():
            count_list.append(count)
        count_list.sort(reverse=True)

        rem_cnt = 0
        rem_sum = 0
        for count in count_list:
            rem_cnt += 1
            rem_sum += count
            if rem_sum >= target_len:
                return rem_cnt
        


if __name__ == "__main__":
    sol = Solution()

    arr1 = [3,3,3,3,5,5,5,2,2,7]
    ans1 = sol.minSetSize(arr1)
    print(ans1)

    arr2 = [7,7,7,7,7,7]    
    ans2 = sol.minSetSize(arr2)
    print(ans2)