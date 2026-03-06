class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_flat = [i for row in matrix for i in row]
        left, right = 0, len(matrix_flat)-1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix_flat[mid] == target:
                return True
            elif matrix_flat[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False