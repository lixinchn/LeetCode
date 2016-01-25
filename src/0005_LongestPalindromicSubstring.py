# more info: http://www.cnblogs.com/TenosDoIt/p/3675788.html
class Solution(object):
    def pre_process_str(self, s):
        ret_s = '#'
        for i in range(len(s)):
            ret_s = ret_s + s[i] + '#'
        return ret_s

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_s = self.pre_process_str(s)
        p = [0 for i in range(len(temp_s))]
        mx, idx = 0, 0
        for i in range(len(temp_s) - 1):
            p[i] = min(p[2 * idx - i], mx - i) if mx > i else 1

            while temp_s[i + p[i]] == temp_s[i - p[i]]:
                p[i] = p[i] + 1
                if i + p[i] >= len(temp_s):
                    break

            if i + p[i] > mx:
                mx = i + p[i]
                idx = i
            if mx == len(temp_s):
                break

        max_len, index = 0, 0
        for i in range(len(p)):
            if p[i] - 1 > max_len:
                max_len = p[i] - 1
                index = i

        return s[(index - max_len) / 2:(index + max_len) / 2]

if __name__ == "__main__":
    solution = Solution()
    s = 'abacdfgdcaba'
    print solution.longestPalindrome(s)

