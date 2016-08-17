class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        max_price = 0
        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]
            if max_price < price:
                max_price = price
            else:
                profit = max_price - price
                if profit > max_profit:
                    max_profit = profit
        return max_profit

        
if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([7, 1, 5, 3, 6, 4])
    print solution.maxProfit([1,2])