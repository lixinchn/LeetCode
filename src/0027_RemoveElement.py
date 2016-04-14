class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_nums_point = -1
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            new_nums_point += 1
            nums[new_nums_point] = nums[i]
        return new_nums_point + 1
        

if __name__ == "__main__":
    solution = Solution()
    nums = []
    print solution.removeElement(nums, 3)
