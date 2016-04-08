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

class ListNodeArrManager():
    lists = []
    def __init__(self, arr):
        for i in range(len(arr)):
            arr_list = arr[i]
            manager = ListNodeManager(arr_list)
            self.lists.append(manager.head)


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ret_head = None
        previous_end = None
        next_temp = None
        while head and head.next:
            if not ret_head:
                ret_head = head.next
            if previous_end:
                previous_end.next = head.next
            next_temp = head.next.next
            head.next.next = head
            head.next = None
            previous_end = head
            head = next_temp
        if head and previous_end:
            previous_end.next = head
        if head and not ret_head:
            ret_head = head
        return ret_head

if __name__ == "__main__":
    solution = Solution()
    nums = []
    manager1 = ListNodeManager(nums)
    l1 = manager1.head
    head = solution.swapPairs(l1)
    while head:
        print head.val
        head = head.next

    

