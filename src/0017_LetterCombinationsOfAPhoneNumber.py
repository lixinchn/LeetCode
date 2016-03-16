class Solution(object):
    digits_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def add(self, letters_arr, digits_arr):
        for i in range(len(digits_arr)):
            j = len(digits_arr) - i - 1
            digits_arr[j] += 1
            if digits_arr[j] == len(letters_arr[j]):
                digits_arr[j] = 0
                continue
            break

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters_arr = []
        digits_arr = []
        count = 0
        for digit in digits:
            letters = self.digits_map.get(digit, None)
            if not letters:
                continue
            if count == 0:
                count = len(letters)
            else:
                count *= len(letters)

            letters_arr.append(letters)
            digits_arr.append(0)

        ret_arr = []
        for i in range(count):
            str_temp = ''
            for j in range(len(digits_arr)):
                str_temp += letters_arr[j][digits_arr[j]]
            ret_arr.append(str_temp)
            self.add(letters_arr, digits_arr)
        return ret_arr

if __name__ == "__main__":
    solution = Solution()
    digits = '23'
    print solution.letterCombinations(digits)
