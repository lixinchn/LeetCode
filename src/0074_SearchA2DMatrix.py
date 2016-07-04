class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        len_matrix = len(matrix)
        start, end = 0, len_matrix - 1
        while True:
            if end < start:
                break
            middle = (start + end) / 2
            line = matrix[middle]
            small_int, big_int = line[0], line[-1]
            if target < small_int:
                end = middle - 1
                continue
            if target > big_int:
                start = middle + 1
                continue
            return self.find_target(line, target)
        return False

    def find_target(self, line, target):
        len_line = len(line)
        start, end = 0, len_line - 1
        while True:
            if end < start:
                break
            middle = (start + end) / 2
            num = line[middle]
            if target < num:
                end = middle - 1
                continue
            if target > num:
                start = middle + 1
                continue
            return True
        return False

        
if __name__ == "__main__":
    solution = Solution()
    print solution.searchMatrix([[1,3,5,7], [10,11,16,20], [23,30,34,50]], 50)
    print solution.searchMatrix([], 1)