class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for index in range(len(digits) - 1, -1, -1):
            digit = digits[index]
            new_digit = digit + carry
            carry = new_digit / 10
            digits[index] = new_digit % 10
            if carry == 0:
                break

        if carry >= 1:
            digits.insert(0, carry)

        return digits

if __name__ == "__main__":
    solution = Solution()
    print solution.plusOne([8])
