from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # Brute force
        boxes = []
        for box in boxTypes:
            boxes.extend([box[1]] * box[0])
        
        boxes.sort(reverse=True)

        added = 0
        added_units = 0
        for box in boxes:
            if added + 1 <= truckSize:
                added_units += box
                added += 1
            else:
                return added_units
        return added_units
    
    # def maximumUnits_heap(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
    

if __name__ == "__main__":
    sol = Solution()

    boxTypes1 = [[1,3],[2,2],[3,1]]
    truckSize1 = 4
    ans1 = sol.maximumUnits(boxTypes1, truckSize1)
    print(ans1)

    boxTypes2 = [[5,10],[2,5],[4,7],[3,9]]
    truckSize2 = 10
    ans2 = sol.maximumUnits(boxTypes2, truckSize2)
    print(ans2)