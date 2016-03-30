class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListNodeManager():
    head = None
    def __init__(self, arr):
        previous = None
        for index in range(len(arr)):
            value = arr[index]
            node = ListNode(value)
            if previous:
                previous.next = node
            if index == 0:
                self.head = node
            previous = node

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        tmp = None
        previous = head
        while l1 and l2:
            if l1.val <= l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next
            previous.next = tmp
            previous = tmp

        if l1:
            previous.next = l1
        elif l2:
            previous.next = l2

        return head


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 5, 7, 10, 20]
    manager1 = ListNodeManager(nums)
    l1 = manager1.head

    nums = [2, 6, 7, 11, 15]
    manager2 = ListNodeManager(nums)
    l2 = manager2.head
    head = solution.mergeTwoLists(l1, l2)
    while head:
        print head.val
        head = head.next