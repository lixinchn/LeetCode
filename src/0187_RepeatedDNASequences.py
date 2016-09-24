class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret_arr = []
        map_dna = {}
        len_s = len(s)
        for i in range(len_s):
            if i + 10 > len_s:
                break
            child_s = s[i:i + 10]
            if child_s not in map_dna:
                map_dna[child_s] = 1
            else:
                if map_dna[child_s] == 1:
                    ret_arr.append(child_s)
                map_dna[child_s] += 1
        return ret_arr
        
if __name__ == "__main__":
    solution = Solution()
    print solution.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    print solution.findRepeatedDnaSequences('AAAAAA')