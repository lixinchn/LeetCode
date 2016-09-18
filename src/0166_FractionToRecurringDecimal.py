class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return 'NaN'
        if numerator == 0:
            return '0'

        negative = False
        if numerator < 0:
            negative ^= True
            numerator *= -1
        if denominator < 0:
            negative ^= True
            denominator *= -1

        ret_str = ''
        result = numerator / denominator
        ret_str += str(result)
        numerator -= result * denominator

        hashmap = {}
        decimals = ''
        index = 0
        while True:
            if numerator == 0:
                break
            numerator *= 10
            if str(numerator) in hashmap:
                split_index = hashmap[str(numerator)]
                decimals = decimals[:split_index] + '(' + decimals[split_index:] + ')'
                print hashmap
                break
            hashmap[str(numerator)] = index
            index += 1
            result = numerator / denominator
            decimals += str(result)
            numerator -= result * denominator

        if decimals:
            ret_str += '.' + decimals
        if negative:
            ret_str = '-' + ret_str
        return ret_str

        
if __name__ == "__main__":
    solution = Solution()
    print solution.fractionToDecimal(1, 6)
