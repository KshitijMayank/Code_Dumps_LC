class Solution:
    def isValid(self, s: str) -> bool:
        
        opened = ['(','{','[']
        pairs = {
            '}':'{',
            ')':'(',
            ']': '['
        }
        stack=[]
        for i in range(len(s)):
            
            if s[i] in opened:
                stack.append(s[i])
            elif (len(stack) !=0 and stack[-1] == pairs[s[i]]):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
                