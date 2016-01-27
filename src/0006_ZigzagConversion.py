# http://www.cnblogs.com/TenosDoIt/p/3738693.html
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= numRows:
            return s

        ret_s = ''
        interval = numRows * 2 - 2

        # first row
        i = 0
        while i < len(s):
            ret_s += s[i]
            i += interval

        # middle rows:
        i = 1
        while i < numRows - 1:
            j = i
            mutable_interval = interval - 2 * i
            while j < len(s):
                ret_s += s[j]
                j += mutable_interval
                mutable_interval = interval - mutable_interval
            i += 1

        # last row
        i = numRows - 1
        while i < len(s):
            ret_s += s[i]
            i += interval

        return ret_s
   

if __name__ == "__main__":
    solution = Solution()
    s = 'PAYPALISHIRING'
    print solution.convert(s, 3)

