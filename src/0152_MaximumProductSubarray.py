class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = None
        min_num = None
        max_ret = None
        for num in nums:
            if num > 0:
                if max_num == None:
                    max_num = num
                    min_num = min_num * num if min_num != None else None
                else:
                    max_num = max_num * num
                    min_num = min_num * num if min_num != None else None
            elif num == 0:
                max_num = None
                min_num = None
                if max_ret < num:
                    max_ret = num
            else:
                if min_num == None:
                    min_num = num if max_num == None else max_num * num
                    max_num = None
                else:
                    max_temp = max_num
                    max_num = min_num * num if min_num != None else None
                    min_num = max_temp * num if max_temp != None else num

            if max_ret == None:
                if max_num == None:
                    max_ret = min_num
                else:
                    max_ret = max_num
            elif max_ret < max_num:
                max_ret = max_num

        return max_ret if max_ret else 0

        
if __name__ == "__main__":
    solution = Solution()
    print solution.maxProduct([2,3,-1,4]) == 6
    print solution.maxProduct([-2]) == -2
    print solution.maxProduct([2,1,-1,4]) == 4
    print solution.maxProduct([2,3,-1,7]) == 7
    print solution.maxProduct([2,3,-1,7,-1]) == 42
    print solution.maxProduct([2,3,-1,7,-1,-8]) == 56
    print solution.maxProduct([-2,0,-1]) == 0
    print solution.maxProduct([2,-5,-2,-4,3]) == 24