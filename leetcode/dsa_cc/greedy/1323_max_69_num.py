class Solution:
    def maximum69Number(self, num: int) -> int:
        
        num_list = list(str(num))

        for idx, char in enumerate(num_list):
            if char == "6":
                num_list[idx] = "9"
                return int("".join(num_list))
        return num


if __name__ == "__main__":
    sol = Solution()

    num1 = 9669
    ans1 = sol.maximum69Number(num1)
    print(ans1)

    num2 = 9999
    ans2 = sol.maximum69Number(num2)
    print(ans2)