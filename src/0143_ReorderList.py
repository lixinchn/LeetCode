class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(arr):
        head = None
        this = None
        for val in arr:
            node = ListNode(val)
            if not head:
                head = node
                this = node
                continue

            this.next = node
            this = node
        return head

    def _print(self):
        temp = self
        result = ''
        while temp:
            result += str(temp.val) + ','
            temp = temp.next
        print result


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        first, second = head, head
        middle = None
        while second.next:
            first = first.next
            second = second.next
            if second.next:
                second = second.next
            else:
                middle = first
        if not middle:
            middle = first.next

        # reverse second half
        temp = middle
        prev = None
        while temp.next:
            temp_next = temp.next
            temp.next = prev
            prev = temp
            temp = temp_next
        if prev:
            temp.next = prev

        # reorder
        first = head
        while temp:
            head_next = first.next
            temp_next = temp.next

            first.next = temp
            temp.next = head_next

            first = head_next
            temp = temp_next
        first.next = None




if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([1,2,3,4,5])
    solution.reorderList(head)
    head._print()