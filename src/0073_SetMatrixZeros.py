class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = set([])
        column = set([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        sorted(column)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row:
                    matrix[i][j] = 0
                if j in column:
                    matrix[i][j] = 0
        
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3], [0,1,2]]
    solution.setZeroes(matrix)
    print matrix

    matrix = [[0]]
    solution.setZeroes(matrix)
    print matrix