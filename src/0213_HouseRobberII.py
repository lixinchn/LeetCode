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

        max_val = 0
        for i in range(0, len_nums):
            dp = []
            new_nums = nums[i:] + nums[:i]
            dp.append(new_nums[0])
            dp.append(max(new_nums[0], new_nums[1]))
            for j in range(2, len_nums - 1):
                dp.append(max(dp[j - 2] + new_nums[j], dp[j - 1]))
            max_val = max(max_val, dp[-1])

        return max_val
        
if __name__ == "__main__":
    solution = Solution()
    print solution.rob([1,2,3,4,5])