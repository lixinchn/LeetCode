class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret_arr = []
        last_arr = []
        for i in range(numRows):
            if i == 0:
                ret_arr.append([1])
            elif i == 1:
                ret_arr.append([1, 1])
                last_arr = [1, 1]
            else:
                arr = [1]
                for j in range(0, len(last_arr) - 1):
                    arr.append(last_arr[j] + last_arr[j + 1])

                arr.append(1)
                ret_arr.append(arr)
                last_arr = arr
        return ret_arr

if __name__ == "__main__":
    solution = Solution()
    print solution.generate(50)