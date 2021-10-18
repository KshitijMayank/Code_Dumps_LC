class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda x:x[0])
        for interval in intervals:
            
            if not merged or merged[-1][1] < interval[0]:
                # simply add if there is not overlap
                merged.append(interval)
            else:
                # add the max of the upper limits
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
            
                
                
            
        
        
        