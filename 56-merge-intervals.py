# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

'''
Test Cases
[]
[[1,2]]
[[1,2], [3,4]]
[[1,4],[4,5]]
[[1,4],[2,3]]
[[1,4],[3,6]]
[[4,5], [1,4]]
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        
        intervals.sort(key=lambda interval: interval.start)
        
        sol = [intervals[0]]
        for interval in intervals:
            if interval.start >= sol[-1].start and interval.start <= sol[-1].end:
                sol[-1].end = max(interval.end, sol[-1].end)
            else:
                sol.append(interval)
        return sol