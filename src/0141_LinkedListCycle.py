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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.next == head:
                return True
            head_next = head.next
            head.next = head
            head = head_next
        return False

if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([1,2,3, 1])
    print solution.hasCycle(head)
