class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1: return ''
        isAllA = True
        target = len(palindrome) # target index to be converted into 'a'
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                isAllA = False
                target = min(target, i) # target should be the letter shown earlier
		# if all letters are 'a', just switch the last letter to 'b'
        if isAllA: return palindrome[:len(palindrome) - 1] + 'b'
		# if not, replace the target letter with 'a' and attach the rest
        return palindrome[:target] + 'a' + palindrome[target + 1:]