class Solution(object):
    def gen_arr_needle(self, needle):
        arr_needle = [0]
        j = 0
        i = 1
        while True:
            if i == len(needle):
                return arr_needle
            if needle[i] == needle[j]:
                arr_needle.append(j + 1)
                i += 1
                j += 1
            else:
                if j == 0:
                    arr_needle.append(0)
                    i += 1
                else:
                    j = arr_needle[j - 1]

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1

        arr_needle = self.gen_arr_needle(needle)
        i, j, len_needle = 0, 0, len(needle)
        while True:
            if i == len(haystack):
                break
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len_needle:
                    break
            else:
                if j == 0:
                    i += 1
                else:
                    j = arr_needle[j - 1]
        if j == len_needle:
            return i - j
        return -1

if __name__ == "__main__":
    solution = Solution()
    print solution.strStr('', '')
    # 