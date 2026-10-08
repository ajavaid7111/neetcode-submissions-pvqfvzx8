class Solution:
    def confusingNumber(self, n: int) -> bool:
        flip_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        s = str(n)
        rotated = ""
        
        
        for char in reversed(s):
           
            if char not in flip_map:
                return False
            
            rotated += flip_map[char]
        
      
        return int(rotated) != n