class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        roman = ''
        scale = 1000
        i = 6
        while i >= 0:
            digit = num / scale
            if digit != 0:
                if digit <= 3:
                    for j in range(digit):
                        roman += symbol[i]
                elif digit == 4:
                    roman += symbol[i]
                    roman += symbol[i + 1]
                elif digit == 5:
                    roman += symbol[i + 1]
                elif digit <= 8:
                    roman += symbol[i + 1]
                    for j in range(digit - 5):
                        roman += symbol[i]
                elif digit == 9:
                    roman += symbol[i]
                    roman += symbol[i + 2]
            num %= scale
            scale /= 10
            i -= 2
        return roman

if __name__ == "__main__":
    solution = Solution()
    num = 6
    print solution.intToRoman(num)