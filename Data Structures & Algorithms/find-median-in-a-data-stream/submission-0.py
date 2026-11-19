class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr = [x for x in self.arr if x <= num] + [num] + [x for x in self.arr if x > num]
        return

    def findMedian(self) -> float:
        mid = len(self.arr)//2
        if len(self.arr) % 2:
            return float(self.arr[mid])
        else:
            return float((self.arr[mid-1] + self.arr[mid])/2)