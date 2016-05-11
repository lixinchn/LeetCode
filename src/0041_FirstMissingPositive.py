class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        len_num = len(nums)
        i = 0
        while i < len_num:
            num = nums[i]
            if num <= 0 or num >= len_num or nums[num - 1] == num:
                i += 1
                continue
            nums[num - 1], nums[i] = nums[i], nums[num - 1]
            
        for i in range(len_num):
            if nums[i] - 1 == i:
                continue
            return i + 1
        return len_num + 1

        
if __name__ == "__main__":
    solution = Solution()
    print solution.firstMissingPositive([-1,4,2,1,9,10])
