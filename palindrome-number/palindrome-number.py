class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0 | x == 1:
            return True
        if x < 0 :
            return False
        rev = 0
        old = x
        new = 0
        while x > 0:
            rem = x % 10
            new = new * 10 +  rem
            x = x // 10
        print(new)   
        if new == old:
            
            return True
        
        