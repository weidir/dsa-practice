from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Convert the list of stones to a max heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            print(f"Heap at beginning of loop: {stones}")

            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            print(f"Popped off stone 1 '{stone1}' and '{stone2}")

            # If the two largest stones are not equal in weight, find the difference and push to the heap             
            if abs(stone1) >= abs(stone2):
                print(f"Pushing {stone1-stone2} to the heap")
                heapq.heappush(stones, stone1-stone2)
            print(f"Heap at end of loop: {stones}\n")
                
            
        return -heapq.heappop(stones) if stones else 0


if __name__ == "__main__":
    sol = Solution()

    stones1 = [2,7,4,1,8,1]
    ans1 = sol.lastStoneWeight(stones1)
    print(ans1)