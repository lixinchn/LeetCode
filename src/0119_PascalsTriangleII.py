class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        last_arr = []
        for i in range(rowIndex + 1):
            if i == 1:
                last_arr = [1, 1]
            else:
                arr = [1]
                for j in range(0, len(last_arr) - 1):
                    arr.append(last_arr[j] + last_arr[j + 1])

                arr.append(1)
                last_arr = arr
        return last_arr

if __name__ == "__main__":
    solution = Solution()
    print solution.getRow(2)