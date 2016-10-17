class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        head, tail = 0, -1
        minimum = None
        total = 0
        for i in range(len(nums)):
            num = nums[i]
            total += num
            if total < s:
                continue
            while True:
                if total - nums[tail + 1] >= s:
                    total -= nums[tail + 1]
                    tail += 1
                else:
                    break

            if minimum == None or minimum > i - tail:
                minimum = i - tail
        return minimum or 0

        
if __name__ == "__main__":
    solution = Solution()
    print solution.minSubArrayLen(100, [1,2,3,99])