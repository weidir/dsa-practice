from typing import List
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        n = len(isConnected)

        # Construct the hashmap from the adjacency matrix
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        print(graph)

        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    input1 = [[1,1,0],[1,1,0],[0,0,1]]
    ans1 = sol.findCircleNum(input1)
    print(ans1)