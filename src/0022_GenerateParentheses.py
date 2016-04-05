class Solution(object):
    def do(self, ret_arr, sample, n, left_num, right_num, deep):
        if deep == 2 * n:
            ret_arr.append(sample)
            return
        if left_num < n:
            sample += '('
            self.do(ret_arr, sample, n, left_num + 1, right_num, deep + 1)
            sample = sample[:-1]
        if right_num < left_num:
            sample += ')'
            self.do(ret_arr, sample, n, left_num, right_num + 1, deep + 1)
            sample = sample[:-1]

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret_arr = []
        if n != 0:
            self.do(ret_arr, '', n, 0, 0, 0)
        return ret_arr


if __name__ == "__main__":
    solution = Solution()
    print solution.generateParenthesis(2)
