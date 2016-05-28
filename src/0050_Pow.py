class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1

        ret = x
        if n > 0:
            i = 0
            while i < n - 1:
                if ret > 0 and ret < 1e-16:
                    return 0
                ret *= x
                i += 1
            return ret

        if n < 0:
            n *= -1
            i = 0
            while i < n - 1:
                if ret > 0 and 1 / ret < 1e-16:
                    return 0
                ret *= x
                i += 1
            ret = 1 / ret
            return ret

if __name__ == "__main__":
    solution = Solution()
    print solution.myPow(2, 2) == 4
    print solution.myPow(2.5, 2) == 6.25
    print solution.myPow(2.1, 1) == 2.1
    print solution.myPow(-2.1, 1) == -2.1
    print solution.myPow(-2.5, -1) == -0.4
    print solution.myPow(-2.5, 3) == -15.625
    print solution.myPow(-2.5, -2) == 0.16
    print solution.myPow(0.00001, 2147483647) == 0
    print solution.myPow(2.00000, -2147483648) == 0
    print solution.myPow(-1.00000, 2147483647) == -1