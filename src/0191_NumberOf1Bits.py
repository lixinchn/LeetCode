class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeros_num = 0
        while n > 0:
            if n % 2 == 1:
                zeros_num += 1
            n = n / 2
        return zeros_num

if __name__ == "__main__":
    solution = Solution()
    print solution.hammingWeight(256)