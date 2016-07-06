class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count1 = {}
        count2 = {}
        for char in t:
            if char not in count1:
                count1[char] = 1
            else:
                count1[char] += 1
        for char in t:
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1
        count = len(t)
        start = 0
        minSize = 100000
        minStart = 0
        for end in range(len(s)):
            if s[end] in count2 and count2[s[end]] > 0:
                count1[s[end]] -= 1
                if count1[s[end]] >= 0:
                    count -= 1
            if count == 0:
                while True:
                    if s[start] in count2 and count2[s[start]] > 0:
                        if count1[s[start]] < 0:
                            count1[s[start]] += 1
                        else:
                            break
                    start += 1
                if minSize > end - start + 1:
                    minSize = end - start + 1
                    minStart = start
        if minSize==100000:
            return ''
        else:
            return s[minStart : minStart + minSize]


        
if __name__ == "__main__":
    solution = Solution()
    print solution.minWindow('ADOBECODEBANC', 'ABC')