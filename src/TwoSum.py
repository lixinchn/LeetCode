class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_obj = {}
        ret = []
        for index, num in enumerate(nums):
            if not num in target_obj:
                target_obj[target - num] = index + 1
            else:
                ret = (target_obj[num], index + 1)
                break
        return ret

if __name__ == "__main__":
    solution = Solution()
    ret = solution.twoSum([2, 7, 11, 15], 9)
    print ret
