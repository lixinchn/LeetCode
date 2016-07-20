class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        num = 2
        arr_ret = [0, 1]
        self.do(n, num, arr_ret)
        return arr_ret

    def do(self, n, num, arr_ret):
        if num > n:
            return

        len_arr = len(arr_ret)
        for index in range(len_arr - 1, -1, -1):
            arr_ret.append((1 << num - 1) + arr_ret[index])

        self.do(n, num + 1, arr_ret)

if __name__ == "__main__":
    solution = Solution()
    print solution.grayCode(0)