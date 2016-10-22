class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ret_arr = []
        self.do(k, n, [], 1)
        return self.ret_arr

    def do(self, k, n, arr, start):
        if k == 1:
            if n <= 9 and n >= start and n not in arr:
                arr.append(n)
                self.ret_arr.append(arr)
            return

        for i in range(start, 10):
            new_arr = arr[:]
            new_arr.append(i)
            self.do(k - 1, n - i, new_arr, i + 1)


if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum3(2, 18)