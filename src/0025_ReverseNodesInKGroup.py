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
    def check_validation(self, begin, k):
        stack = []
        for i in range(k):
            if not begin:
                return stack, None
            stack.append(begin)
            begin = begin.next
        return stack, begin

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        ret_head = None
        begin = head
        last_sort_node = None
        while begin:
            stack, begin = self.check_validation(begin, k)
            if len(stack) == k:
                if last_sort_node:
                    last_sort_node.next = stack[-1]
                previous = None
                while True:
                    if len(stack) == 0:
                        break
                    node = stack.pop()
                    if not ret_head:
                        ret_head = node
                    if not previous:
                        previous = node
                        continue
                    previous.next = node
                    previous = node
                    last_sort_node = node
                    last_sort_node.next = None
            else:
                if last_sort_node:
                    last_sort_node.next = stack[0]
                previous = None
                while True:
                    if len(stack) == 0:
                        break
                    node = stack.pop(0)
                    if not ret_head:
                        ret_head = node
                    if not previous:
                        previous = node
                        continue
                    previous.next = node
                    previous = node
                    last_sort_node = node
                    last_sort_node.next = None
        return ret_head




if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    manager1 = ListNodeManager(nums)
    l1 = manager1.head
    head = solution.reverseKGroup(l1, 6)
    while head:
        print head.val
        head = head.next