class Solution:
    def isValid(self, s: str) -> bool:
        open_braces = ['(','[','{']
        pairs = {
            '}':'{',
            ')' : '(',
            ']':'['
        }
        stack=[]
        for elem in s:
            if elem in open_braces:
                stack.append(elem)
            elif len(stack) !=0 and stack[-1] == pairs[elem]:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        
                