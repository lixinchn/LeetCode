class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = []
        for i in range(len(nums)):
            num = nums[i]
            if not self.dp:
                self.dp.append(num)
            else:
                self.dp.append(self.dp[-1] + num)

        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] if i == 0 else self.dp[j] - self.dp[i - 1]
        


# Your NumArray object will be instantiated and called as such:
nums = [1,2,3,4,5]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)