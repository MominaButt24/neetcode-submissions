class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        newList = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # for t in range(n-i):
            #     newList.append(matrix[i][t])
            # for r in range(i+1, n):
            #     newList.append(matrix[r][n-i-1])
            # for b in range(n-i-2, i+1):
            #     newList.append(matrix[n-i-1][b])
            # for l in range(n-i-2, i):
            #     newList.append(matrix[l][i])

            for i in range(left, right):
                newList.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                newList.append(matrix[i][right-1])
            right -= 1

            if not (left<right and top<bottom):
                break
            for i in range(right-1, left-1, -1):
                newList.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                newList.append(matrix[i][left])
            left += 1
        return newList
