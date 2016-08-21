class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s = len(s)
        i = 0
        j = len_s - 1
        while True:
            if i >= j:
                break
            if not (s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z' or s[i] >= '0' and s[i] <= '9'):
                i += 1
                continue
            if not (s[j] >= 'a' and s[j] <= 'z' or s[j] >= 'A' and s[j] <= 'Z' or s[j] >= '0' and s[j] <= '9'):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

        
if __name__ == "__main__":
    solution = Solution()
    print solution.isPalindrome("A man, a plan, a canal: Panama")
    print solution.isPalindrome("race a car")
    print solution.isPalindrome("")
    print solution.isPalindrome("a")
    print solution.isPalindrome("0P")
    print solution.isPalindrome("ab2a")