from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Going with optimized approach now
        
        sums_so_far = defaultdict(int)
        our_sum = 0
        num_subarrays = 0
        for n in nums:
            our_sum += n
            if our_sum == k:
                num_subarrays += 1
            if (our_sum - k) in sums_so_far:
                num_subarrays += sums_so_far[our_sum - k]
            sums_so_far[our_sum] += 1
        return num_subarrays
            
            
        
        
        # The commented code is for TLE but is correct
        # if len(nums) ==1:
        #     if nums[0] == k:
        #         return 1
        #     else:
        #         return 0
        # Sum = [0] * (len(nums)+1)
        # c = 0
        # for i in range (1,len(nums)+1):
        #     Sum[i] = Sum[i-1] + nums[i-1]
        #     # Save cumulative sum upto previous number
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         check  = Sum[j] - Sum[i]
        #         if  check == k:
        #             c +=1
        # return c