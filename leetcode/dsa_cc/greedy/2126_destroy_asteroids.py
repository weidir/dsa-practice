from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids.sort()

        for asteroid in asteroids:
            if asteroid <= mass:
                mass += asteroid
            else:
                return False

        return True
            
        
if __name__ == "__main__":
    sol = Solution()

    mass1 = 10
    asteroids1 = [3,9,19,5,21]
    ans1 = sol.asteroidsDestroyed(mass1, asteroids1)
    print(ans1)

