class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        loop_range = n / 2 if n % 2 == 0 else n / 2 + 1
        for i in range(loop_range):
            for j in range(i, n - 1 - i):
                matrix[i][j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[i][j]
                matrix[i][j], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[i][j]
                matrix[i][j], matrix[n - 1 - j][i] = matrix[n - 1 - j][i], matrix[i][j]



if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    solution.rotate(matrix)
    print matrix

    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    solution.rotate(matrix)
    print matrix

    matrix = [[1,2], [3,4]]
    solution.rotate(matrix)
    print matrix

    matrix = [[1]]
    solution.rotate(matrix)
    print matrix

