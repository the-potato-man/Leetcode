'''
Test Cases
[]
[1]
[1,2]
[1,2,3]
[3,1,2]
'''
import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        num = num * 1.0
        # (priority number, data)
        # Invert the priority for max heaps
        heapq.heappush(self.maxHeap, (-num, num))
        priority, data = heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, (data,data))

        while len(self.maxHeap) < len(self.minHeap):
            priority, data = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, (-data, data))
            
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            p1, data1 = self.maxHeap[0]
            p2, data2 = self.minHeap[0]
            return (data1 + data2) / 2
        else:
            p1, data = self.maxHeap[0]
            return data

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()