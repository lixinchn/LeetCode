class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret_num = 0
        for num in nums:
            ret_num ^= num
        return ret_num

if __name__ == "__main__":
    solution = Solution()
    print solution.singleNumber([1,1,2,2,0])