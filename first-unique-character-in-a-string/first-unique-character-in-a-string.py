
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        _dict = {}
        seen = set()
        
        for idx,val in enumerate(s):
            
            if val not in seen:
                seen.add(val)
                _dict[val] = idx
            elif val in seen and val in _dict:
                del _dict[val]
        
        if _dict:
            return min(_dict.values())
        else:
            return -1
                
        
                
            
            
        
        