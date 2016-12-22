class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.dp = []
        for i in range(len(matrix)):
            dp = []
            self.dp.append(dp)
            for j in range(len(matrix[i])):
                if i == 0:
                    if j == 0:
                        dp.append(matrix[i][j])
                    else:
                        dp.append(self.dp[i][j - 1] + matrix[i][j])
                else:
                    if j == 0:
                        dp.append(self.dp[i - 1][j] + matrix[i][j])
                    else:
                        dp.append(self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + matrix[i][j])


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        if row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1 - 1]
        if col1 == 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 - 1] + self.dp[row1 - 1][col1 - 1]



# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(0, 1, 2, 3)
print numMatrix.sumRegion(1, 2, 3, 4)
print numMatrix.sumRegion(1, 0, 2, 3)
print numMatrix.sumRegion(0, 0, 2, 3)