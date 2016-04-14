class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        new_nums_point = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[new_nums_point]:
                continue
            new_nums_point += 1
            nums[new_nums_point] = nums[i]
        
        return new_nums_point + 1

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    print solution.removeDuplicates(nums)