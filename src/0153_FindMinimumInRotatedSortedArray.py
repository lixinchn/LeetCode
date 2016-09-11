class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.do(nums, 0, len(nums) - 1)

    def do(self, nums, begin, end):
        if begin == end:
            return nums[begin]

        middle = (begin + end) / 2
        if nums[begin] <= nums[middle] and nums[middle] < nums[end]:
            return nums[begin]
        elif nums[end] < nums[begin] and nums[begin] <= nums[middle]:
            return self.do(nums, middle + 1, end)
        elif nums[middle] < nums[end] and nums[end] < nums[begin]:
            return self.do(nums, begin, middle)

        
if __name__ == "__main__":
    solution = Solution()
    print solution.findMin([0,1,2,3,4,5,6,7])
    print solution.findMin([1,2,3,4,5,6,7,0])
    print solution.findMin([2,3,4,5,6,7,0,1])
    print solution.findMin([3,4,5,6,7,0,1,2])
    print solution.findMin([4,5,6,7,0,1,2,3])
    print solution.findMin([5,6,7,0,1,2,3,4])
    print solution.findMin([6,7,0,1,2,3,4,5])
    print solution.findMin([7,0,1,2,3,4,5,6])
    print solution.findMin([-1])