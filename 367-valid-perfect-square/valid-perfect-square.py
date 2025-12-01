class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return  (num ** 0.5) % 2 == 0 or (num ** 0.5) % 2 == 1
        