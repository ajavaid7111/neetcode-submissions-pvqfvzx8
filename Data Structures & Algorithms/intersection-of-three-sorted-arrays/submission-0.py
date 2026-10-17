class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        new_list = []

        read = 0
        read1 = 0
        read3 = 0

        while read < len(arr1) and read1 < len(arr2) and read3 < len(arr3):

            if arr1[read] == arr2[read1] == arr3[read3]:
                new_list.append(arr1[read])
                read += 1 
                read1 += 1 
                read3 += 1

            elif arr1[read] <= arr2[read1] and arr1[read] <= arr3[read3]:
                read += 1
            elif arr2[read1] <= arr1[read] and arr2[read1] <= arr3[read3]:
                read1 += 1
            else:
                read3 += 1

        return new_list