class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] +=1
            else:
                count[nums[i]] = 1
        s = 0
        for key,val in count.items():
            if val == 1:
                s += key
        return s
        