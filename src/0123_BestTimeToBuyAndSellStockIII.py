class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        f1 = [0 for i in range(length)]
        f2 = [0 for i in range(length)]
        
        minV = prices[0]
        f1[0] = 0
        for i in range(1, length):
            minV = min(minV, prices[i])
            f1[i] = max(f1[i - 1], prices[i] - minV)
            
        maxV = prices[length - 1]
        f2[length - 1] = 0
        for i in range(length - 2, -1, -1):
            maxV = max(maxV, prices[i])
            f2[i] = max(f2[i + 1], maxV - prices[i])
        
        res = 0
        for i in range(length):
            if f1[i] + f2[i] > res:
                res = f1[i] + f2[i]
        return res

        
if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([4,1,2])
    print solution.maxProfit([1,2,3,4,5,6,7,8,9])
    print solution.maxProfit([4,5,1,2])
    print solution.maxProfit([1,2,3])
    print solution.maxProfit([3,2,1])
    print solution.maxProfit([1,2,3,4,5,4,3,2,1])
    print solution.maxProfit([1,2,1,3,1,4,1,5,1,6])
    print solution.maxProfit([1,2,3,5,4,7,5,9,6,11])
    print solution.maxProfit([6,1,3,2,4,7])
