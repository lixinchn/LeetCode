class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index1, index2 = 0, 0
        ret_arr = []
        while index1 < m and index2 < n:
            if nums1[index1] <= nums2[index2]:
                ret_arr.append(nums1[index1])
                index1 += 1
                continue

            ret_arr.append(nums2[index2])
            index2 += 1

        while index1 < m:
            ret_arr.append(nums1[index1])
            index1 += 1

        while index2 < n:
            ret_arr.append(nums2[index2])
            index2 += 1

        nums1[:] = ret_arr[:]



if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,4,5]
    nums2 = [2,3,4,5,6]
    solution.merge(nums1, len(nums1), nums2, len(nums2))
    print nums1

    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, len(nums2))
    print nums1

    nums1 = [1]
    nums2 = []
    solution.merge(nums1, 1, nums2, 0)
    print nums1

    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, 1)
    print nums1