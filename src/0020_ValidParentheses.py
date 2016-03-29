class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr_tmp = []
        for i in range(len(s)):
            char = s[i]
            if char == ')' or char == '}' or char == ']':
                if len(arr_tmp) == 0:
                    return False
                match_char = arr_tmp.pop()
                if char == ')' and match_char != '(':
                    return False
                if char == '}' and match_char != '{':
                    return False
                if char == ']' and match_char != '[':
                    return False
            else:
                arr_tmp.append(char)
        return len(arr_tmp) == 0

if __name__ == "__main__":
    solution = Solution()
    s = '(){}'
    print solution.isValid(s)