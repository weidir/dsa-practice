from typing import List, Tuple

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def get_new_mid(left: Tuple[int], right: Tuple[int], m: int, n: int) -> Tuple[int]:
            left_idx = (left[0] * n) + left[1]
            right_idx = (right[0] * n) + right[1]

            mid_idx = (left_idx + right_idx) // 2

            midpoint = (mid_idx // n, mid_idx % n)
            return midpoint

        def get_new_left(midpoint: Tuple[int], left: Tuple[int], m: int, n: int) -> Tuple[int]:

            # Make the left value one iteration to the right of the midpoint
            if midpoint[1] != (n - 1):
                left = (midpoint[0], midpoint[1] + 1)
            else:
                left = (midpoint[0] + 1, 0)
            
            return left

        def get_new_right(midpoint: Tuple[int], right: Tuple[int], m: int, n: int) -> Tuple[int]:

            # Make the right value one iteration to the left of the midpoint
            if midpoint[1] != 0:
                right = (midpoint[0], midpoint[1] - 1)
            else:
                right = (midpoint[0] - 1, n - 1)
            
            return right

        m = len(matrix)
        n = len(matrix[0])

        left = (0, 0)
        right = (m-1, n-1)

        while left <= right:

            midpoint = get_new_mid(left, right, m, n)
            mid_row = midpoint[0]
            mid_col = midpoint[1]
            mid_val = matrix[mid_row][mid_col]
            print(f"Left: {left} - Right: {right}")
            print(f"Midpoint: {(mid_row, mid_col)} - mid val: {mid_val}\n")
            
            if mid_val == target:
                return True
            elif mid_val > target:
                right = get_new_right((mid_row, mid_col), right, m, n)
            else:
                left = get_new_left((mid_row, mid_col), left, m, n)
        
        return False
    

if __name__ == "__main__":
    sol = Solution()

    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    ans1 = sol.searchMatrix(matrix1, target1)
    print(ans1)

    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    ans2 = sol.searchMatrix(matrix2, target2)
    print(ans2)