class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 1:
            return

        #  simpler way to reverse
        matrix.reverse()
        # t = 0
        # b = len(matrix) - 1
        # while t <= b:
        #     matrix[t] , matrix[b]=  matrix[b], matrix[t]
        #     t+=1
        #     b-=1

        for k in range(len(matrix) - 1):
            for t in range(k+1, len(matrix)):
                matrix[k][t], matrix[t][k] = matrix[t][k], matrix[k][t]

