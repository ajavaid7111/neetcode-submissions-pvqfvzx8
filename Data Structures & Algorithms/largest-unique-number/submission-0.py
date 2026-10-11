class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        

        
        map1 = {}
        for num in nums:
            map1[num] = map1.get(num, 0) + 1
            
      
        unique_nums = [num for num, count in map1.items() if count == 1]
        
       
        return max(unique_nums) if unique_nums else -1



