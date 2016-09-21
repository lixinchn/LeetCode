class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        factor = 5
        while True:
            if n / factor == 0:
                break
            total += n / factor
            factor *= 5
        return total
        

if __name__ == "__main__":
    solution = Solution()
    print solution.trailingZeroes(15)