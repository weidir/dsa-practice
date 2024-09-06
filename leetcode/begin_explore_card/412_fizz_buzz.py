from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n + 1):
            ans.append(
                "FizzBuzz" if i % 15 == 0 else
                "Fizz" if i % 3 == 0 else
                "Buzz" if i % 5 == 0 else
                str(i)
            )
        
        return ans
    

if __name__ == "__main__":
    n = 3
    sol = Solution()
    print(sol.fizzBuzz(n))
