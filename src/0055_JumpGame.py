class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can_jump = False
        len_num = len(nums)
        maximum_length = 0
        # if len_num == 1:
        #     return True
        for i in range(len_num):
            num = nums[i]
            this_length = i + num
            if this_length > maximum_length:
                maximum_length = this_length
                if maximum_length >= len_num:
                    break
            if maximum_length <= i:
                break
        return maximum_length >= len_num - 1

        
if __name__ == "__main__":
    solution = Solution()
    print solution.canJump([2,3,1,1,4])
    print solution.canJump([3,2,1,0,4])
    print solution.canJump([0])
    print solution.canJump([0,1])
    print solution.canJump([2,0,0])
