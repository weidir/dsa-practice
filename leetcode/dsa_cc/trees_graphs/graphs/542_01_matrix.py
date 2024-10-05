from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        # Start BFS from each 0
        