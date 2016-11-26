class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # mean = reduce(lambda x, y: (x + y) / 2, citations)
        h = 0
        len_citations = len(citations)
        citations.sort()
        for i in range(len_citations):
            citation = citations[i]
            now_h = len_citations - i
            if citation >= now_h:
                h = now_h
                break
        return h

solution = Solution()
print solution.hIndex([3,0,6,1,5])
