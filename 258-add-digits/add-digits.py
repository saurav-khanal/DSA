class Solution(object):
    def addDigits(self, num):
        if num==0:
            return num
        sum= 1+(num-1)%9;
        return sum