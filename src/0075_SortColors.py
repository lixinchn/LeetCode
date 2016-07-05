class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        index_1, index_2 = len_nums - 1, len_nums - 1
        index = -1
        while index + 1 < len_nums:
            index += 1
            num = nums[index]
            if num == 0:
                continue
            if num == 1 and index < index_1:
                nums[index], nums[index_1] = nums[index_1], nums[index]
                index_1 -= 1
                if nums[index] != 0:
                    index -= 1
                continue
            if num == 2 and index < index_2:
                nums[index], nums[index_2] = nums[index_2], nums[index]
                if index_1 >= index_2 and nums[index_2] == 2:
                    index_1 -= 1
                index_2 -= 1
                if nums[index] != 0:
                    index -= 1
                continue

if __name__ == "__main__":
    a = [0,1,2,1,1,1,0,2,2,2,2,0,0,1]
    from random import shuffle
    shuffle(a)
    solution = Solution()
    solution.sortColors(a)
    print a
