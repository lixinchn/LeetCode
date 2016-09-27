class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_b = bin(n)
        str_b = str_b[2:]
        len_str = len(str_b)
        if len_str < 32:
            str_b = '0' * (32 - len_str) + str_b
        str_b = str_b[::-1]
        return int(str_b, 2)

if __name__ == "__main__":
    solution = Solution()
    print solution.reverseBits(43261596)