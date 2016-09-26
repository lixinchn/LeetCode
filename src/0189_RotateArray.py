class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums
        # nums[len_nums - k:] + nums[:len_nums - k]
        nums.reverse()
        temp = []
        for i in range(k, len_nums):
            temp.append(nums.pop())
        nums.reverse()
        nums += temp
        
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    solution.rotate(nums, 3)
    print nums