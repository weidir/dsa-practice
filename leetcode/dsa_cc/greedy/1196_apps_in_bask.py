from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        run_sum = 0
        run_cnt = 0
        weight.sort()

        for w in weight:
            if run_sum + w > 5000:
                return run_cnt
            else:
                run_sum += w
                run_cnt += 1

        return run_cnt


if __name__ == "__main__":
    sol = Solution()

    weight1 = [100,200,150,1000]
    ans1 = sol.maxNumberOfApples(weight1)
    print(ans1)

    weight2 = [900,950,800,1000,700,800]
    ans2 = sol.maxNumberOfApples(weight2)
    print(ans2)