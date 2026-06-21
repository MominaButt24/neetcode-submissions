class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if target > matrix[i][c - 1]:
                continue
            left = 0
            right = c -1
            while left <= right:
                mid = (right + left) // 2
                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return False