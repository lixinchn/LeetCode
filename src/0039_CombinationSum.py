class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr_ret = []
        candidates.sort()
        if not candidates or target < candidates[0] or target <= 0:
            return arr_ret
        self.do(candidates, target, [], arr_ret)
        return arr_ret

    def do(self, candidates, target, arr, arr_ret):
        if target == 0:
            return True
        if not candidates or target < candidates[0]:
            return False

        len_candidates = len(candidates)
        for i in range(len_candidates):
            last_index = len_candidates - 1 - i
            last = candidates[last_index]
            time = 0
            while True:
                time += 1
                target_temp = target - last * time
                if target_temp < 0:
                    break
                arr_temp = arr + [last for x in range(time)]
                if self.do(candidates[:last_index], target_temp, arr_temp, arr_ret):
                    arr_temp.reverse()
                    arr_ret.append(arr_temp)


        
if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum([7,3,9,6], 6)