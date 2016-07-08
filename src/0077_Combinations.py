class Solution(object):
    ret_arr = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ret_arr = []
        self.do(n, k, [], 1)
        return self.ret_arr
        
    def do(self, n, k, arr, index):
        if n - index + 1 < k - len(arr):
            return
        if len(arr) == k:
            self.ret_arr.append(arr)
            return

        while index <= n:
            self.do(n, k, arr + [index], index + 1)
            index += 1

if __name__ == "__main__":
    solution = Solution()
    print solution.combine(4, 2)
