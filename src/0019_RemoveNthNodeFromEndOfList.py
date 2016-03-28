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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head

        node_tmp = []
        index = 0
        node_index = head
        while node_index:
            node_tmp.append(node_index)
            index += 1
            node_index = node_index.next

        if n > len(node_tmp):
            return head
        if n == len(node_tmp):
            return head.next

        node_tmp[len(node_tmp) - n - 1].next = node_tmp[len(node_tmp) - n].next
        return node_tmp[0]

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    manager = ListNodeManager(nums)
    head = manager.head
    head = solution.removeNthFromEnd(head, 2)
    while head:
        print head.val
        head = head.next

        