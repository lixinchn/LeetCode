class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        all_len = len(nums)
        middle = all_len / 2
        if nums[middle] == target:
            return middle

        if target < nums[middle]:
            if nums[0] <= nums[middle] and target >= nums[0]:
                return self.search(nums[:middle], target)
            elif nums[-1] >= nums[middle] and target <= nums[-1]:
                return self.search(nums[:middle], target)
            else:
                result = self.search(nums[middle + 1:], target)
                return result if result == -1 else middle + result + 1
        if target > nums[middle]:
            if nums[-1] >= nums[middle] and target <= nums[-1]:
                result = self.search(nums[middle + 1:], target)
                return result if result == -1 else middle + result + 1
            elif nums[0] <= nums[middle] and target >= nums[0]:
                result = self.search(nums[middle + 1:], target)
                return result if result == -1 else middle + result + 1
            else:
                return self.search(nums[:middle], target)

if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,5]
    print solution.search(nums, 5)