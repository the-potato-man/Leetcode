# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        
        intervals.sort(key=lambda interval: interval.start)
        
        heap = []
        heapq.heappush(heap, intervals[0].end)
        for i in range(1,len(intervals)):
            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
        
        return len(heap)