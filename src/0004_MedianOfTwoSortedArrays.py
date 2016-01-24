class Solution(object):
    def findWorker(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])

        if len(nums1) < k / 2:
            return self.findWorker(nums1, nums2[k / 2:], k - k / 2)
        if len(nums2) < k / 2:
            return self.findWorker(nums1[k / 2:], nums2, k - k / 2)

        if nums1[k / 2 - 1] < nums2[k / 2 - 1]:
            return self.findWorker(nums1[k / 2:], nums2, k - k / 2)
        if nums1[k / 2 - 1] > nums2[k / 2 - 1]:
            return self.findWorker(nums1, nums2[k / 2:], k - k / 2)
        if nums1[k / 2 - 1] == nums2[k / 2 - 1]:
            return min(nums1[k - k / 2 - 1], nums2[k - k / 2 - 1])

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length_of_all = len(nums1) + len(nums2)
        if length_of_all % 2 == 0:
            median1 = (float)(self.findWorker(nums1, nums2, length_of_all / 2))
            median2 = (float)(self.findWorker(nums1, nums2, length_of_all / 2 + 1))
            return (median1 + median2) / 2.0
        else:
            return (float)(self.findWorker(nums1, nums2, length_of_all / 2 + 1))

if __name__ == "__main__":
    solution = Solution()
    # 1. median: 15
    nums1 = [1, 12, 15, 26, 38]
    nums2 = [2, 13, 17, 30, 45, 50]
    print 'expected: 15.0:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 2. median: 16
    nums1 = [1, 12, 15, 26, 38]
    nums2 = [2, 13, 17, 30, 45]
    print 'expected: 16.0:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 3. median: 10.5
    nums1 = [1, 2, 5, 6, 8]
    nums2 = [13, 17, 30, 45, 50]
    print 'expected: 10.5:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 4. median: 9.5
    nums1 = [1, 2, 5, 6, 8, 9, 10]
    nums2 = [13, 17, 30, 45, 50]
    print 'expected: 9.5:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 5. median: 9
    nums1 = [1, 2, 5, 6, 8, 9]
    nums2 = [13, 17, 30, 45, 50]
    print 'expected: 9.0:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 6. median: 2.5
    nums1 = []
    nums2 = [2, 3]
    print 'expected: 2.5:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 7. median: 1.0
    nums1 = [1]
    nums2 = [1]
    print 'expected: 1.0:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 8. median: 3.5
    nums1 = [1]
    nums2 = [2, 3, 4, 5, 6]
    print 'expected: 3.5:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 9. median: 1.5
    nums1 = [1, 2]
    nums2 = [1, 2]
    print 'expected: 1.5:' + str(solution.findMedianSortedArrays(nums1, nums2))

    # 10. median: 1.0
    nums1 = [1, 2]
    nums2 = [1, 1]
    print 'expected: 1.0:' + str(solution.findMedianSortedArrays(nums1, nums2))


    # 11. median: 2.0
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    print 'expected: 2.0:' + str(solution.findMedianSortedArrays(nums1, nums2))