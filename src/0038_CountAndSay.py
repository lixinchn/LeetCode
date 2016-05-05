class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''

        ret_str = '1'
        for i in range(n - 1):
            temp_str = ret_str
            how_many = 0
            previous_char = ''
            applied = False
            for j in range(len(temp_str)):
                if temp_str[j] != previous_char and how_many != 0:
                    ret_str = str(how_many) + previous_char if not applied else ret_str + str(how_many) + previous_char
                    how_many = 0
                    applied = True
                how_many += 1
                previous_char = temp_str[j]
            ret_str = str(how_many) + previous_char if not applied else ret_str + str(how_many) + previous_char
        return ret_str
        
if __name__ == "__main__":
    solution = Solution()
    print solution.countAndSay(6)
