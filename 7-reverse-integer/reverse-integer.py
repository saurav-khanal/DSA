class Solution(object):
    def reverse(self, x):
        rev=0
        min = -2**31
        max = 2**31 - 1
        if x<0:
            sign = -1
            x = abs(x)
        else: sign = 1
        while x >0:
            lastdigit = x % 10
            x = x//10
            rev = rev*10 + lastdigit
        if min <= rev >= max:
            return 0
        else: 
            return sign*rev
            
        