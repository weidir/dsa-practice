from typing import List

class Solution:
    def duplicateZeros1(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        arr_len = len(arr)
        i = 0

        while i <= arr_len - 1:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1
    

    def duplicateZeros2(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = []
        arr_len = len(arr)
        for val in arr:
            if not val:
                temp.append(0)
                temp.append(0)
            else:
                temp.append(val)
        
        arr[:] = temp[:arr_len]


if __name__ == "__main__":
    arr1 = [1,0,2,3,0,4,5,0]
    arr2 = [1,0,2,3,0,4,5,0]
    sol = Solution()
    sol.duplicateZeros1(arr1)
    print(arr1)

    sol.duplicateZeros2(arr2)
    print(arr2)