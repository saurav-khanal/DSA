import math
class Solution(object):
    def isPowerOfTwo(self, n):
        if 2**31 -1 < n or n <= 0:
            return False
        x= math.log(n)/math.log(2)
        if abs(x - round(x)) < 1e-10:
            return True
        else:
            return False
