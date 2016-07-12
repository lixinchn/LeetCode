class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        path = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    path = {}
                    path[str(i) + '_' + str(j)] = True
                    if self.find(board, word, path, 1, i, j):
                        return True
        return False

    def find(self, board, word, path, index, i, j):
        if index == len(word):
            return True

        if i - 1 >= 0 and str(i - 1) + '_' + str(j) not in path and board[i - 1][j] == word[index]:
            if self.find(board, word, dict(path, **{str(i - 1) + '_' + str(j): True}), index + 1, i - 1, j):
                return True
        if j + 1 < len(board[0]) and str(i) + '_' + str(j + 1) not in path and board[i][j + 1] == word[index]:
            if self.find(board, word, dict(path, **{str(i) + '_' + str(j + 1): True}), index + 1, i, j + 1):
                return True
        if i + 1 < len(board) and str(i + 1) + '_' + str(j) not in path and board[i + 1][j] == word[index]:
            if self.find(board, word, dict(path, **{str(i + 1) + '_' + str(j): True}), index + 1, i + 1, j):
                return True
        if j - 1 >= 0 and str(i) + '_' + str(j - 1) not in path and board[i][j - 1] == word[index]:
            if self.find(board, word, dict(path, **{str(i) + '_' + str(j - 1): True}), index + 1, i, j - 1):
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print solution.exist([['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']], 'AB')

    print solution.exist([['a', 'b']], 'ba')

    print solution.exist([['c', 'a', 'a'], ['a', 'a', 'a'], ['b', 'c', 'd']], 'aab')

    print solution.exist([['a', 'b', 'c', 'e'], ['s', 'f', 'e', 's'], ['a', 'd', 'e', 'e']], 'abcefsadeese')
