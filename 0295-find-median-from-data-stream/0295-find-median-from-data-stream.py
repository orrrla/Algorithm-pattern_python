import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
    def addNum(self, num: int) -> None:
        # heapq.heappush(self.left, -num)  # 存负数
        
        # 移动左堆最大到右堆
        heapq.heappush(self.right, num)

        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))  # 存负数
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]  # 取负得到原值
        return (-self.left[0] + self.right[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()