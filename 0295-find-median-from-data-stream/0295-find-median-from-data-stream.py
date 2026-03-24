import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, - heapq.heappushpop(self.right, num))
        else:
            heapq.heappush(self.right,-heapq.heappushpop(self.left, -num))
        
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]  # 取负得到原值
        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()