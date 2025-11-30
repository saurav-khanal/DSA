class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0 or n > 2**31-1:
            return False

        while n>1:
            if n%2==0:
                n=n//2
            else:
                return False
        return True

        