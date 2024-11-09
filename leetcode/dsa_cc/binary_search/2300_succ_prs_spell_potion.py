from typing import List
from math import ceil

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        print(f"Success: {success}\n")

        def binary_search(arr: List[int], target: int) -> int:

            if target > arr[-1]:
                return len(arr)

            left = 0
            right = len(arr) - 1

            while left < right:

                mid = (left + right) // 2

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left

        # Sort the potions list
        potions.sort()

        ans = []
        for spell_power in spells:
            target = ceil(success / spell_power)

            target_idx = binary_search(potions, target)
            print(f"Spell power: {spell_power} - target potion power: {target} - target index: {target_idx}")

            success_pairs = len(potions) - target_idx
            print(f"Success pairs: {success_pairs}\n")
            ans.append(success_pairs)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    spells1 = [5,1,3]
    potions1 = [1,2,3,4,5]
    success1 = 7
    ans1 = sol.successfulPairs(spells1, potions1, success1)
    print(ans1)