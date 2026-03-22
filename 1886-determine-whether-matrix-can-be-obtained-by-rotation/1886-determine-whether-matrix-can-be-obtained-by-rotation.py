class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n - i - 1):
                top = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = top

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4): #checks 4 times as after 4 times its same as original matrix
            if mat == target:
                return True
            self.rotate(mat)
        return False