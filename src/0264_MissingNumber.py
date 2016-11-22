class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        xor_all = 0
        for i in range(len_nums + 1):
            xor_all ^= i

        for num in nums:
            xor_all ^= num

        return xor_all

solution = Solution()
print solution.missingNumber([0,1,3])