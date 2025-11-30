class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 & n==log2(n)%1
