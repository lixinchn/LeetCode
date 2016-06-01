class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sums = nums[0]
        current_sums = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            current_sums = max(num, current_sums + num)
            max_sums = max(current_sums, max_sums)
        return max_sums

if __name__ == "__main__":
    solution = Solution()
    print solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print solution.maxSubArray([-2])
    print solution.maxSubArray([-2,1])
