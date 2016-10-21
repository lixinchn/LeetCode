class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i, j = 1, len(nums) - 1
        flag = nums[0]
        while True:
            if i > j:
                if len(nums) - (i - 1) == k:
                    return flag
                elif len(nums) - (i - 1) > k:
                    return self.findKthLargest(nums[i:], k)
                else:
                    return self.findKthLargest(nums[1:i], k - (len(nums) - (i - 1)))
                break
            if nums[i] <= flag:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1


if __name__ == "__main__":
    solution = Solution()
    print solution.findKthLargest([3], 1)