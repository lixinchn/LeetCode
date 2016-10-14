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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        prev = head
        next_n = prev.next
        prev.next = None

        while next_n:
            real_next = next_n.next
            next_n.next = prev
            prev = next_n
            next_n = real_next
        return prev

if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([1,2,3,4,5])
    head = solution.reverseList(head)
    head._print()
