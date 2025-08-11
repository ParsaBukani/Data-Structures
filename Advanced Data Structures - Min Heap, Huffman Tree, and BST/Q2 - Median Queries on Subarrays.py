import heapq  
import sys
input = sys.stdin.read

class MedianFinder:  
    def __init__(self):  
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):  
        if not self.max_heap or num <= -self.max_heap[0]:  
            heapq.heappush(self.max_heap, -num)
        else:  
            heapq.heappush(self.min_heap, num)  

        self.rebalance() 

    def findMedian(self):  
        if len(self.max_heap) >= len(self.min_heap):  
            median = -heapq.heappop(self.max_heap)  
        else:  
            median = heapq.heappop(self.min_heap)  

        self.rebalance()  
        return median  

    def rebalance(self):  
        if len(self.max_heap) > len(self.min_heap) + 1:  
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))  
        elif len(self.min_heap) > len(self.max_heap):  
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))  



data = input().split()
t = int(data[0])
index = 1
for _ in range(t):
    medianFinder = MedianFinder()
    while index < len(data) and (n := int(data[index])) != 0:
        index += 1
        if n > 0:
            medianFinder.addNum(n)
        else:
            print(medianFinder.findMedian())
    index += 1