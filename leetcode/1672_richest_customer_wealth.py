from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Sum each column
        # Linear time and space complexity
        col_sums = []
        for bal_list in accounts:
            col_sums.append(sum(bal_list))

        # Find the maximum value amongst all column sums
        col_sums.sort()
        return col_sums[-1]

    def maximumWealthQuickSort(self, accounts: List[List[int]]) -> int:

        # Sum each column
        # Linear time and space complexity
        col_sums = []
        for bal_list in accounts:
            col_sums.append(sum(bal_list))

        # Find the maximum value amongst all column sums
        sorted_wealths = self.quicksort(col_sums)
        return sorted_wealths[-1]
    

    def quicksort(self, arr: list) -> list:

        if len(arr) <= 1:
            return arr
        
        less, piv, more = self.pivot(arr)

        return self.quicksort(less) + [piv] + self.quicksort(more)
        
        
    def pivot(self, arr: list) -> list:
        """
        Function that takes a pivot value from a list and divides the list into 
        """

        if not arr:
            return arr

        piv = arr[0]
        less = []
        more = []

        for val in arr[1:]:
            if val < piv:
                less.append(val)
            else:
                more.append(val)
        
        return less, piv, more
    
        
# Test the function
if __name__ == "__main__":
    sol = Solution()

    sol_val = sol.maximumWealth(accounts=[[2,8,7],[7,1,3],[1,9,5]])
    print(sol_val)