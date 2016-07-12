class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_index = 0
        index = 0
        while index < len(nums):
            num = nums[index]
            num_next = nums[index + 1] if index + 1 < len(nums) else 'a'
            if num == num_next:
                nums[new_index] = nums[index]
                nums[new_index + 1] = nums[index]
                new_index += 2
            else:
                nums[new_index] = nums[index]
                new_index += 1

            while index + 1 < len(nums) and nums[index + 1] == num:
                index += 1
            index += 1
        return new_index


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    # nums = [1, 1, 1, 2]
    print solution.removeDuplicates(nums)
    print nums