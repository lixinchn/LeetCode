class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_all = 0
        for num in nums:
            xor_all ^= num


        for i in range(32):
            if xor_all >> i == 1:
                break


        xor_half = 0
        for num in nums:
            if (num >> i) & 1 == 1:
                xor_half ^= num


        return [xor_half, xor_all ^ xor_half]

solution = Solution()
print solution.singleNumber([1,2,1,3,2,5])