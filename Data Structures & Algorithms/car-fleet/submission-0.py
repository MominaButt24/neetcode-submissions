class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Pair the position and speed together
        # 2. Sort them by position in descending order (from closest to target to furthest)
        pairs = sorted(zip(position, speed), reverse=True)
        timeStack = []
       
        for p, s in pairs:
            t = (target - p) / s
            if not timeStack or t > timeStack[-1]:
                timeStack.append(t)
        
        return len(timeStack)
            