class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
       

        list1= []
        for num in nums1:
            for j, numt in enumerate(nums2):
                if numt == num:
                    list1.append(j)
                    break

        return list1
