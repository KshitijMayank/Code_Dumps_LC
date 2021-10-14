class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ## Brute Force
        # max_sum = -float('inf')
        # for i in range(len(nums)):
        #     cur_sum = 0
        #     for j in range(i,len(nums)):
        #         cur_sum += nums[j]
        #         max_sum = max(cur_sum,max_sum)
        # return max_sum
    
        ## ----optimized code Dynamic
        
        cur_subarray = nums[0]
        max_subarray = nums[0]
        
        for i in range(1,len(nums)):
            cur_subarray = max(nums[i], nums[i] + cur_subarray)
            max_subarray = max(max_subarray, cur_subarray)
            
        return max_subarray
            
        
        
            
            
            