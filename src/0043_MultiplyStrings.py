class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        result = '0'
        scale = 0
        self.hash_num2 = {}
        for each_num1 in num1[::-1]:
            each_num1 = int(each_num1)
            result_temp = self.get_multiply(each_num1, num2)
            result = self.add(result, result_temp + scale * '0')
            scale += 1
        return result

    def get_multiply(self, each_num1, num2):
        if each_num1 in self.hash_num2:
            return self.hash_num2[each_num1]

        result_temp = '0'
        for i in range(each_num1):
            self.hash_num2[i] = result_temp
            result_temp = self.add(result_temp, num2)
        self.hash_num2[each_num1] = result_temp
        return result_temp

    def add(self, num1, num2):
        index = 0
        result = ''
        len_num1 = len(num1)
        len_num2 = len(num2)
        carry = 0
        while True:
            if index >= len_num1 and index >= len_num2:
                break
            each_num1 = int(num1[len_num1 - index - 1]) if index < len_num1 else 0
            each_num2 = int(num2[len_num2 - index - 1]) if index < len_num2 else 0
            result_temp =  each_num1 + each_num2 + carry
            result = str(result_temp % 10) + result
            carry = result_temp / 10
            index += 1
        if carry:
            result = str(carry) + result
        return result


if __name__ == "__main__":
    solution = Solution()
    print solution.multiply('9369162965141127216164882458728854782080715827760307787224298083754', '7204554941577564438')