class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        new_nums = []
        for num in nums:
            new_nums.append(str(num))

        new_nums.sort(reverse = True, cmp = lambda x, y: cmp(x + y, y + x))
        largest_num = ''.join(new_nums)
        largest_num = int(largest_num) if largest_num else 0
        return str(largest_num)

if __name__ == "__main__":
    solution = Solution()
    print solution.largestNumber([3,30,34,5,9])
    print solution.largestNumber([0,0,0])
    print solution.largestNumber([0,0,3])
    print solution.largestNumber([])