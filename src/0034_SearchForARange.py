class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.doSearch(nums, target, 0)

    def doSearch(self, nums, target, start):
        if not nums:
            return [-1, -1]
        len_nums = len(nums)
        middle = len_nums / 2
        if nums[middle] == target:
            left = self.doSearch(nums[:middle], target, start)[0]
            right = self.doSearch(nums[middle + 1:], target, start + middle + 1)[1]
            return [left if left != -1 else middle + start, right if right != -1 else middle + start]
        if nums[middle] < target:
            return self.doSearch(nums[middle + 1:], target, start + middle + 1)
        if nums[middle] > target:
            return self.doSearch(nums[:middle], target, start)

if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,2,3,4,4,4,5]
    print solution.searchRange(nums, 5)