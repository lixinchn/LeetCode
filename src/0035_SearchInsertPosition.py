class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1

        len_nums = len(nums)
        middle = len_nums / 2 - 1
        middle_next = middle + 1
        if nums[middle] == target:
            return middle
        if nums[middle_next] == target:
            return middle_next
        if nums[middle] < target and nums[middle_next] > target:
            return middle_next
        if nums[middle] > target:
            return self.searchInsert(nums[:middle], target)
        if nums[middle_next] < target:
            return middle_next + 1 + self.searchInsert(nums[middle_next + 1:], target)

        
if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,5,6]
    print solution.searchInsert(nums, 0)