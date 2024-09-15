from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # Convert lists to tuples and hash them
        matches = 0

        row_dict = {}
        for row in grid:
            row_tup = tuple(row)
            if row_tup not in row_dict:
                row_dict[row_tup] = 1
            else:
                row_dict[row_tup] += 1
            
        for col in zip(*grid):
            col_tup = tuple(col)

            if col_tup in row_dict:
                matches += 1 * row_dict[col_tup]
        
        return matches


    def equalPairs2(self, grid: List[List[int]]) -> int:

        n = len(grid)
        matches = 0

        row_dict = {}
        col_dict = {}
        for i in range(n):
            row_dict[i] = grid[i]
            for j in range(n):
                if j not in col_dict:
                    col_dict[j] = [grid[i][j]]
                else:
                    col_dict[j].append(grid[i][j])
        
        for index, row in row_dict.items():
            for index, col in col_dict.items():
                if row == col:
                    matches += 1
        
        return matches
        


if __name__ == "__main__":
    sol = Solution()

    grid1 = [[3,2,1],[1,7,6],[2,7,7]]
    ans1 = sol.equalPairs(grid1)
    print(ans1)

    grid2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    ans2 = sol.equalPairs(grid2)
    print(ans2)