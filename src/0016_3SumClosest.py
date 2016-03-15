class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        index = 0
        biggest = 2 << 31 - 1
        ret = 0
        while True:
            if index >= len(nums) - 2:
                break
            if index != 0 and nums[index] == nums[index - 1]:
                index += 1
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                minus = 1
                target_result = nums[left] + nums[right] + nums[index]
                result = target_result - target
                if result < 0:
                    minus = -1
                    result = result * minus
                if result < biggest:
                    ret = target_result
                    biggest = result
                if result * minus > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
            index += 1
        return ret

if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 2, 1, -4]
    print solution.threeSumClosest(nums, 1)

    nums = [-2, 0, 1, 1, 2]
    print solution.threeSumClosest(nums, 0)

    nums = [0, 2, 1, -3]
    print solution.threeSumClosest(nums, 1)

