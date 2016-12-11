class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i_zero, i_none_zero, len_nums = 0, 0, len(nums)
        while i_zero < len_nums:
            if nums[i_zero] != 0:
                i_zero += 1
                continue
            else:
                while i_none_zero <= i_zero or (i_none_zero < len_nums and nums[i_none_zero] == 0):
                    i_none_zero += 1
                if i_none_zero >= len_nums:
                    return
                nums[i_zero], nums[i_none_zero] = nums[i_none_zero], nums[i_zero]
                i_zero += 1

solution = Solution()
nums = [1,2,3,0,0]
solution.moveZeroes(nums)
print nums

