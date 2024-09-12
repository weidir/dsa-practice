class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        balloon_counts = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0,
        }
        
        for letter in text:
            if letter in balloon_counts:
                balloon_counts[letter] += 1
        
        balloon_counts["l"] //= 2
        balloon_counts["o"] //= 2

        min_count = None
        for letter, count in balloon_counts.items():
            if min_count is None:
                min_count = count
            elif count < min_count:
                min_count = count

        return min_count
    

if __name__ == "__main__":
    sol = Solution()

    text1 = "nlaebolko"
    ans1 = sol.maxNumberOfBalloons(text1)
    print(ans1)

    text2 = "loonbalxballpoon"
    ans2 = sol.maxNumberOfBalloons(text2)
    print(ans2)

    text3 = "leetcode"
    ans3 = sol.maxNumberOfBalloons(text3)
    print(ans3)

    text4 = "balon"
    ans4 = sol.maxNumberOfBalloons(text4)
    print(ans4)