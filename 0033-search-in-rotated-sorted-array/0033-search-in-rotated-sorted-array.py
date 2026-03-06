class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:  # 左半部分有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # target在左半部分
                else:
                    left = mid + 1   # target在右半部分
            else:  # 右半部分有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # target在右半部分
                else:
                    right = mid - 1  # target在左半部分
        
        return -1