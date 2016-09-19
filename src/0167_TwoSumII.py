class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            index2 = self.find(numbers, target - numbers[i], i + 1, len(numbers) - 1)
            if index2 > 0:
                return [i + 1, index2 + 1]


    def find(self, numbers, target, begin, end):
        if begin > end:
            return -1

        middle = (begin + end) / 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] > target:
            return self.find(numbers, target, begin, middle - 1)
        else:
            return self.find(numbers, target, middle + 1, end)


        
if __name__ == "__main__":
    solution = Solution()
    print solution.twoSum([2,7,11,15], 17)