class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_index = {}
        for i in range(len(nums)):
            num = str(nums[i])
            if num in dict_index:
                if i - dict_index[num] > k:
                    dict_index[num] = i
                else:
                    return True
            else:
                dict_index[num] = i
        return False

solution = Solution()
print solution.containsNearbyDuplicate([2,2,2], 1)