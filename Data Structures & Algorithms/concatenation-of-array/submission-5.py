class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # basically we want to make two of the same arrays 

        ## 

        for num in list(nums):
            nums.append(num)

        return nums