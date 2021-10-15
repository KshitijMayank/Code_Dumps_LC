from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ns , np = len(s) , len(p)
        
        p_count = Counter(p)
        s_count = Counter()
        # print(p_count,s_count)
        res = []
        
        for i in range(ns):
            
            s_count[s[i]] +=1
            
            if i >= np:
                
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    # second occpurance or aboe
                    s_count[s[i - np]] -=1
            
            # Comparing the hasmaps
            if p_count == s_count:
                res.append(i - np + 1)
                
        return res
            
                
                
        
        