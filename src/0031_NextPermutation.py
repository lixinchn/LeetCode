class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        modified = False
        while True:
            if i < 0:
                break
            j = i + 1
            if nums[j] > nums[i]:
                k = len(nums) - 1
                while k > i:
                    if nums[k] > nums[i]:
                        break
                    k -= 1
                nums[i], nums[k] = nums[k], nums[i]
                b = nums[j:]
                b.reverse()
                nums[j:] = b
                modified = True
                break
            i -= 1

        if not modified:
            nums.reverse()

if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,1]
    solution.nextPermutation(nums)
    print nums