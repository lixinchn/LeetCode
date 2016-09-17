class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        len_1, len_2 = len(arr1), len(arr2)

        index = 0
        while True:
            if index >= len_1 or index >= len_2:
                break
            int1 = int(arr1[index])
            int2 = int(arr2[index])
            if int1 > int2:
                return 1
            elif int1 < int2:
                return -1
            index += 1

        while index < len_1:
            if int(arr1[index]) == 0:
                index += 1
                continue
            break

        while index < len_2:
            if int(arr2[index]) == 0:
                index += 1
                continue
            break

        if index < len_1:
            return 1
        elif index < len_2:
            return -1
        return 0

if __name__ == "__main__":
    solution = Solution()
    print solution.compareVersion('0.1', '1.1')
    print solution.compareVersion('1.5', '11.1')
    print solution.compareVersion('01', '1')
    print solution.compareVersion('1.01', '1.001')
    print solution.compareVersion('1.0.0.0.1', '1.0.0.0.1')
    print solution.compareVersion('1.1.1', '1.1.1.1')
    print solution.compareVersion('1.1.1', '1.1')
    print solution.compareVersion('1.0', '1')