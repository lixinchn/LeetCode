class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        arr_ret = []
        self.do(s, 0, '', 0, arr_ret)
        return arr_ret

    def do(self, s, index, prefix, part, arr_ret):
        if part == 4:
            if index != len(s):
                return

            if index == len(s):
                arr_ret.append(prefix)
                return

        if index == len(s):
            return

        if s[index] > '2':
            self.do(s, index + 1, prefix + ('.' if prefix else '') + s[index], part + 1, arr_ret)
            if index + 1 < len(s):
                self.do(s, index + 2, prefix + ('.' if prefix else '') + s[index] + s[index + 1], part + 1, arr_ret)
        elif s[index] == '2':
            self.do(s, index + 1, prefix + ('.' if prefix else '') + s[index], part + 1, arr_ret)
            if index + 1 < len(s):
                self.do(s, index + 2, prefix + ('.' if prefix else '') + s[index] + s[index + 1], part + 1, arr_ret)
            if index + 2 < len(s):
                if s[index + 1] < '5':
                    self.do(s, index + 3, prefix + ('.' if prefix else '') + s[index] + s[index + 1] + s[index + 2], part + 1, arr_ret)
                elif s[index + 1] == '5' and s[index + 2] <= '5':
                    self.do(s, index + 3, prefix + ('.' if prefix else '') + s[index] + s[index + 1] + s[index + 2], part + 1, arr_ret)
        elif s[index] == '1':
            self.do(s, index + 1, prefix + ('.' if prefix else '') + s[index], part + 1, arr_ret)
            if index + 1 < len(s):
                self.do(s, index + 2, prefix + ('.' if prefix else '') + s[index] + s[index + 1], part + 1, arr_ret)
            if index + 2 < len(s):
                self.do(s, index + 3, prefix + ('.' if prefix else '') + s[index] + s[index + 1] + s[index + 2], part + 1, arr_ret)
        else:
            self.do(s, index + 1, prefix + ('.' if prefix else '') + s[index], part + 1, arr_ret)




if __name__ == "__main__":
    solution = Solution()
    print solution.restoreIpAddresses('25525511135')
    print solution.restoreIpAddresses('0000')