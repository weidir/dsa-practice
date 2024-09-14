class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        n = len(s)
        l = 0
        r = 1

        max_len = 1
        bag = {s[l]: 0}

        while r < n:
            window_len = r - l + 1
            # If the new character isn't in the bag or is outside of it
            if s[r] not in bag or bag[s[r]] < l:
                
                bag[s[r]] = r
                if window_len > max_len:
                    max_len = window_len

                r += 1
            
            else:
                l = bag[s[r]] + 1
                bag[s[r]] = r
                r += 1
                            
        return max_len
        
        
if __name__ == "__main__":
    sol = Solution()

    s1 = "abcabcbb"
    ans1 = sol.lengthOfLongestSubstring(s1)
    print(ans1)

    s2 = "bbbbb"
    ans2 = sol.lengthOfLongestSubstring(s2)
    print(ans2)

    s3 = "pwwkew"
    ans3 = sol.lengthOfLongestSubstring(s3)
    print(ans3)

    s4 = ""
    ans4 = sol.lengthOfLongestSubstring(s4)
    print(ans4)

    s5 = "dvdf"
    ans5 = sol.lengthOfLongestSubstring(s5)
    print(ans5)

    s6 = "tmmzuxt"
    ans6 = sol.lengthOfLongestSubstring(s6)
    print(ans6)