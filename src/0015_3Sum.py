class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        all_ret = []
        nums.sort()
        index = 0
        while True:
            if index >= len(nums) - 2:
                break
            if index != 0 and nums[index] == nums[index - 1]:
                index += 1
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + nums[index] == 0:
                    ret = []
                    ret.append(nums[index])
                    ret.append(nums[left])
                    ret.append(nums[right])
                    all_ret.append(ret)
                if nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]: right -= 1
                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: left += 1
            index += 1
        return all_ret

if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, 4]
    print solution.threeSum(nums)

    solution = Solution()
    nums = [0, 0, 0]
    print solution.threeSum(nums)

    solution = Solution()
    nums = [-2, 0, 1, 1, 2]
    print solution.threeSum(nums)
