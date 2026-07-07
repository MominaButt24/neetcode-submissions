class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]
        res=0
        for i in range(1,len(intervals)):
            if prevEnd > intervals[i][0]:
                prevEnd = min(prevEnd, intervals[i][1])
                res+=1
            else:
               prevEnd = intervals[i][1]
        return res