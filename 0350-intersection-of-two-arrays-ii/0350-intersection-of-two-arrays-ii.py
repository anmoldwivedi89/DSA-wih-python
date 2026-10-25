class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set()
        lst = []
        dict1 = {}
        dict2 = {}
        for x in nums1:
            dict1[x] = dict1.get(x,0)+ 1
        for j in nums2:
            dict2[j] = dict2.get(j,0) +1
        for z in dict1:
            if z in dict2:
                for x in range(min(dict1[z],dict2[z])):

                    lst.append(z)
                
        return lst
         

    
        
        