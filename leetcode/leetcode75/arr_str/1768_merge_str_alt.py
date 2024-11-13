class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Get max length of two words
        l1, l2 = len(word1), len(word2)
        ml = max(l1, l2)

        ans = ""
        for i in range(ml):
            ans = ans + (word1[i] if i < l1 else "")
            ans = ans + (word2[i] if i < l2 else "")
        
        return ans
    

if __name__ == "__main__":
    sol = Solution()

    word11 = "abc"
    word21 = "pqr"
    ans1 = sol.mergeAlternately(word11, word21)
    print(ans1)

    word12 = "ab"
    word22 = "pqrs"
    ans2 = sol.mergeAlternately(word12, word22)
    print(ans2)

    word13 = "abcd"
    word23 = "pq"
    ans3 = sol.mergeAlternately(word13, word23)
    print(ans3)