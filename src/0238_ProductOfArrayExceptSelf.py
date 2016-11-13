class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs = 1
        zero_num = 0
        zero_index = -1
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zero_index = i
                zero_num += 1
                if zero_num > 1:
                    return [0] * len(nums)
                continue
            rs *= num

        if zero_index >= 0:
            return [0] * zero_index + [rs] + [0] * (len(nums) - zero_index - 1)

        ret_arr = []
        for i in range(len(nums)):
            num = nums[i]
            ret_arr.append(rs / num)
        return ret_arr

solution = Solution()
print solution.productExceptSelf([1,2,3,4])
print solution.productExceptSelf([0,1,2,3,4])
print solution.productExceptSelf([1,2,3,0,4])
print solution.productExceptSelf([1,2,3,4,0])
print solution.productExceptSelf([0,1,2,3,4,0])
