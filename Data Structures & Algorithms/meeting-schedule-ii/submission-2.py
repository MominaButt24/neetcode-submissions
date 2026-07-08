"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        res = count = 0

        st = []
        ed = []

        for interval in intervals:
            st.append(interval.start)
            ed.append(interval.end)

        st.sort()
        ed.sort()

        s , e = 0, 0

        while s < len(intervals):
            if st[s] < ed[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res = max(count, res)
        
        return res