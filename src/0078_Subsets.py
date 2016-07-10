class Solution(object):
    ret_arr = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ret_arr = []
        self.do(nums, [], 0)
        return self.ret_arr
        
    def do(self, nums, arr, index):
        self.ret_arr.append(arr)

        while index < len(nums):
            self.do(nums, arr + [nums[index]], index + 1)
            index += 1

if __name__ == "__main__":
    solution = Solution()
    print solution.subsets([1,2,3,6])