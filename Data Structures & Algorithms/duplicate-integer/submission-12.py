class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make a set 
       seen = set()
       for num in nums:
            if num in seen:
                return True
            seen.add(num)

       return False
