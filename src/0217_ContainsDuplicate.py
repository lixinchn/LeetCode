class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) and len(nums) != 0

if __name__ == "__main__":
    solution = Solution()
    print solution.containsDuplicate([1,2,3])