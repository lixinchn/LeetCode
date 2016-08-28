class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_now = 0
        best_i = -1
        total = 0
        for i in range(len(gas)):
            gas_i = gas[i]
            cost_i = cost[i]
            total_now += gas_i - cost_i
            total += total_now
            if total_now >= 0 and best_i == -1:
                best_i = i
            elif total_now < 0:
                best_i = -1
                total_now = 0
        return best_i if total >= 0 else -1

        
if __name__ == "__main__":
    solution = Solution()
    gas = [2,4]
    cost = [3,4]
    print solution.canCompleteCircuit(gas, cost)