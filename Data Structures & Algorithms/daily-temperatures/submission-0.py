class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        stack = []
        stack.append(0)
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and  temperatures[i] > temperatures[stack[-1]]:
                oldInd = stack.pop()
                res[oldInd] = i - oldInd
            stack.append(i)
        return res
