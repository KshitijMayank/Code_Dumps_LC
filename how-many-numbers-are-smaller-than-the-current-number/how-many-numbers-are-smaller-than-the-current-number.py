class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        mapping = {}
        N = sorted(nums)
        # we have created the mapping 
        for i,v in enumerate(N):
            if v not in mapping:
                mapping[v] = i
        
        # now we take out the index value
        res =[]
        for key,value in enumerate(nums):
            res.append(mapping[value])
            
        return res
        
            
        