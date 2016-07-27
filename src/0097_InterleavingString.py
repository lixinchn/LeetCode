class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1 and not s2 and not s3:
            return True
        index1, index2, index3 = 0, 0, 0
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        if len_1 + len_2 != len_3:
            return False
        dj = []

        while index1 <= len_1:
            dj_c = []
            dj.append(dj_c)
            index2 = 0
            while index2 <= len_2:
                if index1 == 0:
                    if index2 == 0:
                        match = False
                    elif index2 == 1:
                        match = s3[index1 + index2 - 1] == s2[index2 - 1]
                    else:
                        match = dj[index1][index2 - 1] and s3[index1 + index2 - 1] == s2[index2 - 1]
                else:
                    if index2 == 0:
                        if index1 == 1:
                            match = s3[index1 + index2 - 1] == s1[index1 - 1]
                        else:
                            match = dj[index1 - 1][index2] and s3[index1 + index2 - 1] == s1[index1 - 1]
                    else:
                        match = (dj[index1 - 1][index2] and s3[index1 + index2 - 1] == s1[index1 - 1]) or (dj[index1][index2 - 1] and s3[index1 + index2 - 1] == s2[index2 - 1])
                dj_c.append(match)
                index2 += 1
            index1 += 1
        return dj[index1 - 1][index2 - 1]



if __name__ == "__main__":
    solution = Solution()
    print solution.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    print solution.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')
    print solution.isInterleave('db', 'b', 'cbb')
    print solution.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")