class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = list(magazine)
        for letter in ransomNote:
            if letter in magazine_list:
                magazine_list.remove(letter)
            elif letter not in magazine_list:
                return False
        
        return True