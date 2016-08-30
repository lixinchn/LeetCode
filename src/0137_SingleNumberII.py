class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = []
        ret_num = 0
        for i in range(32):
            count.append(0)
            for num in nums:
                if (num >> i & 1):
                    count[i] += 1
            ret_num |= (count[i] % 3) << i
        if ret_num >> 31:
            ret_num = -1 * ((~(ret_num - 1)) & ((1 << 32) - 1))
        return ret_num

        
if __name__ == "__main__":
    solution = Solution()
    print solution.singleNumber([-1])