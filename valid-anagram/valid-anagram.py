class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        
        for i in s:
            
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        
        for i in t:
            if i in dict_s:
                dict_s[i] -= 1
            else:
                return False

            
        print(dict_s)
        c = 0
        for i in dict_s.values():
            if i > 0:
                c+=1
                
        if c >= 1:
            return False
        else:
            return True
        