class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_1 = len(word1)
        len_2 = len(word2)
        dp_arr = []
        dp_arr.append([i for i in range(len_1 + 1)])
        for i in range(1, len_2 + 1):
            arr = [i]
            dp_arr.append(arr)

        for i in range(1, len_2 + 1):
            arr = dp_arr[i]
            for j in range(1, len_1 + 1):
                char_1 = word1[j - 1]
                char_2 = word2[i - 1]
                if char_1 == char_2:
                    arr.append(dp_arr[i - 1][j - 1])
                else:
                    arr.append(min(dp_arr[i][j - 1], dp_arr[i - 1][j - 1], dp_arr[i - 1][j]) + 1)

        return dp_arr[len_2][len_1]
        

if __name__ == "__main__":
    solution = Solution()
    print solution.minDistance('a', '')