from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) <= k:
            return arr

        # Find the element closest to the target if it doesn't exist
        def bin_search(arr, x) -> int:
            # Check edge cases where given target is outside of the array
            # Assumes array is sorted
            if x < arr[0]:
                return 0
            elif x > arr[-1]:
                return -1
            
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (r - l) // 2

                if arr[mid] == x:
                    return mid
                
                elif arr[mid] > x:
                    r = mid - 1

                elif arr[mid] < x:
                    l = mid + 1

            return -1
            
        x_idx = bin_search(arr, x)
        # print(f"X idx: {x_idx}")

        l_idx = x_idx - (k // 2) if k != 1 else x_idx - k
        r_idx = x_idx + (k // 2) if k != 1 else x_idx + k
        # print(f"Initial left index: {l_idx} - Initial right index: {r_idx}")
        
        if l_idx < 0 and r_idx <= len(arr) - 1:
            r_idx -= l_idx
            l_idx = 0
        elif l_idx >= 0 and r_idx > len(arr) - 1:
            l_idx -= r_idx - len(arr)
            r_idx = -1
        # print(f"Final left index: {l_idx} - Final right index: {r_idx}")

        return arr[l_idx:r_idx][:k]


if __name__ == "__main__":
    sol = Solution()

    arr1 = [1,2,3,4,5]
    k1 = 4
    x1 = 3
    ans1 = sol.findClosestElements(arr1, k1, x1)
    print(ans1)

    arr2 = [1,1,2,3,4,5]
    k2 = 4
    x2 = -1
    ans2 = sol.findClosestElements(arr2, k2, x2)
    print(ans2)

    arr3 = [1]
    k3 = 1
    x3 = 0
    ans3 = sol.findClosestElements(arr3, k3, x3)
    print(ans3)

    arr4 = [1,2]
    k4 = 1
    x4 = 1
    ans4 = sol.findClosestElements(arr4, k4, x4)
    print(ans4)
