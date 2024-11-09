from typing import List
import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        def binary_search(arr: list, target: int) -> int:

            if target > arr[-1]:
                return len(arr)

            l = 0
            r = len(arr) - 1

            while l < r:
                mid = (l + r) // 2
                if target < arr[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            return l
        
        nums.sort()

        run_sum = 0
        prefix_sum = []
        for num in nums:
            run_sum += num
            prefix_sum.append(run_sum)
        print(f"Prefix sum: {prefix_sum}")

        ans = []
        for query in queries:
            idx = binary_search(prefix_sum, query)
            print(f"Query: {query} - Query index: {idx}")
            ans.append(idx)
        
        return ans
    

if __name__ == "__main__":
    sol = Solution()

    nums1 = [4,5,2,1]
    queries1 = [3,10,21]
    ans1 = sol.answerQueries(nums1, queries1)
    print(ans1)