class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We will use sliding window here
        seen ={}
        left = 0
        Max = 0
        for right in range(len(s)):
            # Seen
            if s[right] not in seen:
                Max = max(Max,right-left+1)
            # Not Seen-1
            elif seen[s[right]] < left:
                # Proceed
                Max = max(Max,right-left+1)
            # Not Seen-2
            else:
                # change left pointer to where it breaks
                left = seen[s[right]] + 1
            
            seen[s[right]] = right
        return Max
                
                
            
            
        