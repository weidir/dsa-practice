from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        graph = defaultdict(list)

        # Convert edges to graph
        for edge in edges:
            first = edge[0]
            second = edge[1]

            graph[first].append(second)
            graph[second].append(first)
        
        print(graph)
        
        def dfs_check(source, destination):

            seen = set()
            stack = [source]

            while stack and len(seen) <= n:
                
                curr = stack.pop()

                for node in graph[curr]:
                    if node == destination:
                        return True
                        
                    if node not in seen:
                        seen.add(node)
                        stack.append(node)
            
            return False
    
        return dfs_check(source, destination)


if __name__ == "__main__":
    sol = Solution()

    n1 = 3
    edges1 = [[0,1],[1,2],[2,0]]
    source1 = 0
    destination1 = 2
    ans1 = sol.validPath(n1, edges1, source1, destination1)
    print(ans1)

    n2 = 6
    edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source2 = 0
    destination2 = 5
    ans2 = sol.validPath(n2, edges2, source2, destination2)
    print(ans2)

    n3 = 10
    edges3 = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    source3 = 5
    destination3 = 9
    ans3 = sol.validPath(n3, edges3, source3, destination3)
    print(ans3)

    n4 = 10
    edges4 = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
    source4 = 7
    destination4 = 5
    ans4 = sol.validPath(n4, edges4, source4, destination4)
    print(ans4)