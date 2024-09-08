class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char_set = set(sentence)

        if len(char_set) == 26:
            return True
        
        return False
        

if __name__ == "__main__":
    sol = Solution()

    sentence1 = "thequickbrownfoxjumpsoverthelazydog"
    print(sol.checkIfPangram(sentence1))

    sentence2 = "leetcode"
    print(sol.checkIfPangram(sentence2))