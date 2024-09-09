from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        counts = {}
        for match in matches:
            if match[0] in counts:
                counts[match[0]]["w"] += 1
            else:
                counts[match[0]] = {"w": 1, "l": 0}
            
            if match[1] in counts:
                counts[match[1]]["l"] += 1
            else:
                counts[match[1]] = {"w": 0, "l": 1}
        
        no_loss = []
        one_loss = []
        for player, win_loss in counts.items():
            if win_loss['l'] == 0:
                no_loss.append(player)
            elif win_loss['l'] == 1:
                one_loss.append(player)
        
        no_loss.sort()
        one_loss.sort()
            
        return [no_loss, one_loss]
    

if __name__ == "__main__":
    sol = Solution()

    matches1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    print(sol.findWinners(matches1))

    matches2 = [[2,3],[1,3],[5,4],[6,4]]
    print(sol.findWinners(matches2))