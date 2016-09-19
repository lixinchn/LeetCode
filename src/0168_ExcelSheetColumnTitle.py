class Solution(object):
    char_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret_str = ''
        while n > 0:
            remainder = (n - 1) % 26
            ret_str = self.char_arr[remainder] + ret_str
            n = (n - 1) / 26
        return ret_str

        
if __name__ == "__main__":
    solution = Solution()
    print solution.convertToTitle(3)
    print solution.convertToTitle(28)
    print solution.convertToTitle(26)