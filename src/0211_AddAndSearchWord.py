class TrieNode:
    def __init__(self):
        self.value = 0
        self.children = [None] * 26

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = TrieNode()
        self.count = 0
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.trie
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                p.children[idx] = TrieNode()
            p = p.children[idx]
        self.count += 1
        p.value = self.count
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search2(word, 0, self.trie)

    def search2(self, word, pos, p):
        if pos == len(word):
            if p.value == 0:
                return False
            else:
                return True
        else:
            if word[pos] == '.':
                for pp in p.children:
                    if pp:
                        if self.search2(word, pos + 1, pp):
                            return True
                return False
            else:
                idx = ord(word[pos]) - ord('a')
                if not p.children[idx]:
                    return False
                else:
                    return self.search2(word, pos + 1, p.children[idx])


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("ddd")
print wordDictionary.search("ddd")
print wordDictionary.search("word")