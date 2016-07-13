class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        nums = set(nums)
        nums = list(nums)
        return self.do(nums, target)

    def do(self, nums, target):
        if not nums:
            return False
        all_len = len(nums)
        middle = all_len / 2
        if nums[middle] == target:
            return True

        if target < nums[middle]:
            if nums[0] <= nums[middle] and target >= nums[0]:
                return self.search(nums[:middle], target)
            elif nums[-1] >= nums[middle] and target <= nums[-1]:
                return self.search(nums[:middle], target)
            else:
                return self.search(nums[middle + 1:], target)
        if target > nums[middle]:
            if nums[-1] >= nums[middle] and target <= nums[-1]:
                return self.search(nums[middle + 1:], target)
            elif nums[0] <= nums[middle] and target >= nums[0]:
                return self.search(nums[middle + 1:], target)
            else:
                return self.search(nums[:middle], target)

if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,1,1]
    print solution.search(nums, 3)