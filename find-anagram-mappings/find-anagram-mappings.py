class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2==[]:
            
            return []
        
        mapping = {}
        
        for i,v in enumerate(nums2):
            mapping[v] = i
        res = []
        for i in range(len(nums1)):
            if nums1[i] in mapping:
                res.append(mapping[nums1[i]])
            else:
                res = []
        return res
            