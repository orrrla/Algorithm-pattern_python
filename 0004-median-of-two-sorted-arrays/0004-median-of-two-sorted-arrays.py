class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 合并两个数组
        merged = []
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # 添加剩余元素
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        # 找中位数
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n//2 - 1] + merged[n//2]) / 2