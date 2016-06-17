import math
class Solution(object):
    ret_str = ''

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.do(n, k, [9, 8, 7, 6, 5, 4, 3, 2, 1])
        return self.ret_str

    def do(self, n, k, arr_int):
        len_ret = len(self.ret_str)
        if len_ret == n:
            while len(self.ret_str) < n:
                self.ret_str += str(arr_int[-1])
                del arr_int[-1]
            return
        need_to_be_done = math.factorial(n - len_ret - 1)

        index = -1
        while True:
            if need_to_be_done >= k:
                self.ret_str += str(arr_int[index])
                del arr_int[index]
                break
            k -= need_to_be_done
            index -= 1
        self.do(n, k, arr_int)
        


if __name__ == "__main__":
    solution = Solution()
    print solution.getPermutation(3, 2)
