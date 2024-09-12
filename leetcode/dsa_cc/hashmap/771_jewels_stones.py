class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewel_count = 0
        for stone in stones:
            if stone in jewels:
                jewel_count += 1
        
        return jewel_count
    

if __name__ == "__main__":
    sol = Solution()

    jewels1 = "aA"
    stones1 = "aAAbbbb"
    ans1 = sol.numJewelsInStones(jewels1, stones1)
    print(ans1)

    jewels2 = "z"
    stones2 = "ZZ"
    ans2 = sol.numJewelsInStones(jewels2, stones2)
    print(ans2)