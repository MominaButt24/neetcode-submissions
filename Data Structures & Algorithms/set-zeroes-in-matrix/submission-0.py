class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        freq = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    freq.add((i, j))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and (i, j) in freq:
                    for k in range(len(matrix[0])):
                        matrix[i][k] = 0
                    for k in range(len(matrix)):
                        matrix[k][j] = 0
        