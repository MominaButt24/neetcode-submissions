class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        if n == 0:
            res.append(0)
            return res
        if n == 1:
            res.append(0)
            res.append(1)
            return res

        for i in range(n+1):
            count = 0
            while i > 0:
               if i%2:
                count+=1
               i = i // 2
            res.append(count)
        return res