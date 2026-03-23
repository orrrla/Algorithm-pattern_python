def lower_bound(nums,target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums,target)
        if start==len(nums) or nums[start]!=target :return [-1,-1]
        end = lower_bound(nums,target+1)-1
        return [start,end]
