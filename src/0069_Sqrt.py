class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_temp = -1
        min_temp = -1
        temp = x
        while True:
            if temp * temp > x:
                max_temp = temp
            elif temp * temp < x:
                min_temp = temp
            else:
                return temp

            if max_temp != -1 and min_temp != -1:
                temp = (min_temp + max_temp) / 2
                while True:
                    if max_temp <= min_temp:
                        break
                    if min_temp + 1 == max_temp:
                        if max_temp * max_temp < x:
                            temp = max_temp
                        else:
                            temp = min_temp
                        break
                    if temp * temp > x:
                        max_temp = temp 
                    elif temp * temp < x:
                        if temp < max_temp:
                            min_temp = temp
                    else:
                        break
                    temp = (min_temp + max_temp) / 2
                return temp
            temp = temp / 2

if __name__ == "__main__":
    solution = Solution()
    print solution.mySqrt(8192)