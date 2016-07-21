class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(0, 0, [], res, nums)
        return res

    def dfs(self, depth, start, value_list, res, nums):
        if value_list not in res:
            res.append(value_list)
        if depth == len(nums):
            return
        for i in range(start, len(nums)):
            self.dfs(depth + 1, i + 1, value_list + [nums[i]], res, nums)

        

if __name__ == "__main__":
    solution = Solution()
    print solution.subsetsWithDup([1,2,2])

    print solution.subsetsWithDup([-1,1,2])