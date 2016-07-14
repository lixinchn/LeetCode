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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        previous = None
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                head = head.next
                if previous:
                    previous.next = head
            else:
                if not new_head:
                    new_head = head
                previous = head
                head = head.next
        return new_head



if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([1,1,1,2,3])
    head = solution.deleteDuplicates(head)
    head._print()
