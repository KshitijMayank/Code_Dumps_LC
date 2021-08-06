class Solution:
    def reverse(self, x: int) -> int:
        Max = 2**31
        res = 0
        Flag = False
        if x <0:
            x = -x
            Flag= True
        while x > 0:
            
            rem = x % 10
            x = x // 10
            res = res * 10 + rem
            
        if (res > Max or res < -Max):
            return 0
        if Flag:
            return -res
        else:
            return res
            
            
            
        