class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2147483647
        ret_int = 0
        negative = False
        if x < 0:
            x = 0 - x
            negative = True

        while x:
            remainder = x % 10
            ret_int = ret_int * 10 + remainder
            x = x / 10

        if ret_int > MAX_INT:
            return 0

        if negative:
            ret_int = 0 - ret_int

        return ret_int

if __name__ == "__main__":
    solution = Solution()
    x = 100
    print solution.reverse(x)

    x = -100
    print solution.reverse(x)
    