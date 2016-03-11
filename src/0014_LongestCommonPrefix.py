class Solution(object):
    def checkCommon(self, strs, index):
        temp_char = None
        for i in range(len(strs)):
            s = strs[i]
            if len(s) < index + 1:
                return False
            if not temp_char:
                temp_char = s[index]
            if temp_char != s[index]:
                return False
        return temp_char


    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret_str = ''
        index = 0
        while True:
            temp_char = self.checkCommon(strs, index)
            if temp_char:
                ret_str += temp_char
            else:
                break
            index += 1
        return ret_str

if __name__ == "__main__":
    solution = Solution()
    strs = ['sssabc', 'sssbac', 'sssjjj']
    print solution.longestCommonPrefix(strs)
            