class Solution(object):
    def combinationSum2(self, candidates, target):
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
            last_next = candidates[last_index + 1] if last_index + 1 < len_candidates else -1
            if last_next == last:
                continue
            target_temp = target - last
            if target_temp < 0:
                continue
            arr_temp = arr + [last]
            if self.do(candidates[:last_index], target_temp, arr_temp, arr_ret):
                arr_temp.reverse()
                arr_ret.append(arr_temp)
        
if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum2([10,1,2,7,6,1,5], 8)