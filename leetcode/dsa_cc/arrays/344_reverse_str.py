from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        j = len(s) - 1
        while i < j:
            h = s[i]
            t = s[j]

            s[i] = t
            s[j] = h

            i += 1
            j -= 1
    
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s[:] = s[::-1]


if __name__ == "__main__":
    s1 = ["h","e","l","l","o"]
    s2 = ["h","e","l","l","o"]
    sol = Solution()
    sol.reverseString(s1)
    print(s1)
    sol.reverseString2(s2)
    print(s2)