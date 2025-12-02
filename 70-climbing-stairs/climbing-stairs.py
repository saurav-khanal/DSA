class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        return int(round(
        ((((1 + 5**0.5) / 2) ** (n + 1)) -
        (((1 - 5**0.5) / 2) ** (n + 1))) / (5**0.5)))
        