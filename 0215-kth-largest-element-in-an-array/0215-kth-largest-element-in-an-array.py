class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
    
        # 第一步：找到最大值和最小值
        min_val = min(nums)
        max_val = max(nums)
        
        # 计算范围
        range_size = max_val - min_val + 1
        
        # 创建计数数组
        count = [0] * range_size
        
        # 统计每个数字出现的次数
        for num in nums:
            count[num - min_val] += 1
        
        # 从大到小遍历，找第k个最大的
        remaining = k
        for i in range(range_size - 1, -1, -1):
            if count[i] >= remaining:
                return i + min_val
            remaining -= count[i]
        
        return None