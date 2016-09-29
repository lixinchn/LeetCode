class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]
        if len_nums == 2:
            return max(nums[0], nums[1])

        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len_nums):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))

        return dp[len_nums - 1]
        
if __name__ == "__main__":
    solution = Solution()
    print solution.rob([1,2,3,4,5])