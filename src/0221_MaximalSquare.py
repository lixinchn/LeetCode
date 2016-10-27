class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        largest_num = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num = matrix[i][j]
                if num == '0':
                    continue
                arr_right_i = [i]
                arr_right_j = [j]
                arr_bottom_i = [i]
                arr_bottom_j = [j]
                new_arr_right_i = []
                new_arr_right_j = []
                new_arr_bottom_i = []
                new_arr_bottom_j = []
                index = 1
                while True:
                    right_i, right_j = arr_right_i.pop(0), arr_right_j.pop(0)
                    bottom_i, bottom_j = arr_bottom_i.pop(0), arr_bottom_j.pop(0)
                    if right_j + 1 >= len(matrix[i]):
                        break
                    if matrix[right_i][right_j + 1] != '1':
                        break
                    if bottom_i + 1 >= len(matrix):
                        break
                    if matrix[bottom_i + 1][bottom_j] != '1':
                        break
                    new_arr_right_i.append(right_i)
                    new_arr_right_j.append(right_j + 1)
                    new_arr_bottom_i.append(bottom_i + 1)
                    new_arr_bottom_j.append(bottom_j)
                    if len(arr_right_i) == 0:
                        if right_j + 1 >= len(matrix[i]):
                            break
                        if right_i + 1 >= len(matrix):
                            break
                        if matrix[right_i + 1][right_j + 1] != '1':
                            break
                        new_arr_right_i.append(right_i + 1)
                        new_arr_right_j.append(right_j + 1)
                        new_arr_bottom_i.append(right_i + 1)
                        new_arr_bottom_j.append(right_j + 1)
                        index += 1
                        arr_right_i, arr_right_j, arr_bottom_i, arr_bottom_j = new_arr_right_i[:], new_arr_right_j[:], new_arr_bottom_i[:], new_arr_bottom_j[:]
                        new_arr_right_i, new_arr_right_j, new_arr_bottom_i, new_arr_bottom_j = [], [], [], []
                if index * index > largest_num:
                    largest_num = index * index
        return largest_num

solution = Solution()
print solution.maximalSquare(["10100","10111","11111","10010"]) == 4
print solution.maximalSquare(["1111","1111","1111"])

