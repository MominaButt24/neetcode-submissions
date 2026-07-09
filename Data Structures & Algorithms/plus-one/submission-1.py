class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = digits[0]
        for i in range(1,len(digits)):
            num = num*10 + digits[i]

        num = num + 1

        numArr = []
        while num > 0:
            numArr.append(num%10)
            num = num // 10

        numArr.reverse()
        return numArr
