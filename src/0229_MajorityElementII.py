class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_a, num_b, count_a, count_b = 0, 0, 0, 0
        for num in nums:
            if num == num_a:
                count_a += 1
            elif num == num_b:
                count_b += 1
            elif count_a == 0:
                num_a = num
                count_a += 1
            elif count_b == 0:
                num_b = num
                count_b += 1
            else:
                count_a -= 1
                count_b -= 1

        count_a, count_b = 0, 0
        for num in nums:
            if num == num_a:
                count_a += 1
            elif num == num_b:
                count_b += 1

        ret = []
        if count_a > len(nums) / 3:
            ret.append(num_a)
        if count_b > len(nums) / 3:
            ret.append(num_b)
        return ret

solution = Solution()
# print solution.majorityElement([1,1,2,2,5])
print solution.majorityElement([1,2])