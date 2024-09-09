from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        arr_set = set(arr)

        count = 0
        for val in arr:
            if val + 1 in arr_set:
                count += 1

        return count
    

if __name__ == "__main__":
    sol = Solution()

    arr1 = [1, 2, 3]
    ans1 = sol.countElements(arr1)
    print(ans1)

    arr2 = [1,1,3,3,5,5,7,7]
    ans2 = sol.countElements(arr2)
    print(ans2)