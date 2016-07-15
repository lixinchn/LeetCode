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
        previous = None
        temp = head
        while temp:
            previous = temp
            if temp.next and temp.val == temp.next.val:
                while temp.next and temp.next.val == temp.val:
                    temp = temp.next
                temp = temp.next
                previous.next = temp
            else:
                temp = temp.next
        return head



if __name__ == "__main__":
    solution = Solution()
    head = ListNode.create([1,1,2,3,3])
    head = solution.deleteDuplicates(head)
    head._print()
