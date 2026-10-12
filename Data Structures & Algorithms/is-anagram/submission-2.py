class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        for char in s:
            map1[char] = map1.get(char, 0) + 1

        for char in t:
            if char not in map1 or map1[char] == 0:
                return False
            map1[char] -= 1

        return True
