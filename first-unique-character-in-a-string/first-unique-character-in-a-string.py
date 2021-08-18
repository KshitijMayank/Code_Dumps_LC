from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = defaultdict(int)
        seen = set()
        for i,val in enumerate(s):
            if val not in seen:
                seen.add(val)
                d[val] = i
            elif val in seen and val in d:
                del d[val]
        if d :
            
            return min(d.values()) 
        else:
            return -1
                
            
            
        
        