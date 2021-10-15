class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        For each letter, say it occurs v times. We know we have v // 2 * 2 letters that can be partnered for sure. For example, if we have 'aaaaa', then we could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.

At the end, if there was any v % 2 == 1, then that letter could have been a unique center. Otherwise, every letter was partnered. To perform this check, we will check for v % 2 == 1 and ans % 2 == 0, the latter meaning we haven't yet added a unique center to the answer.
        """
        _d = dict()
        for ch in s:
            if ch in _d:
                _d[ch] +=1
            else:
                _d[ch] =1
        res = 0
        for key,val in _d.items():
            res += (val //2) * 2
            if val % 2 == 1 and res % 2 == 0:
                res += 1
        return res
            
        
        
        