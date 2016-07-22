class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dj = [0]
        index = 1
        while index <= len(s):
            if index == 1:
                if s[index - 1] == '0':
                    return 0
                else:
                    dj.append(1)
                index += 1
                continue

            if s[index - 1] == '0':
                if s[index - 2] != '1' and s[index - 2] != '2':
                    return 0
                dj.append(dj[index - 2] if dj[index - 2] else 1)
            else:
                if s[index - 2] == '1' or (s[index - 2] == '2' and s[index - 1] >= '0' and s[index - 1] <= '6'):
                    temp = dj[index - 2] if dj[index - 2] else 1
                    dj.append(dj[index - 1] + temp)
                else:
                    dj.append(dj[index - 1])
            index += 1
        return dj[len(s)]


if __name__ == "__main__":
    solution = Solution()
    print solution.numDecodings('0')
    print solution.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")