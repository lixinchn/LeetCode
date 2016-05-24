class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ret_nums = [[nums[0]]]
        len_num = len(nums)
        for i in range(1, len_num):
            num = nums[i]
            temp_nums = []
            for ret_num in ret_nums:
                temp_nums.extend(self.merge(ret_num, num))
            ret_nums = temp_nums
        return ret_nums

    def merge(self, ret_num, num):
        arr = []
        for i in range(len(ret_num) + 1):
            temp = list(ret_num)
            temp.insert(i, num)
            arr.append(temp)
        return arr

        

if __name__ == "__main__":
    solution = Solution()
    print solution.permute([1,2])