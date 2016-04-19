class Solution(object):
    MAX_INT = 2147483647
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        symbol = 1
        if dividend < 0:
            symbol *= -1
            dividend *= -1
        if divisor < 0:
            symbol *= -1
            divisor *= -1

        arr_symbols = []
        i = 0
        while dividend - (divisor << i) >= 0:
            arr_symbols.append(1)
            i += 1

        quotient = 0
        i -= 1
        while dividend >= divisor:
            if dividend - divisor * (1 << i) >= 0:
                quotient += 1 << i
                dividend -= divisor * (1 << i)
            i -= 1
        ret_val = quotient * symbol
        if ret_val > self.MAX_INT:
            return self.MAX_INT
        return ret_val

if __name__ == "__main__":
    solution = Solution()
    print solution.divide(0, -1)