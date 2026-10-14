class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        
        for index, value in enumerate(nums):
            complement = target - value
            
        
            if complement in map1:
                return [map1[complement], index]
            
   
            map1[value] = index





            










        