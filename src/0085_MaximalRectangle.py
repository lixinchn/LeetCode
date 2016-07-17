class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        area = 0
        lst_rec = [0] * len(matrix[0]) if matrix else 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) == 1:
                    lst_rec[j] += 1
                else:
                    lst_rec[j] = 0
            tmp_area = self.largestRectangleArea(lst_rec)
            if tmp_area > area:
                area = tmp_area
        return area

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        top_index_stack = []
        index = 0
        max_area = 0
        while index < len(heights):
            if not top_index_stack or heights[index] >= heights[top_index_stack[-1]]:
                top_index_stack.append(index)
            else:
                while top_index_stack and heights[index] < heights[top_index_stack[-1]]:
                    area = self.calcArea(top_index_stack, index, heights)
                    if area > max_area:
                        max_area = area
                top_index_stack.append(index)
            index += 1

        while top_index_stack:
            area = self.calcArea(top_index_stack, index, heights)
            if area > max_area:
                max_area = area

        return max_area

    def calcArea(self, top_index_stack, index, heights):
        top_index = top_index_stack.pop()
        if top_index_stack:
            area = heights[top_index] * (index - 1 - top_index_stack[-1])
        else:
            area = heights[top_index] * index
        return area

if __name__ == "__main__":
    solution = Solution()
    print solution.maximalRectangle([[1,0,0,1,1,1], [1,0,1,1,0,1], [0,1,1,1,1,1], [0,0,1,1,1,1]])
    print solution.maximalRectangle([['1']])