class Solution(object):
    def checkPerfectNumber(self, num):
        if 1 <= num>= 10**8:
            return False
        div = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                div.append(i)
                if i != num // i:
                    div.append(num // i)
        div.sort()
        del div[-1]
        if num == sum(div):
            return True
        else:
            return False
