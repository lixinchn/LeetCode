class Solution(object):
    def permuteUnique(self, nums):
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
            ret_nums = self.remove_duplicate(ret_nums)
        return ret_nums

    def merge(self, ret_num, num):
        arr = []
        for i in range(len(ret_num) + 1):
            temp = list(ret_num)
            temp.insert(i, num)
            arr.append(temp)
        return arr

    def remove_duplicate(self, ret_nums):
        temp_nums = []
        temp_ints = {}
        for ret_num in ret_nums:
            num = ''.join(map(str, ret_num))
            if num not in temp_ints:
                temp_ints[num] = True
                temp_nums.append(ret_num)
        return temp_nums



if __name__ == "__main__":
    solution = Solution()
    print solution.permuteUnique([1,1,2])