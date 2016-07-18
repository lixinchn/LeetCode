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
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left_head, left = None, None
        right_head, right = None, None
        while head:
            if head.val < x:
                if not left_head:
                    left_head = head
                if not left:
                    left = head
                else:
                    left.next = head
                    left = left.next
            else:
                if not right_head:
                    right_head = head
                if not right:
                    right = head
                else:
                    right.next = head
                    right = right.next
            head = head.next
        if left and right_head:
            left.next = right_head
        if left and not right_head:
            left.next = None
        if right:
            right.next = None

        return left_head if left_head else right_head


if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([])
    head = solution.partition(head, 3)
    head._print()
