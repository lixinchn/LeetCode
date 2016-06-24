class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        str_ret = ''
        max_len = max(len(a), len(b))
        i_a = max_len - (max_len - len(a)) - 1
        i_b = max_len - (max_len - len(b)) - 1
        carry = 0
        for i in range(max_len - 1, -1, -1):
            int_a = int(a[i_a]) if i_a >= 0 else 0
            int_b = int(b[i_b]) if i_b >= 0 else 0
            result = int_a + int_b + carry

            if result == 0:
                str_ret += '0'
                carry = 0
            elif result == 1:
                str_ret += '1'
                carry = 0
            elif result == 2:
                str_ret += '0'
                carry = 1
            elif result == 3:
                str_ret += '1'
                carry = 1
            i_a -= 1
            i_b -= 1
        if carry == 1:
            str_ret += '1'
        return str_ret[::-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.addBinary('11', '1')
