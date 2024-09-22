class Solution:
    def makeGood(self, s: str) -> str:

        if len(s) == 0:
            return ""

        # Initialize the stack with the first element of the string
        stack = [s[0]]
        
        for char in s[1:]:
            stack.append(char)

            if len(stack) > 1:
                if (stack[-1].upper() == stack[-2] or stack[-1].lower() == stack[-2]) and stack[-1] != stack[-2]:
                    stack.pop()
                    stack.pop()
        
        return ''.join(stack)


if __name__ == "__main__":
    sol = Solution()

    s1 = "leEeetcode"
    ans1 = sol.makeGood(s1)
    print(f"Answer 1: '{ans1}'")
    assert ans1 == "leetcode"

    s2 = "abBAcC"
    ans2 = sol.makeGood(s2)
    print(f"Answer 2: '{ans2}'")
    assert ans2 == ""

    s3 = "kkdsFuqUfSDKK"
    ans3 = sol.makeGood(s3)
    print(f"Answer 3: '{ans3}'")
    # assert ans3 == ""