class Solution:
    def scoreOfString(self, s: str) -> int:
        total_score = 0

        for i in range(len(s) -1 ):
            diff = abs(ord(s[i]) - ord(s[i + 1]))

            total_score += diff

        
        return total_score


        