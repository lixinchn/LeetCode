import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4

        if n % 8 == 7:
            return 4

        i = 0
        while i * i <= n:
            b = int(math.sqrt(n - i * i))
            if i * i + b * b == n:
                return (1 if i > 0 else 0) + (1 if b > 0 else 0)
            i += 1
        return 3

solution = Solution()
print solution.numSquares(13)