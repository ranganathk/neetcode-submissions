class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if (len(self.large) > 0 and num < self.large[0]):
            heapq.heappush(self.small, -num)
            if len(self.small) > len(self.large) + 1:
                mid = heapq.heappop(self.small)
                heapq.heappush(self.large, -mid)
        else: 
            heapq.heappush(self.large, num)
            if (len(self.large) > len(self.small) + 1):
                mid = heapq.heappop(self.large)
                heapq.heappush(self.small, -mid)
        return

    def findMedian(self) -> float:
        len_small = len(self.small)
        len_large = len(self.large)

        if ((len_small + len_large)%2 == 0):
            return float((-self.small[0] + self.large[0])/2)
        elif len_small > len_large:
            return float(-self.small[0])
        else:
            return float(self.large[0])
            
        