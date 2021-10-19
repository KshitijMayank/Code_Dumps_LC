from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ns , np = len(s) , len(p)
        
        p_count = Counter(p)
        s_count = Counter()
        res = []
        
        for i in range(ns):
            # add the pointer to the window entering 
            s_count[s[i]] +=1
            # window complete
            if i >= np:
                # remove the last count if the count == 1
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    # reduce if not only 1
                    s_count[s[i - np]] -=1
            
            # Comparing the hashmaps and add
            if p_count == s_count:
                res.append(i - np + 1)
                
        return res
            
                
                
        
        