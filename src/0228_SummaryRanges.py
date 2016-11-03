class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        self.arr_ret = []
        for num in nums:
            self.do(num, 0, len(self.arr_ret) - 1)
        return self.arr_ret

    def do(self, num, left, right):
        if left > right:
            self.arr_ret.insert(left, str(num))
            return

        middle = (left + right) / 2
        if '->' in self.arr_ret[middle]:
            arr_line = self.arr_ret[middle].split('->')
            left_num, right_num = int(arr_line[0]), int(arr_line[1])
        else:
            left_num, right_num = int(self.arr_ret[middle]), int(self.arr_ret[middle])

        if num < left_num - 1:
            self.do(num, left, middle - 1)
        elif num == left_num - 1:
            self.arr_ret[middle] = '%s->%s' % (num, right_num)
        elif num >= left_num and num <= right_num:
            return
        elif num == right_num + 1:
            self.arr_ret[middle] = '%s->%s' % (left_num, num)
        else:
            self.do(num, middle + 1, right)

solution = Solution()
print solution.summaryRanges([])
