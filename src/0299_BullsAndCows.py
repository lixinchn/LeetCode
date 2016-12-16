class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        arr_index_bulls = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                guess = guess[:i] + '*' + guess[i + 1:]
                secret = secret[:i] + '#' + secret[i + 1:]

        secret = ''.join(sorted(secret))
        guess = ''.join(sorted(guess))

        i = 0
        j = 0
        while i < len(secret) and j < len(guess):
            if secret[i] > guess[j]:
                j += 1
            elif secret[i] < guess[j]:
                i += 1
            else:
                cows += 1
                i += 1
                j += 1
        return '%sA%sB' % (bulls, cows)

solution = Solution()
print solution.getHint('1123', '0111')
