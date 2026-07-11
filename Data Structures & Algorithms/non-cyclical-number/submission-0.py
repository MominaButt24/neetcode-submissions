class Solution:
    def isHappy(self, n: int) -> bool:
        
        freq = {}
    
        while True:
            digit = 0
            while n > 0:
               digit += (n%10) ** 2
               n = n // 10
            if digit == 1:
                return True
            if digit in freq:
                return False
            freq[digit] = 1
            n = digit
        return False