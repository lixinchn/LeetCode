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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first, second = head, head
        while first and second:
            first = first.next
            second = second.next
            if second:
                second = second.next

            if second == first:
                break

        if not second:
            return None

        first = head
        while first != second:
            first = first.next
            second = second.next
        return second

if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([1,2,3, 1])
    print solution.detectCycle(head)
