class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ret_int = 0
        negative = False
        MAX_INT = 2147483647
        MIN_INT = 2147483648
        i = 0
        for i in range(len(str)):
            if str[i] == ' ' or str[i] == '\t':
                continue
            break
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            negative = str[i] == '-'
            i += 1
        str = str[i:]

        for i in range(len(str)):
            try:
                char_int = int(str[i])
            except:
                break
            ret_int = ret_int * 10 + char_int
            if not negative and ret_int > MAX_INT:
                return MAX_INT
            if negative and ret_int > MIN_INT:
                return MIN_INT * -1

        if negative:
            ret_int *= -1

        return ret_int

if __name__ == "__main__":
    solution = Solution()
    str = '100'
    print solution.myAtoi(str)

    str = '-1'
    print solution.myAtoi(str)

    str = '0'
    print solution.myAtoi(str)

    str = '007'
    print solution.myAtoi(str)

    str = '-007'
    print solution.myAtoi(str)

    str = ''
    print solution.myAtoi(str)

    str = '     '
    print solution.myAtoi(str)

    str = 'a123'
    print solution.myAtoi(str)

    str = '12aa3'
    print solution.myAtoi(str)

    str = '-2147483648'
    print solution.myAtoi(str)

    str = '-2147483649'
    print solution.myAtoi(str)
