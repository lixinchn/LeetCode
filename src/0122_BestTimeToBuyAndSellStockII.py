class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        profit = 0
        previous = -1
        previous_high = -1
        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]

            if price > previous:
                max_profit += profit
                profit = 0
                previous_high = price
            else:
                if previous_high - price > profit:
                    profit = previous_high - price

            previous = price
        max_profit += profit
        return max_profit



if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([5])