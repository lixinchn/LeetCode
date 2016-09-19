class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_count = {}
        len_num = len(nums)

        for num in nums:
            if str(num) in dict_count:
                dict_count[str(num)] += 1
            else:
                dict_count[str(num)] = 1

            if dict_count[str(num)] > len_num / 2:
                return num
            
        
if __name__ == "__main__":
    solution = Solution()
    print solution.majorityElement([1])