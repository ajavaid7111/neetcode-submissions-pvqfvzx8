class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for char in magazine:
           counts[char] = counts.get(char, 0) + 1
        
        for char1 in ransomNote:
            if char1 not in counts or counts[char1] == 0:
                return False
            counts[char1] -= 1

        return True 

        