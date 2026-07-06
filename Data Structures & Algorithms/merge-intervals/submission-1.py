class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        end = 0
        start = 0
        res = []
        for i in range(1, len(intervals)):
            if intervals[end][1] >= intervals[i][0]:
                if intervals[end][1] < intervals[i][1]:
                    end = i
            else:
                res.append([intervals[start][0], intervals[end][1]])
                end = i
                start = i
                
        res.append([intervals[start][0], intervals[end][1]])
        return res