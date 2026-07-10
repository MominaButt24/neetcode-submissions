class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        temp = abs(n)
        ans = 1
        while temp > 0:
              ans *= x
              temp-=1

        if n < 0:
            return 1 / ans
        return ans
        