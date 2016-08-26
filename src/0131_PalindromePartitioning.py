class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ret_arr = []
        self.do(s, 0, 1, [])
        return self.ret_arr

    def do(self, s, begin, interval, arr_palindrome):
        temp_s = s[begin:begin + interval]
        if self.is_palindrome(temp_s):
            temp_arr_palindrome = arr_palindrome[:]
            if temp_s:
                temp_arr_palindrome.append(temp_s)
            if begin + interval >= len(s):
                self.ret_arr.append(temp_arr_palindrome)
                return

            new_interval = 1
            self.do(s, begin + interval, new_interval, temp_arr_palindrome)

        if begin + interval + 1 <= len(s):
            self.do(s, begin, interval + 1, arr_palindrome)


    def is_palindrome(self, s):
        i, j = 0, len(s) - 1
        while True:
            if i >= j:
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    print solution.partition('aab')