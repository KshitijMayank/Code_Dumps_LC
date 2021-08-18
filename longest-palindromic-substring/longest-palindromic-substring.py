
        
class Solution:
    def helper(self,s,l,r):
        while (l>=0 and r < len(s) and s[l] == s[r]):
            # we expand
            l -=1
            r +=1
        return s[l+1:r]
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) ==1:
            return s
        res = ''
        for i in range(len(s)):
            # Even
            temp = self.helper(s,i,i+1)
            if len(temp) > len(res):
                res = temp
                
            # odd 
            temp = self.helper(s,i,i)
            if len(temp) > len(res):
                res = temp
            
        return res
            
        
        
    