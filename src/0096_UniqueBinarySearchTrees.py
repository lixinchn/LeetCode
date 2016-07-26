class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr_ret = [1]
        index = 1
        while index <= n:
            arr_ret.append(0)
            for j in range(index):
                arr_ret[index] += arr_ret[j] * arr_ret[index - 1 - j]
            index += 1
        return arr_ret[n]

if __name__ == "__main__":
    solution = Solution()
    print solution.numTrees(4)