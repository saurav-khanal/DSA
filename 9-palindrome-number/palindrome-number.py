class Solution(object):
    def isPalindrome(self, x):
        y = x
        rev=0
        max = 2**31 - 1
        if x<0:
            return False
        while x >0:
            lastdigit = x % 10
            x = x//10
            rev = rev*10 + lastdigit
        if rev >= max:
            return False
        if y==rev:
            return True
        else:
            return False
        
            
        
        